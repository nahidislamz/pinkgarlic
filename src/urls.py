from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home.views import homeView
from menus.views import menuPage


admin.site.site_header = 'Pink Garlic Admin Panel'
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'Pink Garlic Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('', include('accounts.urls')),
    path('menu/', menuPage, name='menu'),
    path('', include('cart.urls')),
    path('', include('checkout.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
