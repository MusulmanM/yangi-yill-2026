from . import views
from django.urls import path

urlpatterns = [
    path('', views.maktab, name='maktab'),
    path('<int:pk>/', views.maktab_detail, name='maktab_detail'),
    # path('admin/', admin.site.urls),
    
]
