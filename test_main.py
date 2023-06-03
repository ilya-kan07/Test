from main import square_eq_solver


def test_no_root():
    """Случай, когда уравнение не имеет корней"""
    res = square_eq_solver(10, 0, 2)
    assert len(res) == 0


def test_single_root():
    """Случай, когда уравнение имеет один корень"""
    res = square_eq_solver(10, 0, 0)
    assert len(res) == 1
    assert res == [0]


def test_multiple_root():
    """Случай, когда уравнеение имеет два корня"""
    res = square_eq_solver(2, 5, -3)
    assert len(res) == 2
    assert res == [0.5, -3]
