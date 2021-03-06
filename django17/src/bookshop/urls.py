"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin


from about import views as about_views
from contact import views as contact_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', about_views.home, name='home'),
    url(r'^books/', include('shop.urls', namespace='shop')),
    
    url(r'^post/$',contact_views.contact1, name='contact' ),
    url(r'^contact/$',contact_views.contact, name='contactnew' ),

    url(r'^about/$',about_views.about, name='about' ),
    url(r'^information/create/$', contact_views.infosubmit, name='infoo'),

]



if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)