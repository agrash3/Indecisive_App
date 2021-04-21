from django.shortcuts import render


# Create your views here.
@login_required
def send_friend_request(request, userID)
    sender = request.user
    receiver = user.objects.get(id=userID)
    friend_request, created = FriendRequest.objects.get_or_create(se der=sender, receiver=receiver)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')
