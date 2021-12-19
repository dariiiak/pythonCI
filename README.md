[![Build Status - GitHub](https://github.com/dariiiak/pythonCI/workflows/pytesting/badge.svg)](https://github.com/dariiiak/pythonCI/actions/workflows/main.yml)

# Код программы

```Python
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
```

# Код тестов
```Python
import pytest
import main

def test_multiplyList():
	mylist = [1, 9, 2]
	assert main.multiplyList(mylist) == 18

def test_sumList():
	mylist = [1, 9, 2]
	assert main.sumList(mylist) == 12

def test_largest():
	mylist = [1, 9, 2]
	assert main.largest(mylist) == 9


def test_smaller():
	mylist = [1, 9, 2]
	assert main.smaller(mylist) == 1

def test_error():
	nums = ['dd', 'dd']
	assert main.multiplyList(nums) == 'Ошибка!'
```

# Результаты тестов

================================================== 5 passed in 0.05s ==================================================
