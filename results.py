#create a function and run it that does the following 
#for a range of intergers between 0 and n(inclusive)
#if the number is an even number,half it
#if the number is an odd number double it
#for the output generated in the previous function,write the results to a file called results.txt

def print_nums (n):
    for num in range (n):
        if num % 2 == 0:
            print(num/2)
        else:
            print(num*2)
    with open("results.txt","w") as f:
        f.write(str(print_nums(n)))
        f.close()
print_nums(10)