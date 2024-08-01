num=int(input("enter a number"))
#...................................................
hexdecimal_num = ""
temp = num
while temp > 0:
    remainder = temp % 16
    if remainder < 10:
        hexdecimal_num = str(remainder) + hexdecimal_num
    else:
        hexdecimal_num = chr(remainder+55) + hexdecimal_num
    temp = temp // 16
#...................................................
octal_num = ""
temp = num

while temp > 0:
    remainder = temp % 8
    octal_num = str(remainder)+octal_num
    temp = temp // 8

    
print(hexdecimal_num)
print(octal_num)