from ekezet_eltav import ekezet_leszedo


def test_ekezet_leszedo():
    assert ekezet_leszedo("héló vílág!") == "helo vilag!"
    assert ekezet_leszedo("árvíztűrő tükörfúrógép") == "arvizturo tukorfurogep"
    assert ekezet_leszedo("ÁbÉcÉ") == "AbEcE"
    assert ekezet_leszedo("123-\t-őúűá----321") == "123-\t-ouua----321"
    assert ekezet_leszedo("") == ""
