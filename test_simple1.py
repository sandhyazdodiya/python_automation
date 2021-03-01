import pytest

def test_first_program():
    print("Hello First")

def test_second_program():
    print("Hello Second")


def test_CreditCard1():
    print("Credit Card 1")

# Mark TestCase with some Tag (ex: smoke)
# @pytest.mark.smoke

@pytest.mark.smoke
def test_marked_case():
    print("Marked Test Case")



@pytest.mark.skip
def test_skip_case():
    print("Skipped Test Case")

# Run test case but do not report ( Because Other Testcases are dependent on this)
# @pytest.mark.xfail
@pytest.mark.xfail
def test_skip_case():
    print("xfail Test Case")


# Fixture

# @pytest.fixture()
# def setup():
#     print("I will be executed first")
#     yield
#     print("I will be executed last")


def test_setup(setup):
    print("Testcase with fixture")