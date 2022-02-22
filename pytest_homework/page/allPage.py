# _*_ coding: utf-8 _*_
# @Time : 2022/1/2 14:59 
# @Author : YU RUI
# @File : allPage.py
# @desc :


# 登录账号页


"""
淘宝首页
www.taobao.com
page_index
"""
# 搜索输入框
page_index_search = ["xpath", '//div[@class="search-combobox"]/div/input']
# 搜索按钮
page_index_searchBtn = ["xpath", "//div[@class='search-button']"]

"""
搜索结果页
https://s.taobao.com/search
page_searchResults
"""
# 结果页搜到的第一个商品
page_searchResults_good = ["xpath", "//div[@class='items']/div[@data-index='0']"]

"""
商品详情页
https://item.taobao.com/item.htm
page_goodsDetail
"""
# 版本  每次搜索出的膳魔师产品第一个都有可能不一样 这个元素不一定有
# //ul[@class='tm-relate-current']/li
page_goodsDetail_version = ["xpath", "//ul[@class='tm-relate-list']/li"]

# 颜色分类
page_goodsDetail_color = ["xpath", "//ul[@data-property='颜色分类']/li"]
# 商品数量
page_goodsDetail_num = ["id", "J_IptAmount"]
# 加入购物车
page_goodsDetail_cartBtn = ["partial link text", "加入购物"]
# 可能会跳出登录框，提示登录，
# 登陆frame框
page_goodsDetail_loginFrame = ["xpath", "//iframe[@class]"]
# 会员名输入框
page_goodsDetail_loginUser = ["id", "fm-login-id"]
# 密码
page_goodsDetail_loginPwd = ["id", "fm-login-password"]
# 登陆按钮
page_goodsDetail_loginBtn = ["xpath", "//div[@class='fm-btn']"]
# 加入购物车后的去购物结算按钮
page_goodsDetail_payBtn = ["partial link text", "去购物车结算"]
# 断言添加购物车是否成功
page_goodsDetail_assert = ["xpath", "//div[@class='result-hint']"]

# 购物车详情页
