from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from django.contrib.auth import get_user_model


class CustomAuthenticate(BaseAuthentication):
    def authenticate(self, request):
        user_model = get_user_model()
        if request.data:
            if '@' in request.data.get('username'):
                user = user_model.objects.get(email=request.data.get('username'))
            else:
                user = user_model.objects.get(username=request.data.get('username'))
            if user.check_password(request.data.get('password')):
                return (user, None)
        return AnonymousUser(), None
