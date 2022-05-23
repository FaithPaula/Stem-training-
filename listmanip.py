
mangoes ="book"
for i in mangoes :
    
    print(i)
    print("Done")

#for loops with lists

words=["I" ,"DID" ,"A"]
for word in words:
    print(word +"I")

#counting letters in strings

str = "Hello guys,welcome back to my class" 
count = 0
for x in str :
     if(x =='o') :
        count += 1
print("The number of 0's is: ",count)   

str = "Hello guys,welcome back to my class" 
count = 0
for x in str :
     if(x =='l') :
         continue
     else :  
        print(x)