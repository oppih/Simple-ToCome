#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='sqlite3', db='tocome')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='letwego28@gmail.com',
    site_name = '参与人员跟踪',
    site_desc = '',
    static = '/static',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
