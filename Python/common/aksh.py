

def isContiousPartsSum(x):
    if type(x) != str:
        x = str(x)

    for i in range(len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1, len(x)):
                if int(x[i:j]) + int(x[j:k]) == int(x[k:len(x)]):
                    return True
    return False


print(isContiousPartsSum(9999198))
print(isContiousPartsSum(99101200))
print(isContiousPartsSum(99991982))