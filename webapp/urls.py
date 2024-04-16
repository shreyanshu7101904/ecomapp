from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("add", views.CreateProduct.as_view(), name='add_prod'),
    path("bill", views.CreateBill.as_view(), name="bill"),
    path("viewbill/<pks>", views.BillView.as_view(), name="gbill")
]