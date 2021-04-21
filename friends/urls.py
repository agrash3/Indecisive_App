from django.urls import path

urlpatterns = [
    path('send_friend_request/<int:userID>/', send_friend_request, name='send friend request'),
]
