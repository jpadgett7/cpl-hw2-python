# Import pytest, so that we can use xfail.
# You should remove this if you find you no longer need pytest.
# flake8 will remind you.
import pytest

# Import all of our testable functions from main.
from main import press_button, which_to_press, dial_to, should_flip


def test_press_button():
    """Test that we'll know when to press the Button Layer button

    Tests press_button function.
    """
    pytest.xfail("Test is not implemented yet.")


def test_which_to_press():
    """Test that we'll know how to respond to the History Layer

    Tests which_to_press function.
    """
    pytest.xfail("Test is not implemented yet.")


def test_dial_to():
    """Test that we'll know how to respond to the Code Layer

    Tests dial_to function.
    """
    pytest.xfail("Test is not implemented yet.")


def test_should_flip():
    """Test that we'll know how to respond to the Switches Layer

    Tests should_flip function.
    """
    pytest.xfail("Test is not implemented yet.")
