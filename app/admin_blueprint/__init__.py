#! -*- coding:utf-8 -*-
# Created by F1renze on 2018/3/18 13:52
__author__ = 'F1renze'
__time__ = '2018/3/18 13:52'

from flask import Blueprint

admin_blueprint = Blueprint('admin_blueprint', __name__)

from  . import views, modelviews