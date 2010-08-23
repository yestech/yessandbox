#!/usr/bin/python

#
# A simple script to generate a set of tokens that can be used in a apache cassandra cluster.
#
# The scripts asks for a cluster size then prints that many keys
#
# Based on benjamin black cassandra summit talk (http://www.slideshare.net/benjaminblack/cassandra-summit-2010-operations-troubleshooting-intro).
# Author: Artie Copeland <artie@yestech.org>
# Distributed under the GNU General Public License, version 3.0.
#

nodes = int(raw_input("How many nodes in the cluster -> "))
for n in range(nodes):
  print (n * (pow(2,127) -1)/nodes)
