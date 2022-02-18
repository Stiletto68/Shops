from django.contrib import admin
from shops.models import Organization, Shop, ShopInlineAdminView


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'address', 'index', 'is_deleted']
    list_filter = ['name']
    list_display_links = ['name']
    ordering = ['id']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    list_display_links = ['name']
    ordering = ['id']
    inlines = [ShopInlineAdminView]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Shop, ShopAdmin)
