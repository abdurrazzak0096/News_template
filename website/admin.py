from django.contrib import admin

from website.models import Demo, WebsiteSettings, Showcase, InnerPage, MenuStyle, Menu, Submenu, LayoutPage, \
    DropdownMenu

# Register your models here.
admin.site.register(Demo)
admin.site.register(WebsiteSettings)
admin.site.register(Showcase)
admin.site.register(InnerPage)
admin.site.register(MenuStyle)
admin.site.register(Menu)
admin.site.register(Submenu)
admin.site.register(DropdownMenu)
admin.site.register(LayoutPage)

