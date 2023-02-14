from django.urls import path
from . import views

urlpatterns=[
	
	path('about/',views.about),
	path('contact/',views.contact),
	path('',views.index),
	path('services/',views.services),
	path('register/',views.register),
	path('login/',views.login),
	path('logout/',views.logout),
    path('display/',views.display),
    path('update/',views.update),
    path('delete/',views.delete),
    path('single/',views.single),
    path('cart/',views.cart),
    path('addtocart/',views.addtocart),
    path('payment/',views.upayment),

    path('womens/',views.womens),



##########################################################################################################################
###########################################ADMIN#####################################################################
 
    path('adindex/',views.ad_index),
    path('adform/',views.ad_form),
    path('adlogin/',views.ad_login),
    path('adreg/',views.ad_register),
    path('adtable/',views.ad_table),
    path('adupdate/',views.ad_update),
    path('addelete/',views.ad_delete),
    path('adlogout/',views.ad_logout),







]