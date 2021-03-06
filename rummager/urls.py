"""rummager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rummagerapi.views.dumpster import DumpsterView
from rummagerapi.views.item import ItemView
from rummagerapi.views.haul import HaulView
from rummagerapi.views.auth import login_user, register_user
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework import routers
from rummagerapi.views.tag import TagView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', TagView, 'tag')
router.register(r'hauls', HaulView, 'haul')
router.register(r'items', ItemView, 'item')
router.register(r'dumpsters', DumpsterView, 'dumpster')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

# This will be used for image upload setup later.
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                             document_root=settings.MEDIA_ROOT)


