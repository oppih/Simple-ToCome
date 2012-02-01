#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', db='tocome', user='root', pw='')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='letwego28@gmail.com',
    site_name = '聚餐签到表',
    site_desc = '',
    static = '/static',
    party_time = '2012.2.1 正月初十',
    party_place = '就在这里',
    party_people = '**** ****届 **班',
    party_affair = '吃、喝、聊',
    party_notes = '点击签到后，如果也带现金来的，请拉到最下方再做一次点击 || 为保证数据正确，完成后就不要乱点了',
    party_notes_more = '（人数统计在最下方）',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
