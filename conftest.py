import pytest

@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


# Run fixture for once before class and after all test case excecuted in class

@pytest.fixture(scope='class')
def class_setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def data_load():
    print("User Profile data is being created")
    return ["Sandhya", "Dodiya", "sandhya@gmail.com"]


# Run fixture multiple times [for each param index data]
# Fixture parameterization
# @pytest.fixture(params= ["chrome", "firefox", "Internet Explorer"])

@pytest.fixture(params= [("chrome", "sandhya"), ("firefox", "dodiya"),"Internet Explorer"])

def cross_browser(request):
    return request.param