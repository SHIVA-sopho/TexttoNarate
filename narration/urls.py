#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:14:16 2018

@author: satyam
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]