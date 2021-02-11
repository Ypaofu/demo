def setup_module():
    print("模块级别的 setup")

def teardown_module():
    print("模块级别的 tesrdown")


def setup_function():
    print("函数级别的 setup")

def teardown_function():
    print("函数级别的 tesrdown")

def test_func1():
    print("测试函数1")


class TestDemo:

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 tesrdown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 tesrdown")


    def test_demo(self):
        print("test_demo")

    def test_demo1(self):
        print("test_demo1")

class TestDemo1:

    def setup_class(self):
        print("类级别的 setup")

    def teardown_class(self):
        print("类级别的 tesrdown")

    def setup(self):
        print("方法级别的 setup")

    def teardown(self):
        print("方法级别的 tesrdown")


    def test_demo(self):
        print("test_demo")

    def test_demo1(self):
        print("test_demo1")