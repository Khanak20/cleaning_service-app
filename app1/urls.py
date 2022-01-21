from app1.views import *
from django.urls import path
from django.conf.urls.static import static
from app1 import views



# from views import hello
urlpatterns = [    
    path('hello/',hello,name='hello'),
    path('Home1/',home,name='home1'),
    path('Home2/',clean,name='clean1'),
    path('get/',page,name='get'),
    path('get1/',page1,name='get1'),
    path('get2/',page2,name='get2'),
    path('regi/',regist,name='regi'),
    path('',regist1,name='regi1'),
    path('home/',index,name='home'),
    path('items/',items1,name='item'),
    path('gallery1/',gallery,name='gallery1'),
    path('view/<int:pk>',book_view,name='book_view'),
    path('edit/<int:pk>', views.book_update, name='book_edit'),
    path('delete/<int:pk>', views.book_delete, name='book_delete'),
    path('forgot/',forgot,name='forgot'),
    path('conf/',Confirm,name='conf'),
    path('cart/', add_to_cart, name='Cart'),
    path('invoice/<int:pk>',invoice,name='invoice'),
    path('myaccount/', myaccount, name='myaccount'),
    path('placeorder/', place_order, name='place_order'),
    path('qr/<int:order_id>/', qrshow, name='qr'),
    path('deleteitem/<int:id>/', remove_cart, name='delete'),

    # ____________________payment__________________
    path('razor/', razor, name='razor'),
    path('success' , success , name='success'),
    path('checkout/' , checkout , name='checkout'),






]