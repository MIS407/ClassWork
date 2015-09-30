# import person as pr
import person *
from person import *
# to access Person and Manager classes do
from person import Person, Manager

#to access Manager class only!
from person import Manager

#joe = pr.Person(101, 'Joe Jones')

joe = Person(101, 'Joe Jones')
Jane = Manager(102, 'Jane Eyre')

# newFunc() uses module and accesses Student class locally.
def newFunc():
    import person Student
    Kathy = (103, 'Kate Jona')

def nextFunc():
    pass
