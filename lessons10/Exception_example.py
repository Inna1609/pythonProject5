
#raise Exception ('Not supported operation')

def sum(a,b):
    try:
        return a+b
    except TypeError as e:
        print('not supported type')


sum(1, 'sdf')
def sum(a,b):
    try:
        assert a==b
        return a+b
    except AssertionError as e:
        print('we are in assertion error')
    except TypeError as e:
        print('we are in type error')
    finally:
        print('final block of code')
    print('this is code after finally')

sum(2, 1)