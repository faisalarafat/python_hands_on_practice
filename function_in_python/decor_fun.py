def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner
@decorfun #same name as decor function name
def num():
    return 5

print(num())