from django.urls import path
from .views import*
urlpatterns = [
    path('customerform/',CustomerForm),
    path('customertable/',CustomerTable),
    path('customertable/delete/<int:id>/',DeleteCustomer, name = 'customer_delete'),
    path('customertable/update/<int:id>/',UpdateCustomer, name = 'customer_update'),
    path('ordersform/',OrderForm),
    path('ordertable/',OrderTable),
    path('orderdelete/<int:id>/',DeleteOrder, name='delete_order'),
    path('orderupdate/<int:id>/',UpdateOrder, name='update_order'),

]