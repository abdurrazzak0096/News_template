from django.contrib import admin

from website.models import Demo, WebsiteSettings, Showcase, InnerPage, MenuStyle, Menu, Submenu, LayoutPage, \
    Dropdownmenu, Contact1, Contact2

# Register your models here.
admin.site.register(Demo)
admin.site.register(WebsiteSettings)
admin.site.register(Showcase)
admin.site.register(InnerPage)
admin.site.register(MenuStyle)
admin.site.register(Menu)
admin.site.register(Submenu)
admin.site.register(Dropdownmenu)
admin.site.register(LayoutPage)
admin.site.register(Contact1)
admin.site.register(Contact2)


