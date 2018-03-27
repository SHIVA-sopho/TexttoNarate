#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:23:00 2018

@author: satyam
"""
from django import forms

from .models import Content

class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ('title','text',)
