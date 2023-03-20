import pytest
from utils import change_calc

def test_change_calc_1st_easy():
    price = 25
    enter_money = ['10', '10', '10']
    result = change_calc(price, enter_money)
    assert result == [5]

def test_change_calc_2nd_smallbills():
    price = 64.62
    enter_money = ['50', '50']
    result = change_calc(price, enter_money)
    assert result == [10, 10, 10, 5, 0.1, 0.1, 0.1, 0.05, 0.01, 0.01, 0.01]

def test_change_calc_3rd_withoutchange():
    price = 620
    enter_money = ['500', '100', '10', '10']
    result = change_calc(price, enter_money)
    assert result == 'Сдача не требуется'

def test_change_calc_4th_not_enough_money_sir():
    price = 510
    enter_money = ['500']
    with pytest.raises(ValueError):
        change_calc(price, enter_money)

    price = 10
    enter_money = []
    with pytest.raises(ValueError):
        change_calc(price, enter_money)

def test_change_calc_5th_incorrect_price():
    price = -10
    enter_money = ['500']
    with pytest.raises(ValueError):
        change_calc(price, enter_money)


