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