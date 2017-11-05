# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CrawelIssue
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

class CrawelIssuekResource(resources.ModelResource):
    
    class Meta:
        model = CrawelIssue
        skip_unchanged = True
        report_skipped = False
        # fields = ('id', 'name', 'price',)
        exclude = ('user', )

class CrawelIssueAdmin(ImportExportActionModelAdmin,ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CrawelIssuekResource
    list_display = ('user', 'keyword', 'city_name', 'instance_index', 'title', 'rating', 'votes', 'contact1','contact2','contact3','contact4','contact5', 'address', 'website', 'others_sites')
    list_filter = ('city_name', 'keyword', 'rating')
    search_fields = ('user', 'keyword', 'city_name', 'instance_index', 'title', 'rating', 'votes', 'contact1','contact2','contact3','contact4','contact5', 'address', 'website', 'others_sites')
    list_per_page = 10
admin.site.register(CrawelIssue,CrawelIssueAdmin )