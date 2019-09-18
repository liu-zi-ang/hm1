import  allure


class Test_001():
    @allure.step(title="登录操作")
    def test_001(self):
        allure.attach("用户名","内容")
        assert True