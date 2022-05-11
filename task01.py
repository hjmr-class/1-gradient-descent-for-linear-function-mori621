import random

ALPHA = 1e-3


def func_y_hat(x):
    y_hat = 5.0 * x -3.0
    return y_hat

def func_y(x, a, b):
    y = a * x + b
    return y

def func_error(y, y_hat):
    e = 0.5 * (y - y_hat)**2
    return e

def func_da(x, a, b):
    da = (func_y(x, a, b) - func_y_hat(x)) * x
    return da

def func_db(x, a, b):
    db = (func_y(x, a, b) - func_y_hat(x)) * 1
    return db


if __name__=='__main__':
    a = random.random()
    b = random.random()

    for i in range(500):
        e_sum = 0
        for j in range(100):
            x = random.random() * 100 - 50
            a -= ALPHA * func_da(x, a ,b)
            b -= ALPHA * func_db(x, a, b)
            e_sum += func_error(func_y(x, a, b), func_y_hat(x))
        e_ave = e_sum / 100
        print('{}: {:.4f}'.format(i, e_ave))
    
    print('a = {:.4f}, b = {:.4f}'.format(a, b))