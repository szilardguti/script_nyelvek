from szamjegy_osszeg import szamjegy_calc


def test_szamjegy_calc():
    assert szamjegy_calc(2**15) == 26
    assert szamjegy_calc(2**1000) == 1366
    assert szamjegy_calc(123456789) == 45
    assert szamjegy_calc(-123) == 6
    assert szamjegy_calc(6*6) == 9
    assert szamjegy_calc(0) == 0
