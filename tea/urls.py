from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.signup, name = 'signup'),
    path('variety/', views.variety, name = 'variety'),
    path('add_product/<id>', views.addProduct, name='addProduct'),
    path('single_variety/<id>', views.specificVariety, name='specificVariety'),
    path('suppliers', views.suppliers, name='suppliers')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)