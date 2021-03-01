import pytest

# def test_first_program():
#     msg = "Hello"
#     assert msg == "Hi", "Test Failed, Strings do not match"


# def test_second_program():
#     a = 4
#     b = 2
#     assert a+b == 6, "Addition do not match."


# def test_CreditCard2():
#     print("Credit Card 2")



# @pytest.mark.smoke
# def test_marked_case():
#     print("Marked Test Case")



# def test_setup(setup):
#     print("Testcase with fixture")




# Fixture will run before and after each method defined in class

# @pytest.mark.usefixtures('setup')
# class TestSimple:
#     def test_first_program(self):
#         msg = "Hello"
#         assert msg == "Hi", "Test Failed, Strings do not match"


#     def test_second_program(self):
#         a = 4
#         b = 2
#         assert a+b == 6, "Addition do not match."


#     def test_CreditCard2(self):
#         print("Credit Card 2")




# @pytest.mark.usefixtures('class_setup')
# class TestSimple:
#     def test_first_program(self):
#         msg = "Hello"
#         assert msg == "Hi", "Test Failed, Strings do not match"


#     def test_second_program(self):
#         a = 4
#         b = 2
#         assert a+b == 6, "Addition do not match."


#     def test_CreditCard2(self):
#         print("Credit Card 2")


def test_cross_browser(cross_browser):
    print(cross_browser)


