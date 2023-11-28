import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['#','@','!','%','$','&','*']
print("welcome to password generator")
nr_letters=int(input(f"how many letters you want\n"))
nr_numbers=int(input(f"how many numbers you want to add\n"))
nr_symbols=int(input(f"how many symbols you want to add\n"))
password=""
for char in range(1,nr_letters+1):
    password +=random.choice(letters)
for char in range(1, nr_numbers + 1):
     password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
         password += random.choice(symbols)
print(password)
