from django.forms import ModelForm
from website.models import Contact1


class ContactForm(ModelForm):
    class Meta:
        model = Contact1
        fields = '__all__'



