import pytest



@pytest.mark.regression
def test_1():
    print("Execution TEST 1")

def test_2():
    print("Execution TEST 2")

@pytest.mark.performance
def test_3():
        print("Execution TEST 3")


def test_4():
    print("Execution TEST 4")

#markeur pour sauter ce test
@pytest.mark.skip
def test_5():
    print("Execution TEST 4")
