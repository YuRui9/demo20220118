# _*_ coding: utf-8 _*_
# @Time : 2022/1/2 21:36 
# @Author : YU RUI
# @File : conftest.py
# @desc :
import os
from time import sleep
import allure

import pytest
from selenium import webdriver


@pytest.fixture
def broswer():
    global driver
    os.popen(r"E:\chrome\chrome.bat")
    sleep(2)
    print("成功打开浏览器")
    # 复用已有浏览器，方便调试
    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)  # options=options
    # 隐式等待10秒
    driver.implicitly_wait(10)
    # 返回driver对象
    yield driver
    # 用例结束后
    os.system('taskkill /im chromedriver.exe /F')
    os.system('taskkill /im chrome.exe /F')
    print("test end!")


# allure 错误截图上传
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            with allure.step('用例运行失败，添加失败的截图'):
                allure.attach(driver.get_screenshot_as_png(),
                              '失败的截图',
                              allure.attachment_type.PNG)
