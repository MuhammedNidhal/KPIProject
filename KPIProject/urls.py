from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI
from KPI.api.train import *


api = NinjaAPI(title="KPI Project")
api.add_router("/train",train_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('api/', api.urls),
]
