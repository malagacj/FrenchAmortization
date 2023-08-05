from finance.tools import capitalization_ratio, french_amortization_fee


def test_capitalization_ratio():
    """ Checks valid returned values for capitalization_ratio function """

    assert capitalization_ratio(1, 1) == 0.5
    assert capitalization_ratio(3, 1) == 0.25
    assert capitalization_ratio(4, 1) == 0.2
    assert capitalization_ratio(7, 1) == 0.125
    assert capitalization_ratio(9, 1) == 0.1
    assert capitalization_ratio(3, 2) == 0.0625
    assert capitalization_ratio(4, 2) == 0.04
    assert capitalization_ratio(4, 3) == 0.008
    assert capitalization_ratio(9, 3) == 0.001
    assert capitalization_ratio(1, 4) == 0.0625
    assert capitalization_ratio(4, 4) == 0.0016


def test_french_amortization_fee():
    """ Checks valid returned values for french_amortization_fee function

        Note: Returned values need to be rounded. This is acceptable behaviour
        from any programming language
    """

    assert round(french_amortization_fee(1_000_000, 1, 1)) == 2_000_000
    assert round(french_amortization_fee(1_000_000, 0.01, 1)) == 1_010_000
