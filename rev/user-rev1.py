arr = []

n = int(input("enter type length of the arrray:"))
for i in range(n):
    user = int(input("Insert number:"))
    arr.append(user)

def reverse(rev_list):
     return rev_list[::-1]
#
#
print(reverse(arr))
