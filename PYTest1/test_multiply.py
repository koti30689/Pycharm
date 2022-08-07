import pytest
@pytest.fixture
def value():
   input = 39
   return input
@pytest.mark.deepak1
def test_by_2(value):
   assert value % 2 == 0
def test_by_4(value):
   assert value % 4 == 0
def test_by_6(value):
   assert value % 6 == 0
def test_by_8(value):
   assert value % 8 == 0
def test_by_10(value):
   assert value % 10 == 0
