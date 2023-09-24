from django.forms import ModelForm
from website.models import Contact1, Contact2


class Contact1Form(ModelForm):
    class Meta:
        model = Contact1
        fields = ('name', 'email', 'phone', 'company', 'title', 'message')


class Contact2Form(ModelForm):
    class Meta:
        model = Contact2
        fields = ('name', 'email', 'phone', 'company', 'title', 'message')



