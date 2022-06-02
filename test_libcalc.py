import libcalc


class TestCalculator:

    def test_addition(self):
        assert 4 == libcalc.add(2, 2)

    def test_subtraction(self):
        assert 2 == libcalc.subtract(4, 2)

    def test_multiplication(self):
        assert 8 == libcalc.multiply(4, 2)
