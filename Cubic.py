from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def initTopo():
        self = Mininet(link=TCLink)
        # Add server, client, and router
        server = self.addHost('server', ip="10.0.10.10/24", mac="00:00:00:00:00:01")
        client = self.addHost('client', ip="10.0.11.10/24", mac="00:00:00:00:00:02")
        router = self.addHost('router')

        self.addLink(router, server, bw = 2, max_queue_size = 100)
        self.addLink(router, client, bw = 1000, max_queue_size = 100)
	self.build()

        router.cmd("ifconfig router-eth0 0")
        router.cmd("ifconfig router-eth1 0")
        router.cmd("ifconfig router-eth0 hw ether 00:00:00:00:01:01")
        router.cmd("ifconfig router-eth1 hw ether 00:00:00:00:01:02")
        router.cmd("ip addr add 10.0.10.1/24 brd + dev router-eth0")
        router.cmd("ip addr add 10.0.11.1/24 brd + dev router-eth1")
        router.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
	server.cmd("sysctl -w net.ipv4.tcp_congestion_control= cubic")
	client.cmd("sysctl -w net.ipv4.tcp_congestion_control= cubic")
        server.cmd("ip route add default via 10.0.10.1")
        client.cmd("ip route add default via 10.0.11.1")

        print "*** Running CLI"
        CLI(self)
        print "*** Stopping network"
        self.stop()

if __name__ == '__main__':
    setLogLevel('info')
    initTopo()  
