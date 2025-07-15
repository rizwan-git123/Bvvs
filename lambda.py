add = lambda x,y: x+y
print(add(5,3))

square= lambda x:x**2
print(square(4))

num=[1,2,3,4,5,6]
even_num=list[filter(lambda x:x% 2 ==0,num)]

data=[(1,'apple'),(3,'banana'),(2,'cherry')]
sorted_data=sorted(data,key=lambda x : x [1])
print(sorted_data)

multiply=lambda x ,y ,z:x*y*z
print(multiply(2,3,4,))

numbers=[1,2,3,4,5]
doubled=list[map(lambda x:x%2,numbers)]
print(doubled)

number=[10,15,20,25,30]
odd=list[filter(lambda x:x%2!=0,number)]
print(odd)

