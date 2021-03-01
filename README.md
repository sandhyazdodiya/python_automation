PyTest is a testing framework that allows users to write test codes using Python programming language.

To install Pytest:
pip install pytest

To check Version :
pytest --version

Naming Convetion:
Pytest File names should start with test_ or end with _test
Pytest Method names should start with test

To run Pytest TestCases:

To run all TestCases from a package:
py.test or pytest 
 
To get more INFO about TesCase:
pytest -v (verbose flag)

To print console logs in output
pytest -s 

To run specific file
pytest <file_name> -v -s  
pytest test_simple2.py -v -s

To selected TestCases from multiple files (Group)
pytest -k CreditCard -v -s

To run marked TestCases (Tag, Group)
pytest -m smoke -v -s


To skip TestCase :
Mark it with skip (bulit in mark, unconditional skip)
@pytest.mark.skip


To run test and skip reporting 
@pytest.mark.xfail


To define fixture
@pytest.fixture()


Define common fixture in conftest.py

To generate xml report
--junitxml=file_name
--junitxml=xml_report






