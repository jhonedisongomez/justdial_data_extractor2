# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import messages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from .models import CrawelIssue

class CrawlerView1(LoginRequiredMixin,TemplateView):

    template_name = "crawler_manager/crawler_page1.html"
    login_url = "/"
    class_form = ""

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        url = request.POST['url']
        user = request.user.pk

        driver = webdriver.Chrome("G:/freelance/justdial_data_extractor2/.env/selenium/webdriver/chromedriver.exe")
        driver2 = webdriver.Chrome("G:/freelance/justdial_data_extractor2/.env/selenium/webdriver/chromedriver.exe")
        driver.get(url)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 0

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            no_of_pagedowns-=1

        isContact = False
        instance_index = 0
        for i in driver.find_elements_by_class_name("cntanr"):
            try:

                rating = i.find_element_by_class_name("exrt_count").get_attribute("innerHTML")
                votes = i.find_element_by_class_name("lng_vote").get_attribute("innerHTML").strip(' \t\n\r')[0:5:1].strip()
                single_url = i.find_element_by_class_name("rating_div").get_attribute("href")
            except Exception as e:

                title = i.find_element_by_class_name("lng_cont_name").get_attribute("innerHTML")
            
            contacts = ""
            list_contacts = []
            contact1 = ""
            contact2 = ""
            contact3 = ""
            contact4 = ""
            contact5 = ""
            address = ""
            website = ""
            other_webs = ""
            keyword = ""
            city_name = ""
            driver2.get(single_url)
            elem2 = driver2.find_element_by_tag_name("body")
            elem2.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            title = elem2.find_element_by_class_name("fn").get_attribute("innerHTML")
                
            for contact in elem2.find_elements_by_class_name("leftdt"):
                indexTel = 0
                for tel in contact.find_elements_by_class_name("tel"):

                    if indexTel == 0:
                        contacts = tel.get_attribute("innerHTML")
                    else:
                        
                        contacts =  contacts + " , " + tel.get_attribute("innerHTML")
                        contacts = contacts.replace("<b>","")
                        contacts = contacts.replace("</b>","")
                    indexTel += 1
                print(contacts)
                list_contacts = contacts.split(",")

                if(len(list_contacts) >=1):

                    contact1 = list_contacts[0]

                if(len(list_contacts) >= 2):

                    contact2 = list_contacts[1]

                if(len(list_contacts) >=3):

                    contact3 = list_contacts[2]

                if(len(list_contacts) >=4):

                    contact4 = list_contacts[3]

                if(len(list_contacts) >=5):

                    contact5 = list_contacts[4]

                indexOtherWebs = 0
                for other_web in elem2.find_elements_by_class_name("lng_als_lst"):
                    if indexOtherWebs == 0:
                        other_webs = other_web.get_attribute("innerHTML")
                    else:
                        other_webs = other_webs + "," + other_web.get_attribute("innerHTML")
                    other_webs = other_webs.replace("<br>","")
                    other_webs = other_webs.replace("</br>","")
                    indexOtherWebs +=1
                address = contact.find_element_by_class_name("lng_add").get_attribute("innerHTML")
                websites = contact.find_elements_by_css_selector(".mreinfp.comp-text")
                website = ""
                for ix,get_website  in enumerate(websites):
                    if ix == 1:
                
                        website = get_website.find_element_by_tag_name("a").get_attribute("href")

            issue = CrawelIssue.objects.create(
            user = user,
            keyword = keyword, 
            city_name = city_name, 
            instance_index = instance_index, 
            title = title, 
            rating = rating, 
            votes = votes, 
            contact1 = contact1, 
            contact2 = contact2, 
            contact3 = contact3, 
            contact4 = contact4, 
            contact5 = contact5,  
            address = address, 
            website = website,
            others_sites = other_webs,
            )
           

            print ( 'No: {}, Saving data to database.'.format(instance_index))
            instance_index += 1 

        return redirect('/admin/crawler_manager/crawelissue/')
class CrawlerView2(LoginRequiredMixin,TemplateView):

    template_name = "crawler_manager/crawler_page2.html"
    login_url = "/"
    class_form = ""

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        user = request.user.pk
        keyword = "" 
        city_name = "" 
        url = request.POST['url']

        driver = webdriver.Chrome("G:/freelance/justdial_data_extractor2/.env/selenium/webdriver/chromedriver.exe")
        driver2 = webdriver.Chrome("G:/freelance/justdial_data_extractor2/.env/selenium/webdriver/chromedriver.exe")
        driver.get(url)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 1

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            no_of_pagedowns-=1

        isContact = False
        instance_index = 0
        for i in driver.find_elements_by_class_name("cntanr"):
            try:
                rating = ""
                votes = ""
                single_url = ""
                title = ""

                if 'chRating' in request.POST:

                    rating = i.find_element_by_class_name("exrt_count").get_attribute("innerHTML")
                
                if 'chVotes' in request.POST:

                    votes = i.find_element_by_class_name("lng_vote").get_attribute("innerHTML").strip(' \t\n\r')[0:5:1].strip()
                
                
                single_url = i.find_element_by_class_name("rating_div").get_attribute("href")
            except Exception as e:

                if 'chTitle' in request.POST:

                    title = i.find_element_by_class_name("lng_cont_name").get_attribute("innerHTML")
            
            contacts = ""
            list_contacts = []
            contact1 = ""
            contact2 = ""
            contact3 = ""
            contact4 = ""
            contact5 = ""
            address = ""
            website = ""
            other_webs = ""
            driver2.get(single_url)
            elem2 = driver2.find_element_by_tag_name("body")
            elem2.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            
            if 'chTitle' in request.POST:

                title = elem2.find_element_by_class_name("fn").get_attribute("innerHTML")
                

            if ('chContact1' in request.POST or 'chContact2' in request.POST or
                'chContact3' in request.POST or 'chContact4' in request.POST or 
                'chContact5' in request.POST or 'chAddress' in request.POST or
                'chOtherSites' in request.POST or 'chWebSite' in request.POST):

                for contact in elem2.find_elements_by_class_name("leftdt"):
                    
                    if('chContact1' in request.POST or 'chContact2' in request.POST or
                    'chContact3' in request.POST or 'chContact4' in request.POST or 
                    'chContact5' in request.POST ):

                        indexTel = 0
                        for tel in contact.find_elements_by_class_name("tel"):

                            if indexTel == 0:
                                contacts = tel.get_attribute("innerHTML")
                            else:
                                
                                contacts =  contacts + " , " + tel.get_attribute("innerHTML")
                                contacts = contacts.replace("<b>","")
                                contacts = contacts.replace("</b>","")

                            indexTel += 1


                        print(contacts)
                        list_contacts = contacts.split(",")
                        
                        if 'chContact1' in request.POST:

                            if(len(list_contacts) >=1):

                                contact1 = list_contacts[0]

                        if 'chContact2' in request.POST:

                            if(len(list_contacts) >= 2):

                                contact2 = list_contacts[1]
                        
                        
                        if 'chContact3' in request.POST:

                            if(len(list_contacts) >=3):

                                contact3 = list_contacts[2]
                        
                        
                        if 'chContact4' in request.POST:

                            if(len(list_contacts) >=4):

                                contact4 = list_contacts[3]
                        
                        if 'chContact5' in request.POST:

                            if(len(list_contacts) >=5):

                                contact5 = list_contacts[4]
                    

                if ('chWebSite' in request.POST or 'chOtherSites' in request.POST or 
                    'chAddress' in request.POST):

                    indexOtherWebs = 0
                    
                    if 'chOtherSites' in request.POST:

                        for other_web in elem2.find_elements_by_class_name("lng_als_lst"):
                            if indexOtherWebs == 0:
                                other_webs = other_web.get_attribute("innerHTML")
                            else:
                                other_webs = other_webs + "," + other_web.get_attribute("innerHTML")
                            other_webs = other_webs.replace("<br>","")
                            other_webs = other_webs.replace("</br>","")
                            indexOtherWebs +=1
                        

                    if 'chAddress' in request.POST:

                        address = contact.find_element_by_class_name("lng_add").get_attribute("innerHTML")
                    
                    if 'chWebSite' in request.POST:

                        websites = contact.find_elements_by_css_selector(".mreinfp.comp-text")
                        website = ""
                        for ix,get_website  in enumerate(websites):
                            if ix == 1:
                        
                                website = get_website.find_element_by_tag_name("a").get_attribute("href")

            issue = CrawelIssue.objects.create(
            user = user,
            keyword = keyword, 
            city_name = city_name, 
            # crawel_number = crawel_number, 
            instance_index = instance_index, 
            title = title, 
            rating = rating, 
            votes = votes, 
            contact1 = contact1, 
            contact2 = contact2, 
            contact3 = contact3, 
            contact4 = contact4, 
            contact5 = contact5, 
            address = address, 
            website = website,
            others_sites = other_webs,
            )

            print ( 'No: {}, Saving data to database.'.format(instance_index))
            instance_index += 1

        return redirect('/admin/crawler_manager/crawelissue/')

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

def logout(request):
    django_logout(request)
    return redirect('/')