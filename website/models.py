from django.db import models

# Create your models here.


class Demo(models.Model):
    title = models.CharField(max_length=50)
    file_path = models.CharField(max_length=50)
    image = models.ImageField(upload_to='demos/')

    def __str__(self):
        return self.title


class WebsiteSettings(models.Model):
    main_title = models.CharField(max_length=50)
    main_subtitle = models.TextField()
    button_text = models.CharField(max_length=50)
    site_name = models.CharField(max_length=100)
    innerPage_title = models.CharField(max_length=100, null=True, blank=True)
    innerPage_Subtitle = models.TextField(null=True, blank=True)
    device_support_title = models.CharField(max_length=100, null=True, blank=True)
    device_support_subtitle = models.CharField(max_length=200, null=True, blank=True,)
    device_support_image = models.ImageField(upload_to='devices/', null=True, blank=True)

    def __str__(self):
        return self.site_name


class Showcase(models.Model):
    image = models.ImageField(upload_to='showcase/')
    file_path = models.CharField(max_length=50)


class InnerPage(models.Model):
    image = models.ImageField(upload_to='innerPages/')
    page_type = models.CharField(max_length=50, null=True, default=True)
    file_path = models.CharField(max_length=50)


class MenuStyle(models.Model):
    image = models.ImageField(upload_to='menuStyles/')
    menu_type = models.CharField(max_length=50)
    file_path = models.CharField(max_length=50)



class Contact1(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50)
    budget = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    type = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    file_path = models.CharField(max_length=50)

    def __str__(self):

        return self.type


class Submenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    is_active = models.BooleanField(True)
    file_path = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class DropdownMenu(models.Model):
    submenu = models.ForeignKey(Submenu, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    is_active = models.BooleanField(True)
    file_path = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class LayoutPage(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='layImage1/')
    image2 = models.ImageField(upload_to='layImage2/')
    button_text = models.CharField(max_length=10)
    file_path = models.CharField(max_length=50)


