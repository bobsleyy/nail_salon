"""
URL configuration for nail_salon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from nail_salon_app.views import (HomepageView, AllVisitsView, GalleryView, GalleryAddView, LoginView, RegistrationView,
                                  VisitDetailsView, VisitRegistrationView, VisitsListView, LogoutView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
    path('all_visits/', AllVisitsView.as_view(), name='all_visits'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('gallery_add/', GalleryAddView.as_view(), name='gallery_add'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('visit_details/<int:id>', VisitDetailsView.as_view(), name='visit_details'),
    path('visit_registration/', VisitRegistrationView.as_view(), name='visit_registration'),
    path('visits_list/', VisitsListView.as_view(), name='visits_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
