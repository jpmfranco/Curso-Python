

def cualquiera(*args):

    count = 0
    for arg in args:
        if count + 1  == len(args):
            return False
        elif args[count] == 0 and args[count + 1] == 0:
            return True
        else:
            count += 1
    return False


print(cualquiera(1,2,3,4,0,8,9,0))
