from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import SiteSettings


class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    # Get the only instance by default, instead of having a list of one element
    def changelist_view(self, request, extra_context=None):
        obj = self.model.objects.all()[0]
        return HttpResponseRedirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)))

admin.site.register(SiteSettings, SettingsAdmin)