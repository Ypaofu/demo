import pytest

#前后调用一次
@pytest.fixture(scope="module")
#同事调用多个文件
@pytest.fixture(scope="session")
def connectDB():
    print("链接数据库")
    yield
    print("断开数据库")