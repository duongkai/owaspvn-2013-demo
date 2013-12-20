from MT19937 import Random
from time import sleep, time
from sys import argv

print "Started bruteforcing MT19937..."
counter = int (time())
while (1):
    first = Random (counter).get()
    if first == int (argv[1]):
        print "OUT! Seeder = {0}".format (counter)
        break
    counter -= 1