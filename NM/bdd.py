def bdd(f, x, h):
    return (f(x)-f(x-h))/(h)
if __name__  == "__main__":
    fn = input("Enter fn: ")
    x = float(input("enter the element: "))

    def f(x):
        return eval(fn)
    
    h = float(input("Step size: "))
    
    print(f"Root = {bdd(f,x,h)}")
    
