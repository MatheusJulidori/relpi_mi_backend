from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('router/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('relpi_miAPP.urls'), name='app'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
]
