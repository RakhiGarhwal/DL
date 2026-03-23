def Perceptron(x1,x2):
    w1,w2=1,1
    b=-1.5
    z=w1*x1+w2*x2+b
    return 1 if z>= 0 else 0
input=[(0,1),(0,0),(1,0),(1,1)]
for x in input:
<<<<<<< HEAD
    print(x,"->",Perceptron(x[0],x[1]))
=======
    print(x,"->",Perceptron(x[0],x[1]))
    ##print("hello")
>>>>>>> 07f769afa21330019dde42d7c84e0c39b169789b
