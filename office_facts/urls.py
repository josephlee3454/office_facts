
from django.urls import path
from .views import OfficeFactList, OfficeFactDetail

urlpatterns = [
    path('', OfficeFactList.as_view(), name='fact_list'),
    path('<int:pk>/', OfficeFactDetail.as_view(), name='fact_detail')
]