from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45)
#     email = models.EmailField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#     phone_number = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=45)
    # last_login = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Driver(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Driver {self.first_name} {self.last_name}"

class Bus(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    plate_no = models.CharField(max_length=20, unique=True)
    no_seats = models.PositiveIntegerField()
    route = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.plate_no}"

class Ticket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)