#write a program to move zeros

def moveZerosToEnd (orig_arr)->list:
    tempList = []
    i = 0
    index = 0
    Arr_length = len(orig_arr) 
    for i in range(Arr_length):
        if orig_arr[i] != 0:
            orig_arr[index] = orig_arr[i]
            index += 1
        
    while index < Arr_length:
        orig_arr[index] = 0
        index += 1
            
    return orig_arr
    


arr = [1,0,2,3,0,0,8,4,2,0,7,3,1,0,0]
result = moveZerosToEnd(arr)
print(result)