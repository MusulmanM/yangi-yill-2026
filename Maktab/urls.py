from . import views
from django.urls import path

urlpatterns = [
    path('', views.maktab, name='maktab'),
    # path('admin/', admin.site.urls),
    
]
