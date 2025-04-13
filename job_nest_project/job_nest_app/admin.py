from django.contrib import admin
from job_nest_app.models import GeneralInfo, UserMadePost

# Register your models here.
@admin.register(GeneralInfo)#this means import the table in admin site
class GeneralInfoAdmin(admin.ModelAdmin):
    #tihs class registers the table to admin site.
    list_display=[
        "company_name",
        "company_location",
    ]
    search_fields=[
        "company_name",
        "company_location",
    ]

@admin.register(UserMadePost)#this means import the table in admin site
class UserMadePostAdmin(admin.ModelAdmin):
    #tihs class registers the table to admin site.
    list_display=[
        "title"

    ]
    search_fields=[
        "title",
    ]
