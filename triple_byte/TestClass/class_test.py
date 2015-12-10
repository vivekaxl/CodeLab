class testinggeorge:
    def __init__(self):
        self.a = 10
        self.b = 102
    def __str__(self):
        return str(self.a) + str(self.b)

    def __repr__(self):
        return str(self.a) + str(self.b)




tg = testinggeorge()
print tg