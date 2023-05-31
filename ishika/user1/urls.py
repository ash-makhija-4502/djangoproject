from django.urls import path
from user1.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

path('login/',login,name='abcd'),
path('table/',tableview),
path('table_filter/',tablefilter),
path('logout/',logout,name="logout1"),
path('table_get/',tableget),
path('producttable/',producttable),
path('product_filter/',producttable_filter),
path('product_get/',producttable_get),
path('register/',registrationpage,name='rp'),
path('',index,name='index2'),
path('contact/',contact,name="ishika"),
path('about/',about,name='ish'),
path('product_display/',product_display,name="dcb"),
path('prouct_display_all',product_display_all),
path('product-filter/<int:id>/',productcategorywise,name='productfilter'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)