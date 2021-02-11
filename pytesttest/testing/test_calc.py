import allure
import pytest

from python_clos.calk import Calculator

# with open("./datas/calc.yaml") as f:
#     add datas = yaml.safe_load(f)['add']

def test_a():
    print("测试用例a")


@allure.feature("测试计算器")
class TestCalc:

    def setup_class(self):
        print("开始计算")
        # 实例化计算机
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        [
            (1, 1, 2),
            (0.1, 0.1, 0.2),
            (-1, -1, -2),
            (0.1, 0.2, 0.3)
        ], ids=['int', 'float', 'negative', 'round']
    )

    @allure.story("测试加法")
    def test_add(self, a, b, expect):
        #实例化计算机
        #calc = Calculator()
        #调用 add 方法
        with allure.step("计算两个数的相加和"):
        result = self.calc.add(a, b)
        #判断 result 是浮点数， 作出保留2为小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        #得到结果之后，判断结果是否正确
        assert result == expect

    # def test_add1(self):
    #     # 实例化计算机
    #     #calc = Calculator()
    #     # 调用 add 方法
    #     result = self.calc.add(0.1, 0.1)
    #     # 得到结果之后，判断结果是否正确
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # 实例化计算机
    #     #calc = Calculator()
    #     # 调用 add 方法
    #     result = self.calc.add(-1, -1)
    #     # 得到结果之后，判断结果是否正确
    #     assert result == -2




