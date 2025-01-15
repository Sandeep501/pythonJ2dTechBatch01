my_string = input("Please enter a string: ")

vowels = ["a", "e", "i", "o", "u"]

cnt=0

for char in my_string:
    if char in vowels:
        cnt+=1
    else:
        pass

print(f"{my_string} has {cnt} vowels")