from django.contrib import admin
from django.urls import path, include
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.home, name='home'),  # Página principal con posts
    path('blog/', include('blog.urls')),          # Opcional: página completa del blog
]
