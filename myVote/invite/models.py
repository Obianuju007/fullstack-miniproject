from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, gender, nickname, password):
        # function for creating a user
        if not email:
            raise ValueError("Email field must be filled")
        if not full_name:
            raise ValueError("Please write your full name")
        if not gender:
            raise ValueError("Please select an option")
        if not password:
            raise ValueError("Password field must be filled")

        user= self.model(
            email=self.normalize_email(email=email), 
            # ensures all email domain name is in lowerletters
            gender=gender,
            nickname=nickname,
            full_name=full_name
        )
        user.set_password(raw_password=password)
        # hashes your password in case someone hacks into your database from being seen.
        user.save(using=self._db)

        return user

    def create_superuser(self, email, full_name, gender, password):
        """ Creating a super user """
        user = self.create_user(
            email=email,
            full_name=full_name,
            gender=gender,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
#  Model representation for a user
    full_name = models.CharField(max_length=100, verbose_name = 'Your full name here')
    nickname = models.CharField(max_length=20, verbose_name='Nickname')
    gender = models.CharField(max_length=10)    # Male/ Female
    email = models.EmailField(max_length=40, verbose_name='What is your email address?', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # No need for a password field because the AbstractBaseUser default model has a password and a last-login field. 

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['full_name', 'nickname', 'gender']

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
       return  str(self.full_name) + ' - ' + str(self.gender) + ' - ' + str(self.email)
    
    def get_short_name(self):
        return self.nickname
    

class Login(models.Model):
    email = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    
class Create_Event(models.Model):
    nature_of_event = models.CharField(max_length=100, blank=False)
    title_of_event = models.CharField(max_length=100, blank=False)
    number_of_guests = models.IntegerField(default=0, blank=False)
    location = models.CharField(max_length=100, blank=False)
    date_time = models.DateTimeField(null=True, blank=False)
    hash_tag = models.CharField(max_length=50)
    rsvp = models.IntegerField(default=0, blank=True)    
    flyer_image = models.ImageField(upload_to='invite/media') 

    


