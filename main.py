from math import log
from os import remove
from time import time


def primes_up_to(limit):
    """
    This function gathers a list of the primes up to the limit either from a
    previously calculated file or via fresh calculation.
    """
    # print 'Calculating primes up to {}...'.format(limit)
    try:
        primes_file = open("primes.txt", "r+")
        contents = primes_file.read()
        primes = map(int, contents.split())
        last = primes[-1]
    except:
        primes_file = open("primes.txt", "w+")
        primes = []
        last = 2
    if last < limit:
        for x in range(last, limit + 1):
            couldbe = True
            for p in primes:
                if x % p == 0:
                    couldbe = False
                    # print '{} is divisible by {}, and so not prime.'.format(x, p)
                    break
            if couldbe:
                # print '{} is prime.'.format(x)
                primes.append(x)
                primes_file.write(' {}'.format(x))
    # print 'Complete!'
    primes_file.close()
    return primes


def prime_count(limit):
    """ This is an implementation of the pi function """
    primes = primes_up_to(limit)
    for x in range(2, limit + 1):
        if x % 1000 == 0:
            limited_primes = list(filter(lambda y: y <= x, primes))
            pi = len(limited_primes)
            logx = x / float(log(x))
            print 'At x={} the pi(x) is {} and x/log(x) is {} with difference {}'.format(x, pi, logx, pi - logx)


n = 100000
started = time()
primes_up_to(n)
finished = time()
print 'primes_up_to calculated up to {} in {} seconds.'.format(n, finished - started)
# remove('primes.txt')
