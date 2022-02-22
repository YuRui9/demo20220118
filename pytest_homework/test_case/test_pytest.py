# _*_ coding: utf-8 _*_
# @Time : 2022/1/2 21:42 
# @Author : YU RUI
# @File : test_pytest.py
# @desc :
import os

import pytest

from pytest_homework.logic.shopping_tb import GoodsSale


class TestTaoBao:

    def test_01_shopping(self, broswer):
        gs = GoodsSale(broswer)
        result = gs.shopping()
        assert result == '已成功加入购物车1', '断言失败，添加到购物车失败'

    # def test_02_baidu(self):
    #     print("测试用例一")


if __name__ == '__main__':
    # ./result 用例的结果数据存放的目录
    pytest.main(['-s', 'test_pytest.py', '--alluredir', './result'])
    # ./report_allure/ allure报告的目录
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
