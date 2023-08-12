from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.models import Demo, WebsiteSettings, Showcase, InnerPage, MenuStyle, Menu, Submenu, LayoutPage, \
 DropdownMenu


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demos'] = Demo.objects.all()
        context['website'] = WebsiteSettings.objects.get()
        context['layout'] = LayoutPage.objects.all()
        context['showcases'] = Showcase.objects.all()
        context['innerPages'] = InnerPage.objects.all()
        context['menuStyles'] = MenuStyle.objects.all()
        context['menus'] = Menu.objects.filter(is_active=True)
        context['submenus'] = Submenu.objects.filter(is_active=True)
        context['dropdownMenus'] = DropdownMenu.objects.filter(is_active=True)

        return context


class ContactView(View):
    def post(self, request):
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data has been successfully saved")
        else:
            messages.error(request, "Invalid data! please try again.")
        return redirect('/')


class PortfolioView(View):
    def get(self, request):
        return render(request, 'simple-portfolio.html')


class MainHomeView(View):
    def get(self, request):
        return render(request, 'main-home.html')


class CreativeAgencyView(View):
    def get(self, request):
        return render(request, 'creative-agency.html')


class DigitalAgencyView(View):
        def get(self, request):
            return render(request, 'digital-agency.html')


class FreelancerPortfolioView(View):
    def get(self, request):
        return render(request, 'freelancer-portfolio.html')


class FullscreenSliderView(View):
    def get(self, request):
        return render(request, 'fullscreen-showcase.html')


class CarousalDarkView(View):
    def get(self, request):
        return render(request, 'carousel-dark.html')


class CarousalLightView(View):
    def get(self, request):
        return render(request, 'carousel-light.html')


class InteractiveLightView(View):
    def get(self, request):
        return render(request, 'interactive-links-light.html')


class InteractiveDarkView(View):
    def get(self, request):
        return render(request, 'interactive-links-dark.html')


class LeftMenuView(View):
    def get(self, request):
        return render(request, 'left-menu.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about-us.html')


class AboutUsV2View(View):
    def get(self, request):
        return render(request, 'about-us-2.html')


class AboutMeView(View):
    def get(self, request):
        return render(request, 'about-me.html')


class ServiceView(View):
    def get(self, request):
        return render(request, 'services.html')


class SingleServiceView(View):
    def get(self, request):
        return render(request, 'single-service.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact-1.html')


class ContactUsV2View(View):
    def get(self, request):
        return render(request, 'contact-2.html')


class ForeZeroForeView(View):
    def get(self, request):
        return render(request, '404.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'blog-col-3.html')


class BlogV2View(View):
    def get(self, request):
        return render(request, 'blog-col-1.html')


class SinglePostView(View):
    def get(self, request):
        return render(request, 'single-post.html')


class ComingSoonView(View):
    def get(self, request):
        return render(request, 'coming-soon.html')


class PortfolioSingleStyle1View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-1.html')


class PortfolioSingleStyle2View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-2.html')


class PortfolioSingleStyle3View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-3.html')


class PortfolioSingleStyle4View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-4.html')


class PortfolioSingleStyle5View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-5.html')


class PortfolioSingleStyle6View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-6.html')


class PortfolioSingleStyle6View(View):
    def get(self, request):
        return render(request, 'portfolio-single-style-6.html')

