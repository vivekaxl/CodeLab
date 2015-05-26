from __future__ import division
from random import random, randint
class Requirement:
    risk_min = 1
    risk_max = 5
    cost_min = 10
    cost_max = 20
    def __init__(i, id):
        i.id = id
        i.risk = int(i.risk_min + random() * (i.risk_max - i.risk_min))
        i.cost = int(i.cost_min + random() * (i.cost_max - i.cost_min))

class Client:
    wt_min = 0
    wt_max = 5
    def __init__(i, id, req):
        i.id = id
        i.weight = int(i.wt_min + random() * (i.wt_max - i.wt_min))
        i.importance = [randint(0,5) for _ in xrange(req)]

class Release:
    def __init__(self, id, budget_release):
        self.id = id
        self.budget = budget_release


class NRP:
    def __init__(self, requirements, releases, clients, density, budget):
        self.trequirements = requirements
        self.treleases = releases
        self.tclients = clients
        self.tdensity = density
        self.tbudget = budget
        self.requirement = None
        self.client = None
        self.release = None
        self.precedence = []

    def generate_precedence(self):
        precedence = [[0 for _ in xrange(self.trequirements)] for _ in xrange(self.trequirements)]
        temp = []
        for _ in xrange(int(self.tdensity * self.trequirements**2)):
            while True:
                row = randint(self.trequirements)
                col = randint(self.trequirements)
                t = row * 1000 + col
                if t not in temp: temp.append(t)

        for t in temp: precedence[int(t/1000)][t%1000] = 1
        return precedence

    def generate_data(self):
        self.requirement = [Requirement(i) for i in xrange(self.trequirements)]
        self.client = [Client(i, self.trequirements) for i in xrange(self.tclients)]
        budget_release = int((sum(req.cost for req in self.requirement) * (self.tbudget/100))/self.treleases)
        self.release = [Release(i, budget_release) for i in xrange(self.treleases)]
        self.precedence = self.generate_precedence()

    def print_data(i):
        print [c.weight for c in i.client]
        for p in i.precedence:
            print p
        for r in i.requirement:
            print r.cost, r.risk
        for c in i.client:
            print c.importance
        print [r.budget for r in i.release]

    def evaluate(self, requirement):


if __name__ == "__main__":
    problem = NRP(50, 5, 5, 0, 80)
    problem.generate_data()
    problem.print_data()







