string = input("Enter string inputs:")
n = input("Enter the letter that you want to search for:")

count = 0

for i in string:
    if i == n:
        count = count + 1

print("count is:" + str(count))
