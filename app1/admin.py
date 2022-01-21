from django.contrib import admin
from.models import *

# Register your models here.
class adminmodel(admin.ModelAdmin):
    list_display=['name','price','Order_date','del_date']
    list_filter=['category_name','price']
    list_max_show_all=4
class logindata(admin.ModelAdmin):
    list_display=['Email','Password']
class orderfilter(admin.ModelAdmin):
    list_display = ('person','order_id','Bitem','ordered_on')
class cartfilter(admin.ModelAdmin):
    list_display = ('person', 'Item' ,'status','added_on')

admin.site.register(products,adminmodel)
admin.site.register(category)
admin.site.register(login,logindata)
admin.site.register(signup,logindata)
admin.site.register(items)
admin.site.register(Mycart,cartfilter)
admin.site.register(Orders,orderfilter)


