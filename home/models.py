from django.db import models

# Create your models here.




from enum import unique
from django.db import models
from django.core.validators import MaxLengthValidator, RegexValidator ,MinLengthValidator
import datetime
import calendar

# Create your models here.

gender_choices=(
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

def renewal_date_time():
    day = datetime.datetime.now().date()
    one_year_delta = datetime.timedelta(days=366 if ((day.month >= 3 and calendar.isleap(day.year+1)) or
                                            (day.month < 3 and calendar.isleap(day.year))) else 365)

    return day + one_year_delta

class beneficiary(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$', message="Phone number must be entered in the format: '+999999999999' or '9999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, null=False, blank=False) # validators should be a list
    date_of_birth = models.DateField(null=False)
    age = models.IntegerField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    adhar_number = models.CharField(max_length=12, unique=True, blank=False)
    pan_number = models.CharField(max_length=10, unique=True, blank=False)
    gender = models.CharField(max_length=50, blank=False, null=False, choices=gender_choices, default=gender_choices[0][0])
    date_of_registration = models.DateTimeField(auto_now=True)
    validity_status = models.CharField(max_length=20)
    next_renewal_date = models.DateField(default=renewal_date_time)
    message_sent = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.full_name
        