def countdown(num):
    array = []
    for i in range(num, -1, -1 ):
        array.append(i)
    return array
print(countdown(5))
def print_and_return(arr="[,]"):
    print(arr[0])
    return arr[1]
x = print_and_return([1,2])
print(x)
def firstPlus_Length(arr="[]"):
    sum = arr[0] + len(arr)
    return sum
x = firstPlus_Length([1,2,3,4,5])
print(x)
def valuesGreater_thanSecond(arr="[]"):
    newarr = []
    count = 0
    if len(arr) < 2:
        return False
    else:
        for i in arr:
            if i > arr[1]:
                count += 1
                newarr.append(i)
        print(count)
        return newarr
x = valuesGreater_thanSecond([2,3,2,1,4])
print(x)
y = valuesGreater_thanSecond([3])
print(y)
def thisLength_thatValue(size=1,value=2):
    newlist = []
    for i in range(size):
        newlist.append(value)
    return newlist
x = thisLength_thatValue(6,2)
print(x)
