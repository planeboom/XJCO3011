from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BeverageViewSet

router = DefaultRouter()
router.register(r'beverages', BeverageViewSet)

urlpatterns = [
    path('admin/', admin.site.get_urls()),
    path('api/', include(router.urls)),
]
