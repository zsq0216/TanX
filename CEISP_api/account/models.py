from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 测试model
class Account(models.Model):
    Enterprise_Name = models.TextField(max_length=200)
    Enterprise_Tel = models.TextField(max_length=13)
    Enterprise_Mail = models.CharField(max_length=200)
    Enterprise_Key = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.Enterprise_Name}'
    
######################################
# 下面是正式model
######################################
    
class EnterpriseUser(AbstractUser):
    Enterprise_Name = models.TextField(max_length=200,default='')
    Enterprise_Intro = models.TextField(max_length=2000,default='')
    Enterprise_Legalperson = models.TextField(max_length=100,default='')
    is_Enterprise = models.BooleanField(default = True)
    
    class Meta:
        db_table = 'tb_users'
        verbose_name = '公司账号信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Scope1emissions(models.Model):
    rawcoal_t = models.FloatField(default=0)
    cleanedcoal_t = models.FloatField(default=0)
    coke_t = models.FloatField(default=0)
    naturalgas_104m3 = models.FloatField(default=0)
    gasoline_t = models.FloatField(default=0)
    diesel_t = models.FloatField(default=0)
    others_t = models.FloatField(default=0)
    file1 = models.FileField(upload_to='./files/files1',default='nofile')
    year = models.IntegerField()
    month = models.IntegerField()
    uploadtime = models.DateTimeField(auto_now=True)
    Enterprise = models.ForeignKey(EnterpriseUser,
                                   to_field='username',
                                   related_name='scope1',
                                   on_delete = models.CASCADE)
    fixburn = models.FloatField(default=0)
    movingburn = models.FloatField(default=0)
    emission1 = models.FloatField(default=0)
    is_certified = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.fixburn = 1.98*self.rawcoal_t+2.41*self.cleanedcoal_t+2.86*self.coke_t+21.62*self.naturalgas_104m3 + 2.93*self.gasoline_t+3.10*self.diesel_t+self.others_t
        self.movingburn = 2.93*self.gasoline_t+3.10*self.diesel_t
        self.emission1 = self.fixburn+self.movingburn
        return super(Scope1emissions,self).save(*args, **kwargs)
    
class Scope2emissions(models.Model):
    electricity_104kwh = models.FloatField(default=0)
    heating_GJ = models.FloatField(default=0)
    file2 = models.FileField(upload_to='./files/files2',default='nofile')
    year = models.IntegerField()
    month = models.IntegerField()
    uploadtime = models.DateTimeField(auto_now=True)
    Enterprise = models.ForeignKey(EnterpriseUser,
                                   to_field='username',
                                   related_name='scope2',
                                   on_delete = models.CASCADE)
    electricity = models.FloatField(default=0)
    heating = models.FloatField(default=0)
    emission2 = models.FloatField(default=0)
    is_certified = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.electricity = 0.11*self.electricity_104kwh
        self.heating = 7.63*self.heating_GJ
        self.emission2 = self.electricity+self.heating
        return super(Scope2emissions,self).save(*args, **kwargs)
    
class Scope3emissions(models.Model):
    plane_kyuan = models.FloatField(default=0)
    CRH_kyuan = models.FloatField(default=0)
    train_kyuan = models.FloatField(default=0)
    urbantransport_kyuan = models.FloatField(default=0)
    selfdriving_per = models.FloatField(default=0)
    publictransport_per = models.FloatField(default=0)
    file3 = models.FileField(upload_to='./files/files3',default='nofile')
    year = models.IntegerField()
    month = models.IntegerField()
    uploadtime = models.DateTimeField(auto_now=True)
    Enterprise = models.ForeignKey(EnterpriseUser,
                                   to_field='username',
                                   related_name='scope3',
                                   on_delete = models.CASCADE)
    travel = models.FloatField(default=0)
    commuting = models.FloatField(default=0)
    emission3 = models.FloatField(default=0)
    is_certified = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.travel = 0.176*self.plane_kyuan+0.069*self.CRH_kyuan+0.540*self.train_kyuan+0.019*self.urbantransport_kyuan
        self.commuting = 0.0546*self.selfdriving_per+0.0182*self.publictransport_per
        self.emission3 = self.travel + self.commuting
        return super(Scope3emissions,self).save(*args, **kwargs)

class offset(models.Model):
    green_electricity_104kwh = models.FloatField(default=0)
    otheroffset_t = models.FloatField(default=0)
    output_wyuan = models.FloatField(default=0)
    file4 = models.FileField(upload_to='./files/files4',default='nofile')
    year = models.IntegerField()
    month = models.IntegerField()
    uploadtime = models.DateTimeField(auto_now=True)
    Enterprise = models.ForeignKey(EnterpriseUser,
                                   to_field='username',
                                   related_name='offset',
                                   on_delete = models.CASCADE)
    offset = models.FloatField(default=1)
    is_certified = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.offset = self.green_electricity_104kwh * 0.11 + self.otheroffset_t
        return super(offset,self).save(*args, **kwargs)
