def edit(fx):
    def mfx(*x,**y):
        print("good Morning")
        fx(*x,**y)
        print("Thanks")    
    return mfx
@edit  
def hello():
    print("hello world")
    
  
hello()

@edit
def mul(a,b):
    print (a*b)

mul(2,5)
    



# output
good Morning
hello world
Thanks
good Morning
10
Thanks




# code2

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)


# output
Good Morning
Hello world
Thanks for using this function
Good Morning
3
Thanks for using this function
