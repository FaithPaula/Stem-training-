#counting letters in strings

str = "Hello guys,welcome back to my class" 

for x in str :
    if x != 'l' :
     print(x)

outstr = "Hello guys,welcome back to my class" 

for x in str :
    if x != 'l' :
       outstr +=x
print(outstr)  

outstr = "Hello guys,welcome back to my class" 

for x in str :
    if x != 'l':
     if x != 'e':
      if x != 'u' :
         outstr +=x 
print(outstr)   

for i in range(1,10) :
    print(i)
for i in range(1,10,2) :
    print(i)
for i in range(1,100,2) :
    print(i)

