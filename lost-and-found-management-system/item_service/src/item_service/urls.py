from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
def root_view(request):
    return HttpResponse("Welcome to the Item Management Service!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', include('items.urls')),
     path('', root_view, name='root'),

]
