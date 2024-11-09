from django.db import models

# Create your models here.
class Enquiry(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    address=models.TextField()
    enquirytext=models.TextField()
    enquirydate=models.DateField(max_length=30)

class AdminLogin(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class tblSession(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    ses=models.CharField(max_length=20)
    created_date=models.DateTimeField()

class tbl_course(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    course_session=models.CharField(max_length=30)
    course_name=models.CharField(max_length=300)
    course_fees=models.CharField(max_length=100)
    course_duration=models.CharField(max_length=50)
    created_date=models.DateTimeField()

class Student(models.Model):
    sid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    emailaddress=models.CharField(max_length=50)
    contactno=models.CharField(max_length=15)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=15)
    dob=models.CharField(max_length=20)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    address=models.TextField()
    aadharno=models.CharField(max_length=15)
    aadharpic=models.ImageField(upload_to='myimage',null=True)
    session=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    coursefees=models.CharField(max_length=50)
    courseduraction=models.CharField(max_length=50)
    hs_percent=models.CharField(max_length=10)
    hs_marksheet=models.ImageField(upload_to='myimage',null=True)
    inter_percent=models.CharField(max_length=10)
    inter_marksheet=models.ImageField(upload_to='myimage',null=True)
    pic=models.ImageField(upload_to='myimage',null=True)
    sign=models.ImageField(upload_to='myimage',null=True)
    application_status=models.CharField(max_length=1)
    fees=models.CharField(max_length=20)
    fees_status=models.CharField(max_length=1)
    fees_sc=models.FileField(null=True,upload_to='myimage')
    status=models.CharField(max_length=1)
    

