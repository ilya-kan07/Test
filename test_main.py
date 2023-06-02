#import pytest
#pytest test_main.py
from main import *


"""Случай, когда уравнение не имеет корней"""
def test_no_root():
   res = square_eq_solver(10, 0, 2)
   assert len(res) == 0             # функция должна вернуть пустой список

"""Случай, когда уравнение имеет один корень"""
def test_single_root():
   res = square_eq_solver(10, 0, 0)
   assert len(res) == 1             # функция должна вернуть список с 1 элементом равным 0
   assert res == [0]

"""Случай, когда уравнеение имеет два корня"""
def test_multiple_root():
   res = square_eq_solver(2, 5, -3)
   assert len(res) == 3             # должна вернуть два элемента равные  0,5 и -3
   assert res == [0.5, -3]
