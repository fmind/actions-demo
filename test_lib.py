import lib


def test_good_inc():
    # given
    x = 3
    # when
    res = lib.inc(x)
    # then
    assert res == 4

def test_bad_inc():
    # given
    x = 3
    # when
    res = lib.inc(x)
    # then
    assert res == 5