from django.urls import path
from .views import *

urlpatterns = [
    path('forms/', FormPageView.as_view()),
    path('producttable/', ProductTableView.as_view()),
    path('producttable/delete/<int:id>/',ProductDeleteView.as_view(), name='product_delete'),
    path('producttable/update/<int:id>/',ProductUpdateView.as_view(), name='product_update'),
]