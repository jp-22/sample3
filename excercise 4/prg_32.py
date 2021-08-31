def dec1(func):
    def inner_fu():
        x = func()
        return x ** 2
    return inner_fu


def dec2(func):
    def inner_fu():
        x = func()
        return x+10
    return inner_fu


@dec2
@dec1
def num():
    return 5

print(num())