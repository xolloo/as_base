def sub_fun(conut):
    print(conut)
    for i in range(conut):
        print(i, "sub")
        yield i


def func(val: int):
    coof = (yield)
    val += coof
    yield from sub_fun(val)
    val += coof
    yield from sub_fun(val)


if __name__ == '__main__':
    gen = func(4)
    gen.send(None)
    val2 = gen.send(10)
    print(val2)
    for g in gen:
        print(g)
