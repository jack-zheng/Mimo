class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("there are %d turtle and %d fish" % (self.turtle.num, self.fish.num))

pool = Pool(10, 5)
pool.print_num()
print(pool.turtle.num)
