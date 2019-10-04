"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url

from main.views import home_view, upload_view, time_view, mail_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url('home/', home_view),
    url('upload/', upload_view),
    url('time/', time_view, name="time"),
    url('mail/', mail_view, name="mail"),
]

#urlpatterns = [
#    url('', views.homepageview, name='home')
#]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
