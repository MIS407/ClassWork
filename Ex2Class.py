# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:02:14 2015

@author: nilakant
"""

class Person():
    __PCount = 0
    
    def __init__(self, uid, lastname):
        self.uid = uid
        self.lastname = lastname
        self.__PCount += 1
        
    def showMe(self):
        print(self.uid, ' ', self.lastname, self.__PCount)
      
class Student(Person):
    
    def __init__(self, sid, lname, status):
        self.sid = sid
        self.lname = lname
        self.status = status
        Person.__init__(self,sid, lname)
        
    def ShowMe(self):
        
        Person.showMe(self)
        print('My status is ', self.status)
        
def main():
    Joe = Person(101, 'Able')
    Joe.showMe()
    
    Jane = Person(102, 'Baker')
    Jane.showMe()
    
    Jack = Student(103, 'Ripper', 'FullTime')
    Jack.ShowMe()
    
if __name__ == '__main__':
    main()