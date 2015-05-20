import itertools

class individual:
    newid = itertools.count().next
    def __init__(self, decision, objectives=None):
        self.id = individual.newid()
        self.decision = decision
        self.objectives = objectives
        self.neighbours = []


