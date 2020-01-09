#!/usr/bin/python

import random

f = open("./toeic1500.dat", 'r')
print(f.readlines()[random.randrange(0,1499)])
