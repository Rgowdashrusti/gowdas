class MyClass:

    def l(self):
        li=[x**2 for x in range(1, 11)]
        print(li)

    def dict(self):
        myDict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
        print(myDict)

        sDict = {x.upper(): x * 3 for x in 'coding '}
        print(sDict)

tmp=MyClass()
tmp.l()
tmp.dict()

dict={1:'s',2:'ys',3:{5:2,4:5,1:'s'}}
print(dict.get(3))
dict.pop(2)
print(dict)
dict.popitem()
print(dict)
dict.clear()
print(dict)