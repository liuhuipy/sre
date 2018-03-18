# open-falcon源码安装

## 环境准备(Centos7)

### 1.更换yum源
```
yum install -y wget             # 下载wget
mv /etc/yum.repos.d/ /etc/yum.repos.d.backup    # 备份原yum
mkdir /etc/yum.repos.d                          
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all                   # 重建缓存
yum makecache
```
### 2.安装redis和mysql
* 编译安装redis
    ```
    yum -y install gcc              # 安装gcc
    wget http://download.redis.io/releases/redis-3.2.8.tar.gz
    tar -zxvf redis-3.2.8.tar.gz
    cd redis-3.2.8/deps/
    make geohash-int hiredis jemalloc linenoise lua     # 编译依赖
    cd ..
    make && make install            # 编译Redis
    cd utils/
    ./install_server.sh             # 使用脚本安装服务
    systemctl start redis_6379      # 启动服务
    ```
* 安装mysql
    ```
    # 这里就不编译安装了，采用yum安装mariadb简单安装配置
    yum install -y mariadb-server mariadb-devel
    systemctl start mariadb         # 启动mariadb
    mysql_secure_installation       # 初始化配置
    vi /etc/my.cnf                  # 配置文件设置utf8
    [mysqld]                        # 添加两行
    character-set-server=utf8 
    collation-server=utf8_unicode_ci 
    systemctl restart mariadb       # 重启mariadb
    ```
* 初始化mysql表结构
    ```
    # 创建普通用户falcon
    export HOME=/home/falcon
    export WORKSPACE=$HOME/open-falcon
    mkdir -p $WORKSPACE
    cd $WORKSPACE

    git clone https://github.com/open-falcon/scripts.git
    cd ./scripts/
    mysql -h localhost -u root -p < db_schema/graph-db-schema.sql
    mysql -h localhost -u root -p < db_schema/dashboard-db-schema.sql
    mysql -h localhost -u root -p < db_schema/portal-db-schema.sql
    mysql -h localhost -u root -p < db_schema/links-db-schema.sql
    mysql -h localhost -u root -p < db_schema/uic-db-schema.sql
    ```
### 3.安装环境
* open-falcon主要使用Go语言编写，故需安装Go语言开发环境：
    ```
    cd ~
    wget https://dl.google.com/go/go1.9.3.linux-amd64.tar.gz
    tar zxvf go1.9.3.linux-amd64.tar.gz
    mkdir -p workspace/src
    echo "" >> .bashrc
    echo 'export GOROOT=$HOME/go' >> .bashrc
    echo 'export GOPATH=$HOME/workspace' >> .bashrc
    echo 'export PATH=$GOROOT/bin:$GOPATH/bin:$PATH' >> .bashrc
    echo "" >> .bashrc
    source .bashrc
    ```
* clone openfalcon整个代码
    ```
    cd $GOPATH/src
    mkdir github.com
    cd github.com
    git clone --recursive https://github.com/open-falcon/of-release.git
    mv of-release/ open-falcon      # 改名为open-falcon
    ```
    
## Agent
agent用于采集机器负载监控指标，比如cpu.idle、load.1min、disk.io.util等，每隔60秒push给Transfer。agent与Transfer建立了长连接，数据
发送速度比较快，agent提供了一个http接口/v1/push用于接收用户手工push的一些数据，然后通过长连接迅速转发给Transfer。
### 1.源码安装
    ```
    cd $GOPATH/src/github.com/open-falcon/agent
    go get ./...
    ./control build
    ./control pack      # 会生成一个tar.gz的安装包，拿这个包可以去其他服务器上部署agent服务。
    ```
### 2.配置
* 配置文件必须叫cfg.json，已经有写好的cfg.example.json，只需将其copy命名为cfg.json，然后修改相关配置即可。
    ```
    {
    "debug": true, # 控制一些debug信息的输出，生产环境通常设置为false
    "hostname": "ansible.node1.com", # agent采集了数据发给transfer，endpoint就设置为了hostname，默认通过`hostname`获取，如果配置中配置了hostname，就用配置中的
    "ip": "", # agent与hbs心跳的时候会把自己的ip地址发给hbs，agent会自动探测本机ip，如果不想让agent自动探测，可以手工修改该配置
    "plugin": {
        "enabled": false, # 默认不开启插件机制
        "dir": "./plugin", # 把放置插件脚本的git repo clone到这个目录
        "git": "https://github.com/open-falcon/plugin.git", # 放置插件脚本的git repo地址
        "logs": "./logs" # 插件执行的log，如果插件执行有问题，可以去这个目录看log
    },
    "heartbeat": {
        "enabled": true, # 此处enabled要设置为true
        "addr": "127.0.0.1:6030", # hbs的地址，端口是hbs的rpc端口
        "interval": 60, # 心跳周期，单位是秒
        "timeout": 1000 # 连接hbs的超时时间，单位是毫秒
    },
    "transfer": {
        "enabled": true, # 此处enabled要设置为true
        "addrs": [
            "127.0.0.1:8433",
            "127.0.0.1:8433"
        ], # transfer的地址，端口是transfer的rpc端口, 可以支持写多个transfer的地址，agent会保证HA
        "interval": 60, # 采集周期，单位是秒，即agent一分钟采集一次数据发给transfer
        "timeout": 1000 # 连接transfer的超时时间，单位是毫秒
    },
    "http": {
        "enabled": true, # 是否要监听http端口
        "listen": ":1988" # 如果监听的话，监听的地址
    },
    "collector": {
        "ifacePrefix": ["eth", "em", "eno"] # 默认配置只会采集网卡名称前缀是eth、em, eno的网卡流量，配置为空就会采集所有的，lo的也会采集。可以从/proc/net/dev看到各个网卡的流量信息
    },
    "ignore": { # 默认采集了200多个metric，可以通过ignore设置为不采集
        "cpu.busy": true,
        "mem.swapfree": true
    }
    ```
### 3.进程管理
* 通过control脚本各种参数来完成常用操作
    ```
    ./control start     # 启动进程
    ./control stop      # 停止进程
    ./control restart   # 重启进程
    ./control status    # 查看进程状态
    ./control tail      # 用tail -f的方式查看var/app.log
    ```
### 4.验证和接口使用规范
* 看var目录下的log是否正常，或者浏览器访问其1988端口。另外agent提供了一个--check参数，可以检查agent是否可以正常跑在当前机器上
    ```
    ./falcon-agent --check
    ```
* 我们设计初衷是不希望用户直接连到Transfer发送数据，而是通过agent的/v1/push接口转发，接口使用范例：
    ```
    ts=`date +%s`; curl -X POST -d "[{\"metric\": \"metric.demo\", \"endpoint\": \"qd-open-falcon-judge01.hd\",
    \"timestamp\": $ts,\"step\": 60,\"value\": 9,\"counterType\": \"GAUGE\",\"tags\": \"project=falcon,module=
    judge\"}]" http://127.0.0.1:1988/v1/push
    ```

## Transfer

    