listA =[2,3,4,5]
listB = [7,8,9,0]

def dotProduct(x, y):
    if len(x) != len(y): #To ensure length must be equall before doing dot product
        return 0
    else:
        return sum(i[0] * i[1] for i in zip(x, y))

p =dotProduct(listA,listB)
print(p)