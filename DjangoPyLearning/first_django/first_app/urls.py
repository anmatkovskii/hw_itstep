from django.urls import path, include
from first_app.views import add, show_info

urlpatterns = [
    path('add/<str:product_name> <int:price>/', add),
    path('show/<str:product_name>/', show_info)
]