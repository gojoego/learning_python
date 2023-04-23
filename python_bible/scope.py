# a = 250

# def f1():
#    global a
#    a = 100 # global
#    print(a)

# def f2():
#    a = 50 # local
#    print(a)

# f1()
# f2()
# print(a)

a = [1, 2, 3]

def f1():
   # a[0] = 5 # global keyword not needed
    print(a)

def f2():
   # a = 50 # local
    print(a)

f1()
f2()
print(a)

# cannot overwrite a global value from inside a local scope
# if Python sees you trying to overwrite global value
# it'll block you and create local unless you use global keyword
# exception is when using lists or dictionaries - can overwrite pieces without requiring "global"

