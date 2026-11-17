from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


from django.db.models.signals import post_save

# ===========================================================================================
#                                  User Creation
# ===========================================================================================


class User(AbstractUser):

    phone = models.CharField(max_length=12)

    ROLE_CHOICES = (
                    ('student','student'),
                    ('trainer','trainer'),
                    ('admin','admin')
    )

    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='student')

# ===========================================================================================
#                                 Student Profile
# ===========================================================================================

class StudentProfile(models.Model):

    student_name = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=200,null=True)
    passout_year = models.CharField(max_length=10,null=True)
    github_url = models.URLField(max_length=10,null=True)
    linkedin_url = models.URLField(max_length=10,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    student_id = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")

    def __str__(self):
        return self.student_name



def create_student_profile(sender,instance,created,*args,**kwargs):
    if created and instance.role == "student":
        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)

# ===========================================================================================
#
# ===========================================================================================


class TrainerProfile(models.Model):

    trainer_name = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=200,null=True)
    language = models.CharField(max_length=200,null=True)
    experiance_year = models.IntegerField(max_length=10,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    trainer_id = models.OneToOneField(User,on_delete=models.CASCADE,related_name="trainer")

    def __str__(self):
        return self.trainer_name

       
def create_trainer_profile(sender,instance,created,*args,**kwargs):
        if created and instance.role == "trainer":
            TrainerProfile.objects.create(student=instance)
    
post_save.connect(create_trainer_profile,sender=User)
