#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', db='todo', user='root', pw='')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='letwego28@gmail.com',
    site_name = '聚餐签到表',
    site_desc = '',
    static = '/static',
    party_time = '2012.2.1 正月初十',
    party_place = '就在这里',
    party_people = '象山中学2008届 高三5班',
    party_affair = '吃、喝、聊',
    party_notes = '请带现金过来的同学再下面选择修改，注上金额',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
