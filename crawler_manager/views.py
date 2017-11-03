# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages

class CrawlerView1(LoginRequiredMixin,TemplateView):

    template_name = "crawler_manager/crawler_page1.html"
    login_url = "/"
    class_form = ""

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        print('hello')

class CrawlerView2(LoginRequiredMixin,TemplateView):

    template_name = "crawler_manager/crawler_page2.html"
    login_url = "/"
    class_form = ""

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        print('hello')
    
class HomeView(TemplateView):

    template_name = "home.html"
    class_form = ""

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, self.template_name)

        else:
            messages.warning(request, 'Username or password incorrect.')
            return redirect('/')

