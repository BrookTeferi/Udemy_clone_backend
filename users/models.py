import email
from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from courses.models import Course
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_superuser(self,email,password,name,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)


        if other_fields.get('is_staff')is not True:
            return ValueError('superuser must have is_staff True')

        if other_fields.get('is_superuser')is not True:
            return ValueError('superuser must have is_superuser True')

        return self.create_user(email,password,name,**other_fields)

      
    def create_user(self,email,password,name,**other_fields):
        if not email:
            raise ValueError('You must provide a valid email')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name,**other_fields)
        user.set_password(password)
        user.save()



class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255, unique=True)
    created=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)
    is_staff=models.BooleanField(default=False)
    paid_courses=models.ManyToManyField(Course)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']


    objects=UserManager()

    def __str__(self) -> str:
        return super().__str__()

    def get_all_courses(self):
        courses=[]
        return courses