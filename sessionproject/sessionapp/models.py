from django.db import models

# Create your models here.

gen = (
    ('M','Male'),
    ('F','Female')
)


class SignupData(models.Model):
    Name = models.CharField(max_length=40)
    Mob_No = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10,default=None,choices=gen)
    Email = models.EmailField(max_length=50, unique=True)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return f"Name={self.Name}-Mob-no={self.Mob_No}-Email={self.Email}-Password={self.Password}"
