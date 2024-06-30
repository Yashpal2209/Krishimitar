"""
URL configuration for krishimitar project.

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
from django.contrib import admin
from django.urls import path
from krishimitar import view
from django.conf import settings
from django.conf.urls.static import static
# import Bima

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",view.home,name="home"),
    path("login/",view.signin,name="signin"),
    path("signup/",view.signup,name="signup"),
    path("sell/",view.sell,name="sell"),
    path("buy/",view.buy,name="buy"),
    path("bima/",view.bima,name="bima"),
    path("signout/",view.signout,name="signout"),
    path("savesell/",view.saveSell,name="saveSell"),
    path("savebima/",view.saveBima,name="saveBima"),
    path("chat/",view.chatting,name="chat"),
    path("buysell/",view.buysell,name="buysell"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
