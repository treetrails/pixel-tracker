from django.contrib import admin
from django import forms
from . import models


class TargetForm(forms.ModelForm):
    class Meta:
        model = models.Target
        # exclude = ['redirect_uri', ]
        fields = forms.ALL_FIELDS


class TargetAdmin(admin.ModelAdmin):
    form = TargetForm
    list_display = ('id', 'email', 'redirect_uri')
    search_fields = ('id', 'email', 'redirect_uri')
    list_filter = ('email',)

    # @transaction.atomic
    # def save_model(self, request, obj, form, change):
    #     obj.redirect_uri = 'https://www.example.com'
    #     obj.save()


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('target', 'remote_addr', 'user_agent')
    search_fields = ('target__email',)
    list_filter = ('target__email',)

admin.site.register(models.Target, TargetAdmin)
admin.site.register(models.Activity, ActivityAdmin)
# admin.site.register(models.Enquiry)
