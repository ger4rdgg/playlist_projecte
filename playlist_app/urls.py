from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views
from .views import login, index

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^$', index),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')

]
