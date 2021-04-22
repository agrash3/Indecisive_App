from django.urls import path

from . import views
from users import views as users_views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name='resultsdata'),
<<<<<<< HEAD
    path('signup/', users_views.SignUpView, name='signup'),
]
=======
]
>>>>>>> bb701322efbda1d8bf64c0f2f189fe194a17c03c
