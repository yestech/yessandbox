#!/usr/bin/python

nodes = int(raw_input("How many nodes in the cluster -> "))
limit = nodes
for n in range(limit):
  print (n * (pow(2,127) -1)/nodes)
