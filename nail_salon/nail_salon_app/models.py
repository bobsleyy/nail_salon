from django.db import models

# Create your models here.


class ServiceType(models.Model):
    """Model for Service Types"""
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class LengthType(models.Model):
    """Model for Length Types"""
    name = models.CharField(max_length=64, unique=True)
    length = models.CharField(max_length=5, unique=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.length})"


class Service(models.Model):
    """Model for Service"""
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    length_type = models.ForeignKey(LengthType, on_delete=models.CASCADE)
    # before_made_by = models.ForeignKey(BeforeMadeBy, on_delete=models.CASCADE)
    # addon = models.ForeignKey(Addons, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    execution_time = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.service_type} - {self.length_type}"


class BeforeMadeBy(models.Model):
    """Model for ask nails were made in my salon or no"""
    made_by = models.CharField(max_length=64, unique=True)
    add_cost = models.DecimalField(max_digits=5, decimal_places=2)
    display_name = models.CharField(max_length=64)

    def __str__(self):
        return self.display_name


class Addons(models.Model):
    """Model for addons"""
    name = models.CharField(max_length=64, unique=True)
    add_time = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class QuantityOfAddons(models.Model):
    """Model for quantity of addons"""
    quantity = models.IntegerField(default=0)
    add_cost = models.DecimalField(max_digits=5, decimal_places=2)
    add_time = models.IntegerField(default=0)


class VisitRegistration(models.Model):
    """Model for registration of visit"""
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    datetime = models.DateTimeField(unique=True)
    # time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    made_by = models.ForeignKey(BeforeMadeBy, on_delete=models.CASCADE)
    quantity = models.ForeignKey(QuantityOfAddons, on_delete=models.CASCADE)
    addons = models.ManyToManyField(Addons)

    def __str__(self):
        return self.first_name + " " + self.second_name


class Photos(models.Model):
    """Model for photos"""
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    upload = models.FileField(upload_to='')

