from django.urls import path
from .views import UserRegistration ,UserLogIn , UserLogOut

urlpatterns = [
    path('login/', UserLogIn.as_view(), name='loginn(token_obtain_pair)'),
    path('signup/', UserRegistration.as_view(), name='signup'),
    path('logout/', UserLogOut.as_view(), name='logout(token_revoke)'),
]
