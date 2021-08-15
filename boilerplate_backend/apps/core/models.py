from django.contrib.auth.models import AbstractUser

# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model


class User(AbstractUser):
    pass
