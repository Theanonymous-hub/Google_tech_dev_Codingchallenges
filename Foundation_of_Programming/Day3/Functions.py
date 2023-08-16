#def add_numbers(num1,num2):
#num2 =int(input("ENter the number2"))
    #sum = num1+num2
    #print("Sum :",sum)
#add_numbers(5,10)
# function definition
def get_square(num):
    return num * num

for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)