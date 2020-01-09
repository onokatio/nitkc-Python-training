#!/usr/bin/python

inputs = []

while True:
    a = input()
    if a in inputs:
        print("error. The letter is already exist.")
    else:
        inputs.append(a)
    print(inputs)
