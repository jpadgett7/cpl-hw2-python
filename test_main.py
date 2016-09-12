# Import pytest, so that we can use xfail.
# You should remove this if you find you no longer need pytest.
# flake8 will remind you.
import pytest
import math

# Import all of our testable functions from main.
from main import press_button, which_to_press, dial_to, should_flip


def test_press_button():
    """Test that we'll know when to press the Button Layer button

    Tests press_button function.
    """
    testVals = (17, 85, 39)
    testOuts = (1,1,0)
    for i in range(3):
        assert press_button(testVals[i]) == testOuts[i]


def test_which_to_press():
    """Test that we'll know how to respond to the History Layer

    Tests which_to_press function.
    """
    testHist1 = [(1,4),(3,1),(2,4),(4,3)]
    testHist2 = [(1,4),(4,4),(2,4)]
    testDisp = (1,2,3,4)
    expPress1 = 4 #4 should always be pressed with the first test history
    expPress2 = (4,4,2,4) #expected values for second test history
    for val in testDisp:
        assert which_to_press(testHist1, val) == expPress1
        assert which_to_press(testHist2, val) == expPress2[val-1]


def test_dial_to():
    """Test that we'll know how to respond to the Code Layer

    Tests dial_to function.
    """
    testBag = {'serial number': 'XX7e3652'}
    testCode1 = 'circuit'
    testCode2 = 'elephant'
    assert dial_to(testBag, testCode1) == 'c'
    assert dial_to(testBag, testCode2) == 'a'


def test_should_flip():
    """Test that we'll know how to respond to the Switches Layer

    Tests should_flip function.
    """
    pytest.xfail("Test is not implemented yet.")
