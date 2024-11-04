from django.db import models

# Create your models here.

class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.user_name
class productmodel(models.Model):
    pro_id=models.IntegerField(primary_key=True)
    pro_name=models.CharField(max_length=100)
    user1=models.ForeignKey(user,on_delete=models.CASCADE)    


class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)

class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_age=models.IntegerField()
    emp_phno=models.CharField(max_length=11)

class Product(models.Model):
    pro_name=models.CharField(max_length=100)
    pro_desc=models.TextField()
    pro_price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_qntuy=models.IntegerField(null=True)
    created_at=models.DateField(auto_now_add=True)

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=11)
    address=models.TextField()
    date_of_birth=models.DateField()

class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class category(models.Model):
    cat_id=models.IntegerField(primary_key=True)
    cat_name=models.CharField(max_length=50)
    def __str__(self):
        return self.cat_name

class employ(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=50)
    cata=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self) :
        return self.emp_name
    
#task
class Publisher(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Bookm(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    isbn=models.CharField(max_length=100,unique=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)

#task
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_code=models.CharField(max_length=100,unique=True)
    date=models.DateField()
    def __str__(self):
        return self.course_name

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=11)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

class Organizer(models.Model):
    name=models.CharField(max_length=100)
    contact_email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Event(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    location=models.CharField(max_length=255)
    organizer=models.ForeignKey(Organizer,on_delete=models.CASCADE)

#task
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

#task
class Userreg(models.Model):
    username=models.CharField(max_length=2000)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100) 

class Userimg(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    user_img=models.ImageField(upload_to='image/')


class Image(models.Model):
    title=models.CharField(max_length=200)
    Image_up=models.ImageField(upload_to='image/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
     
    


