# Nginx初探


* 反转链表；斐波那契数列（递归和非递归的区别）；一个二叉树实现广度优先遍历；一次遍历查找数组中第
二大的数；快速排序；单链表排序；有序链表合并；


* Nginx是一款免费开源的高性能HTTP服务器及反向代理服务器(Reverse Proxy)产品，同时它还可以
提供IMAP/POP3代理服务等功能。

## Nginx的功能特性
* Nginx服务器以其功能丰富著称于世。它既可以作为HTTP服务器，也可以作为反向代理服务器或者邮件
服务器；能够快速响应静态页面的请求；支持FastCGI、SSL、Virtual Host、URL Rewrite、Gzip等
功能；并且支持更多的第三方功能模块的扩展。
* 我们将Nginx提供的基本功能服务从大体上归纳为基本HTTP服务、高级HTTP服务和邮件服务等三大类。
    - Nginx提供基本HTTP服务，可以作为HTTP代理服务器和反向代理服务器，支持通过缓存加速访问，
    可以完成简单的负载均衡和容错，支持包过滤功能，支持SSL等。
    - Nginx提供高级HTTP服务，可以进行自定义配置，支持虚拟主机，支持URL重定向，支持网络监控，
    支持内部SMTP代理服务功能。
    - Nginx作为邮件代理服务器，它支持IMAP/POP3代理服务功能，支持内部SMTP代理服务功能。
    
### 基本HTTP服务
在Nginx提供的基本HTTP服务中，主要包含以下功能特性：
- 处理静态文件；处理索引文件以及支持自动索引。
- 打开并自行管理文件描述符缓存。
- 提供反向代理服务，并且可以使用缓存加速反向代理，同时完成简单负载均衡及容错。
- 提供远程FastCGI服务的缓存机制，加速访问，同时完成简单的负载均衡及容错。
- 使用Nginx的模块化特性提供过滤器功能。Nginx基本过滤器包括gzip压缩、ranges支持、chunked响应、
XSLT、SSI以及图像缩放等。
- 支持HTTP下的安全套接层安全协议SSL。

### 高级HTTP服务
在Nginx提供的高级HTTP服务中，主要包含以下功能特性：
- 支持基于名字和IP的虚拟主机设置。
- 支持HTTP/1.0中的KEEP-Alive模式和管线(PipeLined)模型连接。
- 支持重新加载配置以及在线升级时，无须中断正在处理的请求。
- 自定义访问日志格式、带缓存的日志写操作以及快速日志轮转。
- 提供3xx~5xx错误代码重定向功能。
- 支持重写(Rewrite)模块扩展。
- 支持HTTP DAV模块，从而为Http WebDAV提供PUT、DELETE、MKCOL、COPY以及MOVE方法。
- 支持FLV流和MP4流传输。
- 支持网络监控，包括基于客户端IP地址和HTTP基本认证机制的访问控制、速度限制、来自同一地址的同时
连接数或请求数限制等。
- 支持嵌入Perl语言。

### 邮件代理服务
Nginx提供邮件代理服务也是其基本开发需求之一，主要包含以下功能特性：
- 支持使用外部HTTP认证服务器重定向用户到IMAP/POP3后端，并支持IMAP认证方式和POP3认证方式。
- 支持使用外部HTTP认证服务器认证用户后重定向连接到内部SMTP后端，并支持SMTP认证方式
- 支持邮件代理服务下的安全套接层安全协议SSL。
- 支持纯文本通信协议的扩展协议STARTTLS。

## 常用功能介绍
### HTTP代理和反向代理
* 代理服务和反向代理服务是Nginx服务器作为Web服务器的主要功能之一。在提供反向代理服务方面，Nginx
服务器转发前端请求性能稳定，并且后端转发与业务配置相互分离，配置相当灵活。在进行Nginx服务器配置
时，配置后端转发请求完全不用关心网络环境如何，可以指定任意的IP地址和端口号，或其他类型的链接、请求等。

### 负载均衡
* 负载均衡，包含两方面的含义。一方面是，将单一的重负载分担到多个网络节点上做并行处理，每个节点处理
结束后将结果汇总返回给用户，这样可以大幅提高网络系统的处理能力；第二个方面的含义是，将大量的前端并发
访问或数据流量分担到多个后端网络节点上分别处理，这样可以有效减少前端用户等待响应的时间。
* Nginx服务器的负载均衡策略可以划分为两大类：即内置策略和扩展策略。内置策略主要包含轮询、加权轮询
和IP hash三种；扩展策略主要通过第三方模块实现，种类比较丰富，常见的有url hash、fair等。

### Web缓存
* Nginx服务器的Web缓存服务主要由Proxy_Cache相关指令集和FastCGI_Cache相关指令集构成。
* 其中，Proxy_Cache主要用于在Nginx服务器提供反向代理服务时，对后端源服务器的返回内容进行URL缓存；
FastCGI_Cache主要用于对FastCGI的动态程序进行缓存。另外一款第三方模块ngx_cache_purge主要用于
清除Nginx服务器上指定的URL缓存。




# Nginx服务器的安装部署
* 在centos7上编译安装nginx，首先安装依赖第三方库，通常有pcre库(支持rewrite模块)
```
# yum -y install gcc gcc-c++ automake pcre pcre-devel zlib zlib-devel open openssl-devel
```
* 下载nginx，编译并安装
```
# wget http://nginx.org/download/nginx-1.10.3.tar.gz
# mkdir /Nginx_1_10_3/
# cp nginx-1.10.3.tar.gz /Nginx_1_10_3/
# cd /Nginx_1_10_3/
# tar xf nginx-1.10.3.tar.gz 
# cd nginx-1.10.3
# ll
总用量 676
drwxr-xr-x. 6 1001 1001   4096 11月  7 22:14 auto
-rw-r--r--. 1 1001 1001 265299 1月  31 2017 CHANGES
-rw-r--r--. 1 1001 1001 404694 1月  31 2017 CHANGES.ru
drwxr-xr-x. 2 1001 1001   4096 11月  7 22:14 conf
-rwxr-xr-x. 1 1001 1001   2481 1月  31 2017 configure
drwxr-xr-x. 4 1001 1001     68 11月  7 22:14 contrib
drwxr-xr-x. 2 1001 1001     38 11月  7 22:14 html
-rw-r--r--. 1 1001 1001   1397 1月  31 2017 LICENSE
drwxr-xr-x. 2 1001 1001     20 11月  7 22:14 man
-rw-r--r--. 1 1001 1001     49 1月  31 2017 README
drwxr-xr-x. 9 1001 1001     84 11月  7 22:14 src
```
* 解压出来的文件和目录用途：
    - src目录中存放了Nginx软件的所有源代码。
    - man目录中存放了Nginx软件的帮助文档。
    - html目录中存放了两个后缀名为.html的静态网页文件。
    - conf目录中存放的是Nginx服务器的配置文件
    - auto目录中存放了大量脚本文件，和configure脚本程序有关。
    - configure文件是Nginx软件的自动脚本程序。

* Nginx编译需要使用configure脚本自动生成Makefile文件。
    - --prefix=<path>：       指定Nginx软件的安装路径。默认为/usr/local/nginx/目录
    - --sbin-path=<path>：    指定Nginx可执行文件安装路径。此项只能在安装时指定，默认为<prefix>/sbin/nginx/目录
    - --conf-path=<path>：    指定默认的nginx.conf路径。默认为<prefix>/conf/
    - --pid-path=<path>：     在nginx.conf中未指定pid指令的情况下，指定默认的nginx.pid路径。默认未<prefix>/logs/nginx.pid。
                              nginx.pid保存了当前运行的Nginx服务的进程号。
    - --lock-path=<path>：    指定nginx.lock文件的路径。nginx.lock是Nginx服务器的锁文件，默认为/var/lock/目录
    - --error-log-path=<path>：在nginx.conf中为指定error_log指令的情况下，指定默认的错误日志路径。默认为<prefix>/logs/error.log
    - --http-log-path=<path>：在nginx.conf中未指定error_log指令的情况下，指定默认访问日志的路径。默认为<prefix>/logs/access.log
    - --user=<user>：         在nginx.conf中未指定user指令的情况下，指定默认的Nginx服务器进程的属主用户，即Nginx进程运行的用户。默认为nobody，表示不限制。
    - --group=<group>：       在nginx.conf中未指定group指令的情况下，指定默认的Nginx服务器进程的属主用户组，即Nginx进程运行的用户组。默认未nobody
    - --builddir=<dir>：      指定编译时的目录
    - --add-module=<path>：   指定第三方模块的路径，用以编译到Nginx服务器中
    - --with-poll_module：    声明启用poll模块。poll模块是信号处理的一种方法。
    - --without-poll_module： 声明禁止poll模块
    ......
    
* 使用./configure命令配置并生成Makefile文件
```
./configure --prefix=/Nginx
```
* 使用make命令进行编译
```
# make
# make install
```

## Nginx服务的启停控制

### Nginx服务的信号控制
* Nginx服务在运行时，会保持一个主进程和一个或多个worker process工作进程。我们通过给Nginx服务的主进程发送信号就可以控制
服务的启停了。
* 获取PID有两个途径。一是默认在Nginx服务器安装目录下的logs目录中会产生文件名为nginx.pid的文件，文件中保持的就是Nginx
服务主进程的PID；二是通过ps命令查看nginx相关进程。
```
# cat nginx.pid 
25713
# ps -ef | grep nginx
root      25713      1  0 23:46 ?        00:00:00 nginx: master process ./sbin/nginx
nobody    25714  25713  0 23:46 ?        00:00:00 nginx: worker process
root      25743   2685  0 23:55 pts/0    00:00:00 grep --color=auto nginx
```
* Nginx服务主进程信号控制方法：
    - TERM或INT：快速停止Nginx服务
    - QUIT：平缓停止Nginx服务
    - HUP：使用新的配置文件启动进程，之后平缓停止原有进程，即平滑重启
    - USR1：重新打开日志文件。常用于日志切割
    - USR2：使用新版本的Nginx文件启动服务，之后平缓停止原有Nginx进程，即平滑升级
    - WINCH：平缓停止worker process，用于Nginx服务器平滑升级
* 启动Nginx，启动后可以使用ps -ef | grep nginx命令查看nginx服务进程状态
```
# ./sbin/nginx
```
### Nginx服务的停止
* 停止Nginx服务的两种方法：快速停止和平缓停止
* 使用kill命令
```
# kill -TERM | -INT | -QUIT `cat /Nginx/logs/nginx.pid`
其中，TERM和INT信号用于快速停止，QUIT用于平缓停止。
```
### Nginx服务的重启
* 平滑重启：Nginx服务进程接收到信号后，首先读取新的Nginx配置文件，如果配置语法正确，则启动新的Nginx服务
然后平缓关闭旧的服务进程；如果新的Nginx配置有问题，将显示错误，仍然使用旧的Nginx进程提供服务。
* 使用命令实现Nginx服务的平滑重启：
```
# kill -HUP `cat /Nginx/logs/nginx.pid`
```
### Nginx服务器的升级
* 如果要对当前Nginx服务器进行版本升级，最简单的办法是停止当前Nginx服务，然后开启新的Nginx服务，但这样会
导致一段时间内用户无法访问服务器，这显然是不行的。
* 平滑升级：Nginx服务接收到USR2信号后，首先将旧的nginx.pid文件添加后缀.oldbin，变为nginx.pid.oldbin
文件；然后执行新版本Nginx服务器的二进制文件启动服务。如果新的服务启动成功，系统中将有新旧两个Nginx服务共同
提供Web服务。之后需要向旧的Nginx服务进程发送WINCH信号，使旧的Nginx服务平滑停止，并删除nginx.pid.oldbin
文件。在发送WINCH信号之前，可以随时停止新的Nginx服务。
```
# kill -USR2 `cat /Nginx/logs/nginx.pid`
# kill -WINCH `cat /Nginx/logs/nginx.pid` 
```

## Nginx服务器基础配置指令
* 默认Nginx服务器配置文件都存放在安装目录conf中，主配置文件名为nginx.conf。
```
#user  nobody nobody;                           #指定运行Nginx服务器的用户(组)
worker_processes  1;                            #允许生成的worker process数，理论上说，worker process
                                                #的值越大，可以支持的并发处理量也越多。

#error_log  logs/error.log;                     #错误日志存放路径
#error_log  logs/error.log  notice;             #错误日志类型
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;                     #Nginx进程PID存放路径


events {    
    use epoll;                                  #配置事件驱动模型            
    worker_connections  1024;                   #设置每个worker process可以同时支持的最大连接数
}


http {                                          #http块    
    include       mime.types;                   #定义MIME-Type
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';
                                                #定义请求处理日志的格式
                                                
    #access_log  logs/access.log  main;         #定义日志存放路径

    sendfile        on;                         #是否开启sendfile传输文件
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;                      #设置连接超时时间

    #gzip  on;

    server {                                    #server块
        listen       8081;                      #配置虚拟主机的监听配置
        server_name  myserver1;                 #配置虚拟主机的名称或IP配置

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {                            #location块，在http/server的location中生效
            root   html;                        #配置请求的根目录
            index  index.html index.htm;        #设置我在默认首页
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html; #设置网站的错误页面
        location = /50x.html {                  
            root   html;
        }
    }
    ...
}
```
* nginx.conf一共由三部分组成，分别为全局块、events块和http块。在http块中，又包含http全局块、多个server
块。每个server块中，可以包含server全局块和多个location块。
* 全局块
    - 全局块是默认配置文件从开始到events块之间的一部分内容，主要设置一些影响Nginx服务器整体运行的配置指令，
    因此这些指令的作用域是Nginx服务器全局。
    - 通常包括配置运行Nginx服务器的用户组、允许生成的worker process数、Nginx进程PID存放路径、日志的存放
    路径和类型以及配置文件引入等。
* events块
    - events块涉及的指令主要影响Nginx服务器与用户的网络连接。常用到的设置包括是否开启对多worker process
    下的网络连接进行序列化，是否允许同时接收多个网络连接，选取哪种事件驱动模型处理连接请求，每个worker
    process可以同时支持的最大连接数等。
* http块
    - http块是Nginx服务器配置中的重要部分，代理、缓存和日志定义等绝大多数的功能和第三方模块的配置都可以放在
    这个模块中。http块中可以包含自己的全局块，也可以包含server块。
    - 可以在http全局块中配置的指令包括文件引入、MIME-Type定义、日志自定义、是否使用sendfile传输文件、连接
    超时时间、单连接请求数上限等。
* server块
    - server块和'虚拟主机'有着密切联系。虚拟主机技术将一台服务器的某项或者全部服务内容逻辑划分为多个服务单位，对外表现为多个服务器，从而充分利用
    服务器硬件。从用户角度来看，一台虚拟主机和一台独立的硬件主机是完全一样的。
    - 虚拟主机技术使得Nginx服务器可以在同一台服务器上只运行一组Nginx进程，就可以运行多个网站。
    - 每一个http块都可以包含多个server块，而每个server块就相当于一台虚拟主机，它内部可有多台主机联合提供服务。
    - 和http块相同，server块也可以包含自己的全局块，同时可以包含多个location块。在server全局块中，最常见的
    两个配置项是本虚拟主机的监听配置和本虚拟主机的名称或IP配置。
* location块
    - 每个server块中可以包含多个location块。location块的主要作用是，基于Nginx服务器接收到的请求字符串，对
    除虚拟主机名称之外的字符串进行匹配，对特定的请求进行处理。地址定向、数据缓存和应答控制等功能都在这部分实现。
    - location表达式类型：
        * ～表示执行一个正则匹配，区分大小写
        * ～*表示执行一个正则匹配，不区分大小写
        * ^~表示普通字符匹配。使用前缀匹配。如果匹配成功，则不再匹配其他location
        * =进行普通字符精确匹配。也就是完全匹配
        * @它定义一个命名的location，使用在内部定向时，例如error_page，try_files
    - location优先级：
    - 在nginx的location和配置中location的顺序没有太大关系。正则location表达式的类型与顺序有关。相同类型的
    表达式，能够匹配字符串长的会优先匹配。
    - 以下是按优先级排序说明：
        * 字符精确的优先级最高，一旦匹配成功，则不再查找其他匹配项
        * 所有剩下的常规字符串，最长的匹配，如果这个匹配使用^~前缀，则不再查找其他匹配项
        * 正则匹配的优先级次之，如果写了多个正则location，则按配置顺序依次查找，一旦找到，则不再查找下去
        * 如果第3条规则产生匹配的话，结果被使用。否则，使用第2条规则的结果
    
   
## Nginx服务器的Rewrite功能
### Nginx后端服务器组的配置的5个指令
* upstream指令
    - 语法结构为：upstream name { ... } 
    - 其中，name是给后端服务器组起的组名，花括号中列出后端服务器组中包含的服务器。默认情况下，某个服务器组接收到
    请求后，按照轮叫调度(Round-Robin,RR)策略顺序选择组内服务器处理请求。
* server指令
    - 语法结构为：server address [parameters];
    - address，服务器的地址，可以是包含端口号的IP地址(IP:Port)、域名或者以"unix:"为前缀用于进程间通信的
    Unix Domain Socket。
    - parameters，为当前服务器配置更多属性。
        * weight=number，为组内服务器设置权重，权重值高的服务器被优先用于处理请求。此时组内服务器的选择策略为
        加权轮叫策略。组内所有服务器的权重默认设置为1，即采用一般轮叫调度原则处理请求。
        * max_fails=number，设置一个请求失败的次数。在一定时间范围内，当对组内某台服务器请求失败的次数超过该
        变量设置的值时，认为该服务器无效。
        * fail_timeout=time，有两个作用，一是设置max_fails指令尝试请求某台组内服务器的时间；另一个作用是在
        检查服务器是否有效时，如果一台服务器被认为是无效的，该变量设置的时间为认为服务器无效的持续时间。默认10s
        * backup，将某台组内服务器标记为备用服务器，只有当正常的服务器处于无效状态或者繁忙状态时，该服务器才被
        用来处理客户端请求。
        * down，将某台组内服务器标记为永久的无效状态，通常与ip_hash指令配合使用。
    ```
    upstream backend
    {
        server backend.example.com weigth=5;
        server 127.0.0.1:8080 max_fails=3 fail_timeout=30s;
        server unix:/tmp/backend3;
    }
    ```    
* ip_hash指令
    - 该指令用于实现会话保持功能，将某个客户端的多次请求定向到组内同一台服务器上，保证客户端与服务器之间建立稳定的
    会话。只有当该服务器处于无效状态时，客户端请求才会被下一个服务器接收和处理。其语法结构为：
    ```
    ip_hash；
    ```
    - ip_hash指令不能与server指令中的weight变量一起使用。由于ip_hash技术主要根据客户端IP地址分配服务器，因此在
    整个系统中，Nginx服务器应该是处于最前端的服务器，这样才能获取到客户端的IP地址，否则它得到的IP地址将是位于它前面
    的服务器地址，从而就会产生问题。同时要注意，客户端IP地址必须是C类地址。
    ```
    upstream backend
    {
        ip_hash;
        server myback1.proxy.com;
        server myback2.proxy.com;
    }
    ```
    - 实例中配置了一个名为backend的服务器组，包含两台后端服务器myback1.proxy.com和myback2.proxy.com。在添加
    ip_hash指令后，我们使用同一个客户端向Nginx服务器发送请求，将会看到一直是由服务器myback1.proxy.com响应；如果
    注释ip_hash指令后进行相同的操作，发现组内的两台服务器轮流响应请求。
* keepalive指令
    - 指令用于控制网络连接保持功能。通过该指令，能够保证Nginx服务器的工作进程为服务器组打开一部分网络连接，并且将
    数量控制在一定的范围之内。其语法结构为：
    ```
    keepalive connections;
    ```
    其中，connections为Nginx服务器的每一个工作进程允许该服务器组保持的空闲网络连接数的上限值。如果超过该值，工作
    进程将采用最近最少使用的策略关闭网络连接。
* least_conn指令
    - 该指令用于配置Nginx服务器使用负载均衡策略为网络连接分配服务器组内的服务器。该指令在功能上实现了最少连接负载均
    衡算法，在选择组内的服务器时，考虑各服务器权重的同时，每次选择的都是当前网络连接最少的那台服务器，如果这样的服务
    器有多台，就采用加权轮叫原则选择权重最大的服务器。其语法结构为：
    ```
    least_conn;
    ```

* rewrite规则相关指令
    - if指令
        * 该指令用来支持条件判断，并根据条件判断结构选择不同的Nginx配置，可以在server块或location块中配置该指令。
        ```
        if ( condition ) { ... }
        ```
        * 其中，花括号代表一个作用域，形成一个if配置块，是条件为真时的Nginx配置。condition为判断条件(true/false)
        它可以支持几种设置方法：
            - 变量名。如果变量的值为空字符串或者以"0"开头的任意字符串，if指令认为条件为false，其他认为条件为true
            ```
            if ($slow) {
                ... #Nginx配置
            }
            ```
            - 使用"="和"!="比较变量和字符串是否相等，相等时if指令认为条件为true，反之为false。
            ```
            if ($request_method = POST) {
                return 405;
            }
            ```
    - break指令
    该指令
    
    
    
    
    
    
        
    
        
    
    
    
    
    



  

