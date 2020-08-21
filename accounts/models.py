from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, birth_date, cidade,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Email inválido')
        if not password:
            raise ValueError('Senha inválida')
        if not full_name:
            raise ValueError('Preencha o nome')
        if not birth_date:
            raise ValueError('Preencha a data de nascimento corretamente')
        if not cidade:
            raise ValueError('Preencha a cidade corretamente')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            birth_date=birth_date,
            cidade=cidade,
        )

        user.set_password(password)
        user.active = True
        user.staff = False
        user.admin = False
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, full_name, birth_date, cidade, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            birth_date,
            cidade,
            password=password,
        )
        user.active = True
        user.staff = True
        user.admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, birth_date, cidade, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            birth_date,
            cidade,
            password=password,
        )
        user.active = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=255,blank=True,null=True)
    birth_date = models.DateField()
    cidade = models.CharField(max_length=255,blank=True,null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    #phone =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','birth_date','cidade'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.full_name.split(' ',1)[0]

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()



class Helper(models.Model):
    email = models.ForeignKey(User,on_delete=models.CASCADE)



class Client(models.Model):
    email = models.ForeignKey(User,on_delete=models.CASCADE)


admin.site.register(Client)
admin.site.register(User)
admin.site.register(Helper)
