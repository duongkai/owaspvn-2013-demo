from MT19937 import Random
from time import sleep, time
from random import randint

random_coin = Random(0)
while (1):
    sleep_time = randint (40, 60)
    print "sleeping in (s): {0} @time = {1}".format (sleep_time, time())
    sleep (sleep_time)
    random_coin.set (int (time()))
    print "re-sleeping in (s): {0} @time = {1}".format (sleep_time, time())
    sleep (sleep_time)
    a = random_coin.get()
    print "result = {0}".format (a)