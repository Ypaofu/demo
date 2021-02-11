import pytest

@pytest.fixture(params=[1, 2, 3])
def login(request):
    #print(request.param)
    data = request.param
    print("获取测试数据")
    return data

def test_case1(login):
    print(login)
    print("测试用例1")