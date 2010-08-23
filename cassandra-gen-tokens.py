#!/usr/bin/python

#
# A simple script to generate a set of tokens that can be used in a apache cassandra cluster.
#
# The scripts asks for a cluster size then prints that many keys
# 
# Based on benjamin black cassandra summit talk (http://www.slideshare.net/benjaminblack/cassandra-summit-2010-operations-troubleshooting-intro).
# Author: Artie Copeland <artie@yestech.org>
# Distributed under the GNU General Public License, version 3.0.
# Latest version: http://github.com/yestech/yessandbox/blob/master/cassandra-gen-tokens.py
#

class CassandraTokens:	
  def nodes(self, nodes):
    self.nodes = nodes

  def generateRing(self):
    self.ring = []
    for n in range(nodes):
        token = self.calculateToken(n)
        self.ring.append(token)

  def printTokens(self):
    print("Tokens")
    for n in range(len(self.ring)):
        print(self.ring[n])

  def printNodes(self):
    print("Node\tToken")
    for n in range(len(self.ring)):
        print(str(n) +  "\t" + str(self.ring[n]))

  def printRing(self):
    print("Node\tToken Range")
    for n in range(len(self.ring)):
        endToken = (self.ring[(n + 1) % len(self.ring)]) -1
        if (endToken == -1):
           endToken = self.calculateToken(self.nodes)
        tokenRange = "[" + str(self.ring[n]) + " , " + str(endToken) + "]"
        print(str(n) +  "\t" + tokenRange )

  def calculateToken(self, node):
     return (node * (pow(2,127) -1)/self.nodes)

nodes = int(raw_input("How many nodes in the cluster -> "))
t = CassandraTokens()
t.nodes(nodes)
t.generateRing()
t.printTokens()
t.printNodes()
t.printRing()


