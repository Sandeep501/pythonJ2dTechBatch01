# count the no.of vowels in the given string

my_string = input("Please enter a String: ")

vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0

# "Balaji"

for char in my_string:
    if char in vowels:
        cnt+=1
    else:
        pass
    
print(f"{my_string} has {cnt} of vowels")
