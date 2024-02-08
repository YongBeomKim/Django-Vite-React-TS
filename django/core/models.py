from typing import List
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework_simplejwt.tokens import SlidingToken


# User Model Manager
class UserManager(BaseUserManager):

    def create_user(self, email, username=None, password=None, check=True):
        assert email is not None, 'Users must have an Email Addresss'
        if check:
            assert email not in settings.MASTER_EMAIL, f'{email} 은 관리자 이메일 입니다.'
            assert username not in settings.MASTER_USERNAME, f'{username} 은 관리자만 가능합니다.'

        user = self.model(email = email, username = username)
        user.set_password(password)
        user.save(using = self._db)
        SlidingToken.for_user(user=user)
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
            check=False
        )
        user.is_superuser = True
        user.is_manager = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


# User
class User(AbstractBaseUser):

    email    = models.EmailField(verbose_name='이메일',unique=True,db_index=True)
    username = models.CharField(verbose_name='닉네임',max_length=100,unique=True)
    is_superuser = models.BooleanField(verbose_name='최고관리자', default=False)
    is_active    = models.BooleanField(verbose_name='계정활성화', default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    objects      = UserManager()
    # created  = False # 중복작업 확인용 메서드
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = ['username']

    def __str__(self) -> str:
        return self.username + f" ({self.email})"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
