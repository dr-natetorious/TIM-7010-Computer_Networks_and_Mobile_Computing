#!/usr/bin/python

# Import the Topology Base Class
from mininet.topo import Topo

# Declare the custom topology map
class MyTopo( Topo ):

  def __init__( self ):
    "Create custom topo."

    # Initialize base class
    Topo.__init__( self )

    # Add hosts and switches
    s1 = self.addSegment('s1', 2)
    s2 = self.addSegment('s2', 3)
    s3 = self.addSegment('s3', 2)
    s4 = self.addSegment('s4', 1)
    s5 = self.addSegment('s5', 4)

    # Define links between each switch
    self.addLink(s1, s2)
    self.addLink(s1, s3)
    self.addLink(s3, s4)
    self.addLink(s4, s5)
    
  # Create a switch and adds a given number of hosts
  def addSegment(self, name, host_count):
    switch = self.addSwitch(name)
    for i in range(0, host_count):
      host_name = name+ '_host_'+str(i)
      host = self.addHost(host_name)
      self.addLink(switch, host)
    
    return switch

# Export the topologies
topos = { 'mytopo': ( lambda: MyTopo() ) }