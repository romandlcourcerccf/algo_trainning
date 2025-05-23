class Test():
    pass


root = Test()

def m(v):
    if not v:
        v = Test()

m(root)

print(root)
