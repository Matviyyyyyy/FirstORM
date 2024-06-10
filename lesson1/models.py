from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField("Course")

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class MyModel(models.Model):
    short_text = models.CharField(max_length=100)
    long_text = models.TextField()
    number = models.IntegerField()
    float_number = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True)
    related = models.ForeignKey(Course, related_name="one_to_many", on_delete=models.DO_NOTHING)
    many_to_many = models.ManyToManyField(Course, related_name="onetomany")
    true_false = models.BooleanField(default=False)


