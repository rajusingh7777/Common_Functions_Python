l =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

func = lambda x: [y for z in x for y in func(z)] if type(x) is list else[x]

print(func(l))

