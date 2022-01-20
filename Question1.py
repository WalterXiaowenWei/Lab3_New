#1) Take a variable with distance in kilometres as input and output the same distance converted to miles.

def convert_function (kilometres):
    miles = kilometres * 0.62137
    return miles

x = 2
while x < 3:
    kilometres = int(input("please input the distance in kilometres: "))
    print("Your input kilometres is equal to ", convert_function(kilometres), "miles")
