from unit_testing import factorial

def test_fact():
    assert factorial.fact(0) == 1
    assert factorial.fact(1) == 1
    assert factorial.fact(2) == 2
    assert factorial.fact(3) == 6
    assert factorial.fact(4) == 24
