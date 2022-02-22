# _*_ coding: utf-8 _*_
# @Time : 2022/1/2 15:05 
# @Author : YU RUI
# @File : shopping_tb.py
# @desc :
"""
    这是购物流程，包含了搜索产品，添加产品到购物车，以及处理了中间可能跳出的需要登录的页面
"""
import os
from time import sleep

from selenium import webdriver

from pytest_homework.logic.login_tb import Login
from pytest_homework.page import allPage


class GoodsSale(Login):
    def shopping(self):
        # 打开淘宝
        self.open('https://www.taobao.com')
        # 输入要搜索的产品名称
        self.locator_list(allPage.page_index_search).send_keys('膳魔师')
        # 点击搜索按钮
        self.locator_list(allPage.page_index_searchBtn).click()
        # 面对可能出现的登录界面进行处理
        try:
            self.login()
        except Exception:
            pass
        # 点击搜索页的第一个元素
        self.locator_list(allPage.page_searchResults_good).click()

        # 切换句柄
        self.change_window(1)

        try:
            self.locator_list(allPage.page_goodsDetail_version).click()
        except Exception as e:
            print(e)
        # 选择颜色,数量
        self.locator_list(allPage.page_goodsDetail_color).click()
        self.wait(1)
        self.locator_list(allPage.page_goodsDetail_num).clear()
        self.wait(1)
        self.locator_list(allPage.page_goodsDetail_num).send_keys(2)
        # 点击加入购物车
        self.wait(1)
        self.locator_list(allPage.page_goodsDetail_cartBtn).click()

        # 可能会再次出现登录页面，所以需要再次处理登录
        elems = self.locator_list_group(allPage.page_goodsDetail_loginFrame)
        try:
            el = elems[0]
            self.change_frame(el)
            self.login()
            self.change_defaultFrame()
            sleep(2)
        except Exception:
            pass
        # 返回页面中特定的元素，方便后续用例断言
        return self.get_text(allPage.page_goodsDetail_assert[1])

    # def addSimilarGood(self):



if __name__ == '__main__':
    os.popen(r"E:\chrome\chrome.bat")
    sleep(3)
    print("成功打开浏览器")
    # 复用已有浏览器，方便调试
    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    # 隐式等待10秒
    driver.implicitly_wait(10)
    # 用例执行，返回driver
    gs = GoodsSale(driver)
    gs.shopping()
    # os.system('taskkill /im chromedriver.exe /F')
    # os.system('taskkill /im chrome.exe /F')
    # print("test end!")
