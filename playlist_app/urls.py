from django.urls import path, include
from playlist_app import views

#urlpatterns = [
    #path('', views.index, name='index'),
    #path('login/', views.users, name='login'),
    #path('', include('social_django.urls', namespace='social')),
    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

#]
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from users import views
from .views import login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^$', login)
]
