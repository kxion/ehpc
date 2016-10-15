#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-09-08 18:06:32

from flask import redirect, request, url_for
from flask_login import current_user
from functools import wraps


def admin_login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.is_authenticated and current_user.permissions == 0:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.auth', next=request.url))
    return wrap


def student_login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.is_authenticated and current_user.permissions == 1:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.signin', next=request.url))
    return wrap


def teacher_login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user.is_authenticated and current_user.permissions == 2:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.auth', next=request.url))
    return wrap
