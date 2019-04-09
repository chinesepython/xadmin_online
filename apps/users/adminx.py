# -*- coding: utf-8 -*-
__author__ = 'xyh'
__date__ = '2019/4/8 14:30'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    # 页面主题切换配置
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    # 页面页头页脚配置和左侧菜单列表显示
    site_title = "xyh后台管理系统"
    site_footer = "xyh后台管理网站"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 定义后台进入该表时显示哪些字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 定义可以通过哪些字段搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤器 任意字段 条件过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
