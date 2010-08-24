#!/usr/bin/python

""""
Class that handles all the code to generate and print tokens.

Based on benjamin black cassandra summit talk (http://www.slideshare.net/benjaminblack/cassandra-summit-2010-operations-troubleshooting-intro).
Author: Artie Copeland <artie@yestech.org>
Distributed under the GNU General Public License, version 3.0.
""""
class CassandraTokens:	
  def nodes(self, nodes):
    self.nodes = nodes

  def generateRing(self):
    self.ring = []
    for n in range(self.nodes):
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

import unittest
from cassandrautil import CassandraTokens
""""
Provides unit tests for CassandraTokens
""""
class CassandraTokensTestCase(unittest.TestCase):
    def setUp(self):
        self.cassandraToken = CassandraTokens()

    def tearDown(self):
        self.cassandraToken = None

    def testGenerateRing(self):
        self.cassandraToken.nodes(7)
        self.cassandraToken.generateRing()
        expectedRing = [0L,24305883351495604533098186245126300818L,
        48611766702991209066196372490252601636L,72917650054486813599294558735378902454L,
        97223533405982418132392744980505203272L,121529416757478022665490931225631504090L,
        145835300108973627198589117470757804908L]
        self.assertEqual(expectedRing, self.cassandraToken.ring)
        
    def testCalculate10NodesLastToken(self):
        self.cassandraToken.nodes(10)
        token = self.cassandraToken.calculateToken(9)
        expectedToken = 153127065114422308558518573344295695154L
        self.assertEqual(expectedToken, token)
        
    def testCalculate1NodeToken1(self):
        self.cassandraToken.nodes(1)
        token = self.cassandraToken.calculateToken(0)
        expectedToken = 0L
        self.assertEqual(expectedToken, token)

if __name__ == '__main__':
    unittest.main()

