# f = open("Saurav.txt", "a")
# a = f.write("Saurav is a good boy\n")
# print(a)
# f.close()

# Handle read and write both
f = open("Saurav.txt", "r+")
print(f.read())
f.write("Today is Saturday\n")
f.write("Thank you\n")