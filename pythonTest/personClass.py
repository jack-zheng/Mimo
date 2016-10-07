class person:
    name = "p name"
    age = "2"

    def walk(self):
        print("I can walk")

    def isAlive(self):
        return True

if __name__ == '__main__':
    p1 = person()
    print(p1.age)
    print(p1.name)
    p1.walk()
    print(p1.isAlive())
