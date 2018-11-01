'Make a tool for reasoning about normal distributions'

from math import sqrt, tau, exp, erf, hypot
from random import normalvariate
from statistics import mean, stdev

class NormalDist:
    'Tools for manipulating normal distributions'

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    @classmethod
    def from_sample(cls, data):
        'Compute mean and stdev from a sample'
        mu, sigma = mean(data), stdev(data)
        return cls(mu, sigma)

    def __add__(self, other):
        mu = self.mu + other.mu
        sigma = hypot(self.sigma, other.sigma)
        return NormalDist(mu, sigma)

    def examples(self, n=1):
        'Generate *n* samples for a given mean and stdev'
        return [round(normalvariate(self.mu, self.sigma)) for i in range(n)]

    def cdf(self, x):
        'P(X <= x | mu, sigma)'
        return 1/2 * (1 + erf((x - self.mu) / (self.sigma * sqrt(2))))

    def pdf(self, x):
        'P(x < X < x + dx | mu, sigma) / dx'
        variance = self.sigma ** 2
        return 1 / sqrt(tau * variance) * exp(-(x - self.mu)**2 / (2 * variance))

    def __repr__(self):
        return f'NormalDist(mu={self.mu!r}, sigma={self.sigma!r})'

if __name__ == '__main__':

    iq = NormalDist(100, 15)
    sa = NormalDist.from_sample([120, 118, 135, 101, 89, 142, 117, 105, 143, 103, 102, 115])
    mp = NormalDist(17, 5)
    print(iq + mp)
    ss = sa + mp
    print(ss)
    print(ss.cdf(115))
    print(ss.examples(10))
    print
