import allure
import pytest

@allure.feature("测试计算器")
@pytest.fixture(autouse=True)
def login():
    print('登录操作')
    print('获取 token')
    username = 'tom'
    password = "123456789"
    token = "token159852"
    #
    yield [username, password, token]
    print("注销操作")

#测试用例1：需要提前登录
#在测试用例中传入 fixture 方法名
def test_case1(login):

    print(f"用户信息为:{login}")
    print('测试用例1')
@allure.story("测试加法")
def test_case2():
    print('测试用例2')

#测试用例3：需要提前登录
def test_case3(login):
    print('测试用例3')

@pytest.mark.usefixtures("login")
def test_case4():
    print('测试用例4')