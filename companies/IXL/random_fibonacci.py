import bisect
import random


def random_fib(k):
    fibs = []
    a, b = 0, 1
    while a < k:
        if not fibs or fibs[-1] != a:
            fibs.append(a)
        a, b = b, a + b
    if not fibs:
        return None
    return random.choice(fibs)


# follow-up: called frequently, cache the sequence and binary search the cutoff
class FibSampler:
    def __init__(self):
        self.fibs = [0, 1, 2]

    def _extend_to(self, k):
        while self.fibs[-1] < k:
            self.fibs.append(self.fibs[-1] + self.fibs[-2])

    def sample(self, k):
        if k <= 0:
            return None
        self._extend_to(k)
        count = bisect.bisect_left(self.fibs, k)
        return self.fibs[random.randrange(count)]


random.seed(0)
print([random_fib(10) for _ in range(10)])
print(random_fib(0), random_fib(1), random_fib(2))

sampler = FibSampler()
print([sampler.sample(10) for _ in range(10)])
print(sampler.sample(0), sampler.sample(1), sampler.sample(2))
print(sampler.sample(10 ** 18) < 10 ** 18, len(sampler.fibs))

counts = {}
for _ in range(70000):
    x = sampler.sample(14)
    counts[x] = counts.get(x, 0) + 1
print(sorted(counts.items()))
