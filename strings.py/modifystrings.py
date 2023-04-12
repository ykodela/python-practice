a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.strip())

a = "Hello World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))