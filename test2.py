def isPowTwo(num:int) -> bool:
    i =0
    while i < num :
        if 2 ** i == num:
            return True
        i += 1
    return False
        
print(isPowTwo(2))


def isPowTwo(num:int) -> bool:
    if num < 1:
        return False
    while num % 2 == 0:
        num = num //2
    
    return num == 1

print(isPowTwo(150))



def isPowTwo(num:int) -> bool:
    if num < 1:
        return False
    
    for i in range(100):
        if num == 1:
            return True
        if num % 2 != 0:
            return False
        num = num // 2
    
    return False

print(isPowTwo(18))

