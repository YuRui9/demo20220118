# _*_ coding: utf-8 _*_
# @Time : 2022/1/2 15:06 
# @Author : YU RUI
# @File : login_tb.py
# @desc :
import base64

from pytest_homework.key_word.keyword_web import WebKeys
from pytest_homework.page import allPage

password = 'eXJ4eTE1MTEwOCE='
str_password = base64.b64decode(password).decode("utf-8")


# 这个类是用于处理中途跳出的需要登录的页面,最开始的登录已经通过本地登录淘宝处理了，所以直接就进入了淘宝首页
class Login(WebKeys):
    def login(self):
        self.locator_list(allPage.page_goodsDetail_loginUser).send_keys("切你又不来")
        self.locator_list(allPage.page_goodsDetail_loginPwd).send_keys(str_password)
        self.locator_list(allPage.page_goodsDetail_loginBtn).click()
