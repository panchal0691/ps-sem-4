cube = lambda x: x*x*x # complete the lambda function 


def fibonacci(n):
    # return a list of fibonacci numbers
    
    l =[0,1]
    
    for i in range(0,n):
        new = l[i] + l[i+1]
        l.append(new)
    
    # newl = list(map(cube,l))
    return l[0:n]
        
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
