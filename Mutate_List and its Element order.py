# To reverse the elements of the List besides reverse the element itself which is also a list.

L = [[1, 2], [3, 4], [5, 6, 7],[-1,0,4,7]]


def deep_reverse(L):
    p = L[::-1]
    s =[]
    for  x in p:
        t=x[::-1]
        s.append(t)
    L[:]=s      #it will mutates the list L
    #L=s        #it will not mutate the list L, as L(which here act as just a ordinary variable) is with in scope of function only
                # and its scope get over once goes out of for loop

deep_reverse(L)
print(L)
