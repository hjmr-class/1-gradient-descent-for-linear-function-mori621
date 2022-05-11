import random

#変化させるのもあり
ALPHA = 1e-3


def func_y_hat(x):
    y_hat = 2 * x**2 + 5 * x + 7
    return y_hat

def func_y(x, a, b, c):
    y = a * x**2 + b * x + c
    return y

def func_error(y, y_hat):
    e = 0.5 * (y - y_hat) * (y - y_hat)
    return e

def func_d(x, a, b, c):
    da = (func_y(x, a, b, c) - func_y_hat(x)) * x**2
    db = (func_y(x, a, b, c) - func_y_hat(x)) * x
    dc = (func_y(x, a, b, c) - func_y_hat(x)) * 1
    return da, db, dc


if __name__=='__main__':
    a = random.random()
    b = random.random()
    c = random.random()

    for i in range(500):
        e_sum = 0
        for j in range(100):
            x = random.random() * 10 - 5
            da, db, dc = func_d(x, a, b, c)
            #ループ後にまとめて更新するほうが一般的(epoch的?)
            a -= ALPHA * da
            b -= ALPHA * db
            c -= ALPHA * dc
            e_sum += func_error(func_y(x, a, b, c), func_y_hat(x))
        e_ave = e_sum / 100
        # print('{}: {}'.format(i, e_ave))
        print('{}: {:.4f}'.format(i, e_ave))
    
    # print('a = {}, b = {}, c = {}'.format(a, b, c))
    #y_hatの設定を書いた方がわかりやすい
    print('a = {:.4f}, b = {:.4f}, c = {:.4f}'.format(a, b, c))