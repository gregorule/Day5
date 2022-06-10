from unit_testing import factorial

def fact():
    assert factorial.fact(0) == 1
    assert factorial.fact(1) == 0
    assert factorial.fact(2) == 2
    