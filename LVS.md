# 构建高可用的LVS负载均衡集群

## LVS集群的组成与特点
* Linux虚拟服务器(Linux Virtual Server, LVS)，是一个由章文嵩开发的一款自由软件。利用LVS可以实现高可用的
、可伸缩的Web、Mail、Cache和Media等网络服务。并在此基础上开发支持庞大用户数的、可伸缩的、高可用的电子商务应用。
* 通过LVS要实现的最终目标是：利用Linux操作系统和LVS集群软件实现一个高可用、高性能、低成本的服务器应用集群。

### LVS集群的组成
* 利用架设的服务器集群系统由3个部分组成：最前端的负载均衡层(Load Balancer)，中间的服务器群组层(Server Array)，
底端的数据共享存储层(Shared Storage)
    - 负载均衡层：位于整个集群系统的最前端，由一台或者多台负载调度器(Director Server)组成。LVS核心模块IPVS就
    安装在Director Server上，而Direcotr的主要作用类似于一个路由器，它含有为完成LVS功能所设定的路由表，通过这
    些路由表把用户的请求分发给服务器群组层的应用服务器(Real Server)。同时，在Director Server上还要安装对Real
    Server的监控模块Ldirectord，此模块用于监测各个Real Server服务的健康状况。
    - 服务器群组层：由一组实际运行应用服务的机器组成，Real Server可以是Web服务器、Mail服务器、FTP服务器、DNS
    服务器中的一个或多个，每个Real Server之间通过高速的LAN或分布在各地的WAN相链接。
    - 共享存储层：是为所有Real Server提供共享存储空间和内容一致性的存储区域，一般由磁盘阵列设备组成。

### LVS集群的特点
1. IP负载均衡与负载调度算法
- IP负载均衡技术
    1. LVS的IP负载均衡技术是通过IPVS模块来实现的。IPVS是LVS集群系统的核心软件，主要作用是：安装在Director 
    Server上，同时在Director Server上虚拟出一个IP地址，用户必须通过这个虚拟IP地址访问服务器。这个虚拟的IP称为
    LVS的VIP，即Virtual IP。访问的请求首先经过VIP到达负载调度器，然后由负载调度器从Real Server列表中选取一个
    服务节点响应用户的请求。
    2. IPVS实现负载均衡的方式有3种，分别是NAT、TUN和DR。
        - VS/NAT：即Virtual Server via Network Address Translation，也就是网络地址翻译技术实现虚拟服务器。
        当用户请求到达调度器时，调度器将请求报文的目标地址(即虚拟IP地址)改写成选定的Real Server地址，同时将报文
        的目标端口也改成选定的Real Server的相应端口，最后将报文请求发送到选定的Real Server。在服务器端得到数据
        后，Real Server将数据返回给用户时，需要再次经过负载调度器将报文的源地址和源端口改成虚拟IP地址和相应端口，
        然后把数据发送给用户，完成整个负载调度过程。在NAT方式下，用户请求和响应报文都必须经过Director Server地址
        重写，当用户请求越来越多时，调度器的处理能力将成为瓶颈。
        - VS/TUN：即Virtual Server via IP Tunneling，也就是通过IP隧道技术实现虚拟服务器。在VS/TUN方式中，调
        度器采用IP隧道技术将用户请求转发到某个Real Server，而这个Real Server将直接相应用户的请求，不再经过前端
        调度器。在TUN方式中，调度器将只处理用户的报文请求，从而使集群系统的吞吐量大大提高。
        - VS/DR：即Virtual Server via Direct Routing，也就是用直接路由技术实现虚拟服务器。这种方式的连接调度和
        管理与前两种一样，但它的报文转发方法又有所不同，VS/DR通过改写请求报文的MAC地址，将请求发送到Real Server，
        而Real Server将响应直接返回给客户，免去了VS/TUN中的IP隧道开销。这种方式是3种负载调度方式中性能最好的，但是
        要求Director Server与Real Server必须由一块网卡连在同一物理网段上。
        
- 负载调度算法
    1. 负载调度器要动态地选择一台Real Server响应用户请求，是通过负载调度算法实现的。根据不同的网络服务器需求和服务器
    配置，IPVS实现了8种负载调度算法。4种常见的调度算法有：
        - 轮叫调度(Round Robin)：'轮叫'调度也叫1:1调度，调度器通过'轮叫'调度算法将外部用户请求按顺序1:1地分配到集群
        中每个Real Server上。这种算法平等地对待每一台Real Server，而不管服务器实际的负载状况和连接状态。
        - 加权轮叫调度(Weighted Round Robin)
        - 最少连接调度(least Connections)
        - 加权最少连接调度(Weighted Least Connections) 
        1. 其他4种调度算法分别为：基于局部性的最少连接(Locality-Based Least Connections)、带复制的基于局部性最
        少连接(Locality-Based Least Connections with Replication)、目标地址散列(Destination Hashibng)和源
        地址散列(Source Hashing)。
     
2. 高可用性
- LVS是一个基于内核级别的应用软件，因此具有很高的处理性能。由LVS构建的负载均衡集群系统具有优秀的处理能力，每个服务节点
的故障不会影响整个系统的正常使用，又能够实现负载的合理均衡，使应用具有超高负荷的服务能力，可支持上百万个并发连接请求。

3. 高可靠性
- LVS负载均衡集群软件已经在企业和学校中得到了很好的普及，国内外很多大型的、关键性的Web站点也都采用了LVS集群软件。这些
都说明了LVS的高稳定性和高可靠性。

        