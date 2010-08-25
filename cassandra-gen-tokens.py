#!/usr/bin/python

#
# A simple script to generate a set of tokens that can be used in a apache cassandra cluster.
# The script relys on the module "cassandrautil" to be available.
#
# The scripts asks for a cluster size then prints that many keys
# 
# Based on benjamin black cassandra summit talk (http://www.slideshare.net/benjaminblack/cassandra-summit-2010-operations-troubleshooting-intro).
# Author: Artie Copeland <artie@yestech.org>
# Distributed under the GNU General Public License, version 3.0.
# Latest version: http://github.com/yestech/yessandbox/blob/master/cassandra-gen-tokens.py
#
# 
#

from cassandrautil import CassandraTokens

nodes = int(raw_input("How many nodes in the cluster -> "))
t = CassandraTokens()
t.nodes(nodes)
t.generateRing()
t.printTokens()
t.printNodes()
t.printRing()


