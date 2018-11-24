import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CustomerManager(models.Manager):
	def for_user(self, user):
		return self.filter(id=user)

MALE = 'M'
FEMALE = 'F'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female')
)
class Customer(models.Model):
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    Gender = models.CharField(
        max_length = 1,
        choices = GENDER_CHOICES,
        default = MALE,
    )
    Number = models.IntegerField()
    Address = models.CharField(max_length=200)
    Created_At = models.DateTimeField('date created', default=timezone.now())
    objects = CustomerManager()
    def __str__(self):
        return "%s %s" % (Name, Surname)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Created_At <= now

    was_published_recently.admin_order_field = 'Created_At'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'

class Restaurant_Branch(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.IntegerField()
    Address = models.CharField(max_length=200)

class Manager(models.Model):
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    Gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    Number = models.IntegerField()
    Created_At = models.DateTimeField('date created', default=timezone.now())
    Restaurant_Branch_ID = models.ForeignKey(Restaurant_Branch, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return "%s %s" % (Name, Surname)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Created_At <= now

    was_published_recently.admin_order_field = 'Created_At'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'

class Cart(models.Model):
    Amount_of_Order = models.IntegerField()
    Total_Price = models.IntegerField()
    Total_Discount = models.IntegerField()
    Ordered_At = models.DateTimeField('date ordered', default=timezone.now())
    Manager_ID = models.ForeignKey(Manager, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return "Cart #%d" % (self.id)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Ordered_At <= now

    was_published_recently.admin_order_field = 'Ordered_At'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Ordered recently?'

class Pizza_List(models.Model):
    Created_At = models.DateTimeField('date created')
    def __str__(self):
        return "List #%d" % (self.id)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Created_At <= now

    was_published_recently.admin_order_field = 'Created_At'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'

class Pizza(models.Model):
    List_ID = models.ForeignKey(Pizza_List, on_delete=models.CASCADE, default=0)
    Name = models.CharField(max_length=200)
    Filling = models.CharField(max_length=500)
    LITTLE_SIZE = 'L'
    AVERAGE_SIZE = 'A'
    BIG_SIZE = 'B'
    DOUGH_LAYER_LEVELS = (
        (LITTLE_SIZE, 'Thin'),
        (AVERAGE_SIZE, 'Average'),
        (BIG_SIZE, 'Plump'),
    )
    Dough_Layer = models.CharField(
        max_length = 1,
        choices = DOUGH_LAYER_LEVELS,
        default = AVERAGE_SIZE,
    )
    Price = models.IntegerField()
    Discount = models.IntegerField()
    Cart_ID = models.ForeignKey(Cart, on_delete=models.CASCADE, default=0)
    Created_At = models.DateTimeField('date created', default=timezone.now())

    def __str__(self):
        return self.Name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Created_At <= now

    was_published_recently.admin_order_field = 'Created_At'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'