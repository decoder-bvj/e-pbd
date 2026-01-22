
from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard
from bmc.views import bmc_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('bmc/pdf/<int:pk>/', bmc_pdf, name='bmc-pdf'),
]
