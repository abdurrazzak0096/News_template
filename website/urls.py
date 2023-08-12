from django.urls import path
from . import views


urlpatterns = [

          path('', views.HomeView.as_view()),
          path('simple-portfolio/', views.PortfolioView.as_view(), name='simple-portfolio'),
          path('main-home/', views.MainHomeView.as_view(), name='main-home'),
          path('creative-agency/', views.CreativeAgencyView.as_view(), name='creative-agency'),
          path('digital-agency/', views.DigitalAgencyView.as_view(), name='digital-agency'),
          path('carousel-light/', views.CarousalLightView.as_view(), name='carousel-light'),
          path('carousel-dark/', views.CarousalDarkView.as_view(), name='carousel-dark'),
          path('interactive-links-light/', views.InteractiveLightView.as_view(), name='interactive-links-light'),
          path('interactive-links-dark/', views.InteractiveDarkView.as_view(), name='interactive-links-dark'),
          path('freelancer-portfolio/', views.FreelancerPortfolioView.as_view(), name='freelancer-portfolio'),
          path('fullscreen-showcase/', views.FullscreenSliderView.as_view(), name='fullscreen-showcase'),
          path('left-menu/', views.LeftMenuView.as_view(), name='left-menu'),
          path('about-us/', views.AboutUsView.as_view(), name='about-us'),
          path('about-us-2/', views.AboutUsV2View.as_view(), name='about-us-2'),
          path('about-me/', views.AboutMeView.as_view(), name='about-me'),
          path('404/', views.ForeZeroForeView.as_view(), name='404'),
          path('services/', views.ServiceView.as_view(), name='services'),
          path('single-service/', views.SingleServiceView.as_view(), name='single-service'),
          path('contact-1/', views.ContactUsView.as_view(), name='contact-1'),
          path('contact-2/', views.ContactUsV2View.as_view(), name='contact-2'),
          path('blog-col-3/', views.BlogView.as_view(), name='blog-col-3'),
          path('blog-col-1/', views.BlogV2View.as_view(), name='blog-col-1'),
          path('single-post/', views.SinglePostView.as_view(), name='single-post'),
          path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
          path('portfolio-single-style-1/', views.PortfolioSingleStyle1View.as_view(), name='portfolio-single-style-1'),
path('portfolio-single-style-2/', views.PortfolioSingleStyle2View.as_view(), name='portfolio-single-style-2'),
path('portfolio-single-style-3/', views.PortfolioSingleStyle3View.as_view(), name='portfolio-single-style-3'),
path('portfolio-single-style-4/', views.PortfolioSingleStyle4View.as_view(), name='portfolio-single-style-4'),
path('portfolio-single-style-5/', views.PortfolioSingleStyle5View.as_view(), name='portfolio-single-style-5'),
path('portfolio-single-style-6/', views.PortfolioSingleStyle6View.as_view(), name='portfolio-single-style-6'),


 ]