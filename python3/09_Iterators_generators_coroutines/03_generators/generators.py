# A generator is a function that, unlike a regular function that always
# forgets what it has done and starts from beginning each time it is called,
# a generator remembers where it left off and continues from there at the
# next call. In Python, generators are an easy way to define iterators.

# First, a sneak preview of the last lecture about defining your own data
# types as classes. Here is an iterator defined as a proper class with
# certain "magic" methods to implement the iterator behaviour.

class Squares:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            result = self.start ** 2
            self.start = self.start + 1
            return result
    def __iter__(self):
        return self
    def __str__(self): # Human readable
        return "Range iterator from " + self.start + " to " + self.end
    def __repr__(self): # Expression to generate this object
        return "Squares(" + self.start + ", " + self.end + ")"

# Iterators are much easier to define as generators. Simply using the
# keyword yield instead of return makes Python convert that function to a
# generator type with all the iteration methods loaded in.

def squares(start, end):
    curr = start
    while curr < end:
        yield curr * curr
        curr += 1

print("Printing the squares with Squares class:")
for x in Squares(1, 10):
    print(x, end = ' ')
print("\nPrinting the squares with generator:")
for x in squares(1, 10):
    print(x, end = ' ')
print('\n')

# So far, both examples generated a finite sequence. But there is nothing in
# the laws of nature or man that says that a sequence couldn't be infinite.

def fibonacci():
    yield 1
    yield 1
    curr = 2
    prev = 1
    while True:
        yield curr
        curr, prev = curr + prev, curr

# One one, two twos, three threes, four fours, five fives, ...

def pyramid_series():
    v = 1
    while True:
        for i in range(v):
            yield v
        v += 1

# Finite for all values of start, or infinite for some? Nobody knows!

def collatz(start):
    while True:
        yield start
        if start == 1: break
        elif start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1

# John von Neumann's failed idea for pseudorandom number generation.
# Even the greatest of giants stumble sometimes.

def middle_square(n, k):
    n = str(n).rjust(k, '0')
    while True:
        start = (len(n) - k) // 2
        v = int(n[start:start+k])
        yield v
        n = str(v * v).rjust(2 * k, '0')

# Prime numbers, remembering all the prime numbers generated so far. To
# test whether a number is prime, it is sufficient to test divisibility
# only by the smaller primes found so far.

def primes():
    primes = [2, 3, 5, 7, 11]
    yield from primes # Handy syntactic sugar for yield inside for-loop
    current = 13
    while True:        
        for divisor in primes:
            if current % divisor == 0:
                break
            if divisor * divisor > current:
                primes.append(current)
                yield current
                break
        current += 2

# Since a generator can take parameters, we can write a iterator decorator
# that can be used to modify the result of any existing iterator. We don't
# have to care how that iterator was originally defined, as long at it
# somehow produces new values.

# Let through every k:th element and discard the rest.
def every_kth(it, k):
    count = k
    for x in it:
        count -= 1
        if count == 0:            
            yield x
            count = k

# Duplicate each element k times.
def stutter(it, k):
    for x in it:
        for i in range(k):
            yield x

# Extract all n-element sublists of the sequence from iterator.
def ngrams(it, n):
    result = []
    for v in it:
        result.append(v)
        if len(result) >= n:
            yield result
            result = result[1:]

# Clip the values produced by the iterator to range [lower, upper].
def clip(it, lower, upper):
    for v in it:
        yield max(min(v, upper), lower)

# Extract all unique permutations of 0, ..., n-1 from the sequence,
# assuming that sequence contains only values in 0, ..., n-1.

def unique_permutations(it, n):
    # Set of permutations that we have already seen before.
    seen = set()    
    # Current sublist of n most recent elements.
    curr = []    
    # Counts of how many times each value occurs in current sublist.
    counts = [0 for i in range(n)]
    # How many of those counts are ones, for quick lookup.
    ones = 0
    # Iterate through the values produced by the iterator.
    for v in it:
        curr.append(v)        
        # If sublist is too long, shorten it from the front.
        if len(curr) > n:
            out = curr[0] # Note the outgoing element
            curr = curr[1:]
            # Update the count for the outgoing element out.
            counts[out] -= 1
            if counts[out] == 1:
                ones += 1
            elif counts[out] == 0:
                ones -= 1
        # Update the count for the current element.
        counts[v] += 1
        if counts[v] == 1:            
            ones += 1
            # If each value occurs exactly once, this is a permutation.
            if ones == n:
                currt = tuple(curr)
                if currt not in seen:
                    seen.add(currt)
                    yield currt
        elif counts[v] == 2:
            ones -= 1                   

print("Collatz sequence starting from 12345 is:")
print(list(every_kth(stutter(collatz(12345), 3),3)))

print("The string split into three consecutive words, overlapping:")
print(list(ngrams("Hello world, how are you today?".split(" "), 3)))

# Print each sequence in the corresponding column, each column as far
# down as there are elements in it.

print("Clipping the values between 5 and 10:")
print(list(clip(range(0, 20), 5, 10)))

# Extract the unique permutations from the list.
items = [0, 2, 1, 0, 1, 2, 0, 0, 2, 2, 0, 1]
print(f"Unique 3-permutations of {items} are:")
print(list(unique_permutations(items, 3)))

# Since the iterator produces values one at the time, we could
# analyze sequences too long to fit in memory all at once. First,
# generator that produces random numbers in 0, ..., n - 1 so that
# a number that was seen recently cannot be emitted this round.

import random
def tabu_generator(n, len_, recent = None):
    if recent == None:
        recent = n // 2
    tabu = []
    while len_ > 0:
        v = random.randint(0, n-1)
        if v not in tabu:
            yield v
            tabu.append(v)
            if len(tabu) > recent:
                tabu = tabu[1:]            
            len_ -= 1        

# Count how many permutations occur for different values of recent.

for recent in range(0, 6):
    itemgen = (random.randint(0, 7) for i in tabu_generator(8, 10**5, recent))
    total = 0
    for perm in unique_permutations(itemgen, 8):
        total += 1
    print(f"Using tabu length {recent}, found {total} unique permutations.")

# Constructing the shortest possible sequence that contains all
# permutations of {0, ..., n-1} is an unsolved mathematical problem.
# Google "greg egan haruhi superpermutation" for an interesting story.

def vertical_print(*its, start="", end="", sep=" "):
    its = list(map(iter, its))
    term = len(its)
    while term > 0:
        result = start
        for idx in range(len(its)):
            if its[idx]:
                try:
                    val = str(next(its[idx]))
                except StopIteration:
                    its[idx] = None
                    val = " "
                    term -= 1
            else: val = " "
            result += val + sep                
        result += end
        if term > 0: yield result

for line in vertical_print("Hello", "there", "how", "are", "yeh?",
                           "supercalifragilisticexpialidocious",
                           start = "[", end="]"):
    print(line)

# Sieve of Erathostenes is a classic but inefficient way to generate
# prime numbers. Recursive generators make it a more interesting here
# for the purposes of our discussion.

def sieve_of_erathostenes(m, div):
    if div == 2:
        yield from range(3, m, 2)
    else:
        for i in sieve_of_erathostenes(m, div - 2 if div > 3 else 2):
            if i == div or i % div != 0:
                yield i

# The itertools module defines tons of handy functions to perform
# computations on existing iterators, to be combined arbitrarily.

import itertools as it

print("Middle square 10-digit random numbers from 1234567890:")
print(list(it.islice(middle_square(1234567890, 10), 50)))

print("4-digit random numbers from 540 fall into a cycle right away:")
print(list(it.islice(middle_square(540, 4), 12)))

# Python's built in function enumerate is handy if you need the position
# of each iterated element.

print ("Here are the first 5 prime numbers that contain their index:")
print(list(it.islice(((i, p) for (i, p) in enumerate(primes()) if str(i) in str(p)), 5)))

# Take primes until they become greater than thousand
print ("Here is every seventh prime number up to one thousand:")
print (list(it.takewhile( (lambda x: x <= 1000), every_kth(primes(), 7))))

print("Here are the prime numbers under 10000 filtered with the sieve:")
print(list(sieve_of_erathostenes(10000, 101)))

# Iterators can be turned into various combinatorial possibilities.
# Again, even though there are exponentially many solutions, these
# are generated lazily one at the time as needed by the computation.

print("Here are all possible permutations of [1, 2, 3, 4].")
print(list(it.permutations(range(1, 5))))

print("Here are all possible 3-combinations of [1, 2, 3, 4].")
print(list(it.combinations(range(1, 5), 3)))

print("Here are all possible replacement combinations of [1, 2, 3, 4].")
print(list(it.combinations_with_replacement(range(1, 5), 3)))

# For more examples of iterators and generators, see the itertools
# recipes section in Python documentation.