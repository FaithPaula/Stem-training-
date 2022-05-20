words = ("apples" , "love" , "People" , "!")
print(words[0])
print(words[1])
print(words)

# lists can store any data types
dat = ('a' , 1 , "foo" , 6 , 7 , "Hey!")
print(dat)

#nested lists
m = [
    [5,7.8],
    [3,2,1]
    ]
print(m[1][2]) 
print(m[1][2])    
print(m)

#strings - can also be indexed as lists

str = "Hello class"
print(str[5])
print(str[6])
print(str[7-3]) 

strg = ["Hello" , "class" , "123" , "51" , "abc" , "Hey" , 'b' , 'a']
print(strg)
print(strg[5])
print(strg[6])
print(strg[7-3])
strg[0]= strg[7-2]
print (strg)

#lists index cannot be readdressed like lists

subjects = ["Math" , "Science" , "Religious"]
subjects[2] = "mechanics"
print(subjects) 

