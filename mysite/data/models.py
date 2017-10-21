from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Address(models.Model):
    number_regis = models.CharField(max_length=10)
    village_no_regis = models.IntegerField(default=0)
    village_name_regis = models.CharField(max_length=40)
    lane_regis = models.CharField(max_length=40) # ซอย
    road_regis = models.CharField(max_length=70) 
    sub_district_regis = models.CharField(max_length=70) 
    district_regis = models.CharField(max_length=70)
    province_regis = models.CharField(max_length=70)
    postal_code_regis = models.IntegerField(default=0)
    smartphone_number_regis = models.CharField(default=20)
    phone_number_regis = models.CharField(default=20)

    number = models.CharField(max_length=10)
    village_no = models.IntegerField(default=0)
    village_name = models.CharField(max_length=40)
    lane = models.CharField(max_length=40) # ซอย
    road = models.CharField(max_length=70) 
    sub_district = models.CharField(max_length=70) 
    district = models.CharField(max_length=70)
    province = models.CharField(max_length=70)
    postal_code = models.IntegerField(default=0)
    smartphone_number = models.CharField(default=20)
    phone_number = models.CharField(default=20)


class PersonalInfo(models.Model):

	TITLE_LIST = (
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MISS', 'Miss.'),
    )
    title = models.CharField(max_length=6,choices=TITLE_LIST)
    firstname_thai = models.CharField(max_length=30)
    lastname_thai = models.CharField(max_length=30)
    firstname_eng = models.CharField(max_length=30)
    lastname_eng = models.CharField(max_length=30)
    card_number = models.CharField(max_length=20)
    religion = models.CharField(max_length=20)
    BLOOD_TYPE_LIST = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )
    blood_type = models.CharField(max_length=6,choices=BLOOD_TYPE_LIST)
    pub_date = models.DateField('date published')