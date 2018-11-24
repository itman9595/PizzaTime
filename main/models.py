import datetime
from django.db import models
from django.utils import timezone

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
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    gender = models.CharField(
        max_length = 1,
        choices = GENDER_CHOICES,
        default = MALE,
    )
    number = models.IntegerField()
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')
    objects = CustomerManager()
    def __str__(self):
        return "%s %s" % (name, surname)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'

class Restaurant_Branch(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    address = models.CharField(max_length=200)

class Manager(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    number = models.IntegerField()
    created_at = models.DateTimeField('date created')
    restaurant_branch_id = models.ForeignKey(Restaurant_Branch, on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s" % (name, surname)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'

class Cart(models.Model):
    amount_of_order = models.IntegerField()
    total_price = models.IntegerField()
    total_discount = models.IntegerField()
    ordered_at = models.DateTimeField('date ordered')
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
    def __str__(self):
        return "Cart #%d" % (self.id)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.ordered_at <= now

    was_published_recently.admin_order_field = 'ordered_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Ordered recently?'

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=1000)
    LITTLE_SIZE = 'L'
    AVERAGE_SIZE = 'A'
    BIG_SIZE = 'B'
    DOUGH_LAYER_LEVELS = (
        (LITTLE_SIZE, 'Thin'),
        (AVERAGE_SIZE, 'Average'),
        (BIG_SIZE, 'Plump'),
    )
    dough_layer = models.CharField(
        max_length=1,
        choices=DOUGH_LAYER_LEVELS
    )
    price = models.IntegerField()
    discount = models.IntegerField()
    created_at = models.DateTimeField('date created')
    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now

    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Created recently?'