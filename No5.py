#!/usr/bin/python

inputs = []

while True:
    print("input string a >",end='')
    a = input()
    print("input string b >",end='')
    b = input()
    if b in a:
        print(b,"is exist in ",a)
    else:
        print(b,"is not exist in ",a)
