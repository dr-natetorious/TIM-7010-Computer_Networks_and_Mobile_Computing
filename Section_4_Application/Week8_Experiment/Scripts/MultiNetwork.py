#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter( Node ):
  "A Node with IP forwarding enabled."

  def config( self, **params ):
    super( LinuxRouter, self).config( **params )
    # Enable forwarding on the router
    self.cmd( 'sysctl net.ipv4.ip_forward=1' )

  def terminate( self ):
    self.cmd( 'sysctl net.ipv4.ip_forward=0' )
    super( LinuxRouter, self ).terminate()

class NetworkTopo( Topo ):
  
  def build( self, **_opts ):
    # Create the router
    router = self.addNode('r0', cls=LinuxRouter, ip='172.15.0.1/16')
    self.setup_switch_1(router)
    self.setup_switch_2(router)
    
  def setup_switch_1(self, router):
    # Create the switch and link to router
    s1 = self.addSwitch('s1')
    self.addLink(s1, router,
      intfName2='r0-sw1-15',
      params2={'ip': '172.15.0.1/16'})
    self.addLink(s1, router,
      intfName2='r0-sw1-20',
      params2={'ip':'172.20.0.1/16'})

    # Add hosts attached to switch 1
    h1 = self.addHost(
      'h1',
      ip='172.15.0.100/16',
      defaultRoute='via 172.15.0.1'
    )

    h2 = self.addHost(
      'h2',
      ip='172.20.0.100/16',
      defaultRoute='via 172.20.0.1'
    )

    self.addLink(h1, s1)
    self.addLink(h2, s1)
    return s1

  def setup_switch_2(self, router):
    s2 = self.addSwitch('s2')
    h3 = self.addHost(
      'h3',
      ip='192.168.10.100/24',
      defaultRoute='via 192.168.10.1'
    )
    h4 = self.addHost(
      'h4',
      ip='192.168.20.100/24',
      defaultRoute='via 192.168.20.1'
    )
    h5 = self.addHost(
      'h5',
      ip='192.168.10.200/24',
      defaultRoute='via 192.168.10.1'
    )

    self.addLink(s2, h3)
    self.addLink(s2, h4)
    self.addLink(s2, h5)

    self.addLink(s2, router,
      intfName2='r0-sw2-10',
      params2={'ip': '192.168.10.1/24'})
    self.addLink(s2, router,
      intfName2='r0-sw2-20',
      params2={'ip':'192.168.20.1/24'})

def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo )  # controller is used by s1-s3
    net.start()
    info( '*** Routing Table on Router:\n' )
    print net[ 'r0' ].cmd( 'route' )
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()

