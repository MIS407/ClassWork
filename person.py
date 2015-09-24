# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

__author__="Sree Nilakanta"

# File person.py 
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
        
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
