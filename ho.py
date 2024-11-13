print("harry" .capitalize()) #Harry

print("Hello Harry" .casefold()) #hello harry print("hello World" .center(20)) # hello World

print("hello World" .count('1')) #3 print("hello World" .encode()) #b'hello World'

print("hello World" .endswith('.')) #False

print("H\te\t\t\to" .expandtabs(2)) #Hello

print("hello World" .find('wor')) #6

print("{price:.2f}$".format(price=49)) #49.00$

print("hello World" .index('Wor')) #6

print("hello World".split()) #['hello', 'World"] print("hi World" .replace("World", "harry")) #hi harry

print("hello World 20" .isdigit()) #False

print("Complex".isalpha()) #True

print("50" .zfill(10)) #0000000050

print("hello World".upper()) #HELLO WORLD

print("I'm harry".swapcase()) #i'M HARRY

print("Company12" .isalnum()) #True

print("Company12" .isascii()) #True

print("Company12" .isdecimal()) #False

print("hello_World" .isidentifier()) #True print("hello_World" .islower()) #False

print("Hellol\nAre you #1?" .isprintable()) #False

print("".isspace()) #True

print("Mango" .maketrans("M", "T")) #{77: 84)


print("Hello World" .startswith("Hello")) #True

print("'hello' 'World'" .rsplit(","))#["'hello' 'World'"] print("hello\nworld" .splitlines()) #['hello', 'world'