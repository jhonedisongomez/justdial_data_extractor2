# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

class CrawlerView():

    template_name = ""
    login_url = "/"

    def get(self, request, *args, **kwargs):

        print('hello')

    def post(self, request, *args, **kwargs):

        print('hello')
    
