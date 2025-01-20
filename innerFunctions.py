# what is a method/function

def employee(name: str):
    print(f"{name} belongs to J2d")
    
# employee("Sandeep")
# employee("Kalyan")
# employee("Srinath")

def outer_method():
    def inner_method():
        print("This is my inner method")
    
    inner_method()
    print("This is outer method")

# outer_method()


def outer_method(z):
    z = 100 + z
    def inner_method():
        nonlocal z
        z = 20
        print(f"This is my x value: {z}")
    
    def sec_inner_method():
        pass
    
        
    inner_method() # output --> 110
    print(f"This is outer method value: {z}")  # --> 100


outer_method(100)