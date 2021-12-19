import time
#

def multiplyList(myList):
    try:
        result = 1
        for x in myList:
            result = result * x
        return result
    except:
        return 'Ошибка!'


def sumList(myList):
    result = 0

    for x in myList:
        result = result + x

    return result


def largest(arr):
    max_ = arr [0]
    for ele in arr:
        if ele > max_:
            max_ = ele
    return max_


def smaller(arr):
    min_ = arr [0]
    for ele in arr:
        if ele < min_:
            min_ = ele
    return min_


start_time = time.time()
f = open('input.txt', 'r')
nums = list(map(int, f.read().split()))
f.close()
print(nums)
print(f'Минимальное: {smaller(nums)}')
print(f'Максимальное: {largest(nums)}')
print(f'Сумма: {sumList(nums)}')
print(f'Произведение: {multiplyList(nums)}')
res_time_test = time.time() - start_time
print("--- %s seconds ---" % (res_time_test))

start_time = time.time()
f = open('input2.txt', 'r')
nums = list(map(int, f.read().split()))
f.close()
print(nums)
print(f'Минимальное: {smaller(nums)}')
print(f'Максимальное: {largest(nums)}')
print(f'Сумма: {sumList(nums)}')
print(f'Произведение: {multiplyList(nums)}')
res_time_test2 = time.time() - start_time
print("--- %s seconds ---" % (res_time_test2))

print(f'Со вторым файлом большего размера программа работает медленнее на {res_time_test2 - res_time_test}')
