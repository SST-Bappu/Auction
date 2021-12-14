from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self,email,name=None,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,name="Admin"):
        user = self.create_user(email,name,password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255,blank=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    def __str__(self):
        return self.email

class auctionItem(models.Model):
    User = get_user_model()
    user= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200,null=True, blank=True)
    min_bid = models.FloatField(null = True)
    photo = models.ImageField(blank=True)
    end_date = models.DateField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    max_bid = models.FloatField(default=0)
    bid_winner = models.CharField(max_length=200,null=True,blank=True)

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.product_name
    
    class meta:
        db_table = '"auctions"'

class bids(models.Model):
    User = get_user_model()
    user= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    auction = models.ForeignKey(auctionItem,null=True, on_delete=models.SET_NULL)
    bid_price = models.FloatField(null=True)
    
    def __str__(self):
        return self.user.email

    class meta:
        db_table = '"auctions"'
 
