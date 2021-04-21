
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
=======
from django.urls import path, include
from polls import views as polls_views
<<<<<<< HEAD
>>>>>>> parent of dd8e683 (login enabled)
=======
>>>>>>> parent of dd8e683 (login enabled)

urlpatterns = [
    path('', include('pages.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('users.urls')),
<<<<<<< HEAD
=======
    path('', polls_views.home, name='home'),
    path('users/', include('users.urls')),
    path('create/', polls_views.create, name='create'),
    path('vote/<poll_id>/', polls_views.vote, name='vote'),
    path('results/<poll_id>/', polls_views.results, name='results'),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
<<<<<<< HEAD
>>>>>>> parent of dd8e683 (login enabled)
=======
>>>>>>> parent of dd8e683 (login enabled)
=======
>>>>>>> parent of 34d5ad8 (Merge branch 'master' of https://github.com/agrash3/Indecisive_App into master)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
