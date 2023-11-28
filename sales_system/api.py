import atexit
from rest_framework.authtoken.models import Token


def delete_all_tokens():
    Token.objects.all().delete()

atexit.register(delete_all_tokens)