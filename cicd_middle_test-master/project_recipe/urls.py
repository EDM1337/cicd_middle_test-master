from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]