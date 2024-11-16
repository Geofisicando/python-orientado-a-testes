def soma(x,y):
    '''
    Sum two integers
    '''
    return x+y

def inc(x):
    '''
    Add 1 to x
    '''
    return x+1

def test_result():
    '''
    Test function soma
    '''
    assert soma(1,1) == 2

def test_inc():
    '''
    Test inc function
    '''
    assert inc(1) == 3
