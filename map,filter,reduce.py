#map : used when we need to apply the same function to very element
cube = lambda x: x*x*x
l=[1,2,3,4,5]
newl=[]
for element in l:
    newl.append(cube(element))

print(newl)#this was the lengthy method instead,
print("\n now with the shortcut method \n")
newl= list(map(cube,l))# where cube is function which will be iterated on every item
print(newl)

#filter
#it filters the element based on the arguement
print("filter function: \n")
def filtering(a):
    return a>4
filtered_newl=list(filter(filtering,newl))
print(" the filtered list is as follows: \n", filtered_newl)

#integrating lamba function as well:
print("list will be: ", l)
otherusedmapl= list(map(lambda x: x*x, l))
print("other new maped list is: ", otherusedmapl)
