#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
users = []
for i in xrange(n):
   user = int(raw_input().strip(), 2)
   users.append(user)

# print users

teams = []
maxi = 0
count = 0
for i in xrange(0,  len(users)-1):
	for j in xrange(i+1, len(users)):
		team = users[i] | users[j]
		numberOfTopics = bin(team).count("1")
		if numberOfTopics > maxi:
			maxi  = numberOfTopics
			count = 1
		elif numberOfTopics == maxi:
			count += 1

print maxi
print count