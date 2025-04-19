# sum of digits present inside a string 

a = input("enter anything : ")  
b = 5 
total = 0 
for char in a: 
    # ASCII values to int value 
    num = ord(char) - ord('0')
    total = total + num

print(total) 



