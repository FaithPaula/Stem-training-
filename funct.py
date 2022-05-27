#functions to replace characters in astring

def replacein(phrase) :
    word=""
    for letter in phrase :
        if letter.lower() in "aeiou" :
            word = word + "g"
        else :
            word=word + letter
    return word
print(replacein(input("Enter a phrase: ")))                