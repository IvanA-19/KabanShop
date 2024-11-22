from users.models import UserProfile


def user_avatar(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(email=request.user.email)
        avatar = profile.avatar
        return {'avatar': avatar}
    return {'avatar': None}
