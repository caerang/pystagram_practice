from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
def profile(request, username):
    user_model = get_user_model()
    user = get_object_or_404(user_model, username=username)
    photos = user.photo_set.order_by('-created_at', '-pk')

    ctx = {
        'user': user,
        'photos': photos,
    }
    return render(request, 'profile.html', ctx)
