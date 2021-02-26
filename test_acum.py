import pytest
from stff.acum import Accumulator

def test_acummulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1