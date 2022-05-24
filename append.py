fruits=["apple" ,"orange" , "banana"]
fruits.append("cherry")
print(fruits)


my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)

fruits=["apple" , "orange" ,"banana"]
fruits_2=["cherry" , "tomato"]
fruits_3=fruits + fruits_2
print(fruits_3)

fruits.extend(fruits_2)
(print(fruits))

fruits_2.clear()
print(fruits_2)

fruits_4=("apple" ,"orange" ,"banana")
print(fruits_4)
print(fruits_4[1])

new_list=list(fruits_4)
new_list.append("tomato")
fruits_4= tuple (new_list)

fruits_5={"apple" ,"oranges" ,"oranges", "oranges"}
print(fruits_5)


mylist=[1 ,2 ,3 , 4, 7]
for el in mylist:
    print(el)
other_list=[]
other_list.append(el)   
print(other_list)

mylist=[1 ,2 ,31, 4, 8]
other_list =[el for el in mylist]
#print(other_list)

for el in mylist:
    if el % 2 == 0 :
        other_list.append(el)
print(other_list)

my_list=[1 ,2 ,31, 4, 8]
other_list=[el for el in mylist if el%2==0]
print(other_list)

def add (a,b) :
    return a+b
result=add(4,6) 
print(result)

def mean(a,b) :
    return (a+b)/2
result=mean(4,6)
print(result)

