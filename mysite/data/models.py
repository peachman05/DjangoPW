from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    number_regis = models.CharField("เลขที่(ตามทะเบียนบ้าน)",max_length=10)
    village_no_regis = models.IntegerField("หมู่(ตามทะเบียนบ้าน)",default=0)
    village_name_regis = models.CharField("หมู่บ้าน(ตามทะเบียนบ้าน)",max_length=40)
    lane_regis = models.CharField("ซอย(ตามทะเบียนบ้าน)",max_length=40) # ซอย
    road_regis = models.CharField("ถนน(ตามทะเบียนบ้าน)",max_length=70) 
    sub_district_regis = models.CharField("ตำบล(ตามทะเบียนบ้าน)",max_length=70) 
    district_regis = models.CharField("อำเภอ(ตามทะเบียนบ้าน)",max_length=70)
    province_regis = models.CharField("จังหวัด(ตามทะเบียนบ้าน)",max_length=70)
    postal_code_regis = models.IntegerField("รหัสไปรษณีย์(ตามทะเบียนบ้าน)",default=0)
    smartphone_number_regis = models.CharField("เบอร์มือถือ(ตามทะเบียนบ้าน)",max_length=20)
    phone_number_regis = models.CharField("เบอร์โทรบ้าาน(ตามทะเบียนบ้าน)",max_length=20)

    number = models.CharField("เลขที่(ปัจจุบัน)",max_length=10)
    village_no = models.IntegerField("หมู่(ปัจจุบัน)",default=0)
    village_name = models.CharField("หมู่บ้าน(ปัจจุบัน)",max_length=40)
    lane = models.CharField("ซอย(ปัจจุบัน)",max_length=40) # ซอย
    road = models.CharField("ถนน(ปัจจุบัน)",max_length=70) 
    sub_district = models.CharField("ตำบล(ปัจจุบัน)",max_length=70) 
    district = models.CharField("อำเภอ(ปัจจุบัน)",max_length=70)
    province = models.CharField("จังหวัด(ปัจจุบัน)",max_length=70)
    postal_code = models.IntegerField("รหัสไปรษณีย์(ปัจจุบัน)",default=0)
    smartphone_number = models.CharField("เบอร์มือถือ(ปัจจุบัน)",max_length=20)
    phone_number = models.CharField("เบอร์โทรบ้าน(ปัจจุบัน)",max_length=20)

class AddressForm(ModelForm):
    class Meta:
        model = Address
        # fields = ['number_regis', 'village_no_regis', 'village_name_regis']
        # fields = '__all__'
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['number_regis'].widget.attrs['size'] = 5


class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    TITLE_LIST = (
        ('MR', 'Mr.(นาย)'),
        ('MRS', 'Mrs.(นาง)'),
        ('MISS', 'Miss.(นางสาว)'),
    )
    title = models.CharField(max_length=6,choices=TITLE_LIST)
    firstname_thai = models.CharField("ชื่อจริง(ไทย)",max_length=30)
    lastname_thai = models.CharField("นามสกุล(ไทย)",max_length=30)
    firstname_eng = models.CharField("ชื่อจริง(อังกฤษ)",max_length=30)
    lastname_eng = models.CharField("นามสกุล(อังกฤษ)",max_length=30)
    card_number = models.CharField("เลขบัตรประชาชน",max_length=20)
    religion = models.CharField("ศาสนา",max_length=20)
    BLOOD_TYPE_LIST = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )
    blood_type = models.CharField("กรุ๊ปเลือด",max_length=6,choices=BLOOD_TYPE_LIST)
    birth_date = models.DateField('วัน/เดือน/ปี เกิด')
    email =  models.EmailField("Email",max_length=60)
    STATUS_LIST = (
        ('MR', 'Married(แต่งงาน)'),
        ('SN', 'Single(โสด)'),
        ('DV', 'Divorce(หย่า)'),
        ('WD', 'Widow(หม้าย)'),
    )
    status = models.CharField("สถานะ",max_length=10,choices=STATUS_LIST)
    domicile_province = models.CharField("ภูมิลำเนาเดิม จังหวัด",max_length=30)

    firstname_spouse_thai = models.CharField("ชื่อจริงคู่สมรส(ไทย)",max_length=30)
    lastname_spouse_thai = models.CharField("นามสกุลคู่สมรส(ไทย)",max_length=30)
    firstname_spouse_eng = models.CharField("ชื่อจริงคู่สมรส(อังกฤษ)",max_length=30)
    lastname_spouse_eng = models.CharField("นามสกุลคู่สมรส(อังกฤษ)",max_length=30)

    firstname_father_thai = models.CharField("ชื่อจริง(ไทย)",max_length=30)
    lastname_father_thai = models.CharField("คำนำหน้า(ไทย)",max_length=30)
    firstnamename_father_eng = models.CharField("ชื่อจริง(อังกฤษ)",max_length=30)
    lastname_father_eng = models.CharField(max_length=30)

    firstname_mother_thai = models.CharField(max_length=30)
    lastname_mother_thai = models.CharField(max_length=30)
    firstname_mother_eng = models.CharField(max_length=30)
    lastname_mother_eng = models.CharField(max_length=30)

class PersonalInfoForm(ModelForm):
    class Meta:
        model = PersonalInfo
        exclude = ['user']

class WorkInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    start_service_date = models.DateField('date published')
    position = models.CharField(max_length=30)
    group = models.CharField(max_length=30) #สังกัด
    end_service_date = models.DateField('date published')
    current_position = models.CharField(max_length=60)
    position_number = models.CharField(max_length=20)
    rank_number = models.CharField(max_length=20)
    rank_money = models.IntegerField(default=0)
    academic_standing = models.CharField(max_length=20)
    academic_standing_money = models.IntegerField(default=0)

    start_PW_date = models.DateField('date published')
    isGPF_member = models.BooleanField()

    department = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)

class WorkInfoForm(ModelForm):
    class Meta:
        model = WorkInfo
        exclude = ['user']

class Insignia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    class1 = models.CharField(max_length=60)
    date1 = models.DateField('date published')

class InsigniaForm(ModelForm):
    class Meta:
        model = Insignia
        exclude = ['user']
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    acronym_bachelor = models.CharField(max_length=10)
    major_field_bachelor = models.CharField(max_length=40)
    minor_field_bachelor = models.CharField(max_length=40)
    start_year_bachelor = models.DateField('date published')
    end_year_bachelor = models.DateField('date published')

    acronym_master = models.CharField(max_length=10)
    major_field_master = models.CharField(max_length=40)
    minor_field_master = models.CharField(max_length=40)
    start_year_master = models.DateField('date published')
    end_year_master = models.DateField('date published')

    acronym_phD = models.CharField(max_length=10)
    major_field_phD = models.CharField(max_length=40)
    minor_field_phD = models.CharField(max_length=40)
    start_year_phD = models.DateField('date published')
    end_year_phD = models.DateField('date published')

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['user']