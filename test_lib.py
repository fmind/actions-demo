import lib


def test_inc():
    # given
    x = 3
    # when
    res = lib.inc(x)
    # then
    assert res == 4