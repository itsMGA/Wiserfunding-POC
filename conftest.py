import pytest
from simple_settings import LazySettings

def pytest_addoption(parser):
    parser.addoption('--environment', action='store')


@pytest.fixture()
def environmentConfigs(request):
    return LazySettings("environmentConfigs." + request.config.getoption("--environment"))

@pytest.fixture()
def testData(request):
    return LazySettings("TestData." + request.config.getoption("--environment") + "TestData")

