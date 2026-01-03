from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teams(models.Model):
    teamName = models.CharField(max_length=200, null=True)
    teamLeaderName = models.CharField(max_length=250, null=True)
    teamLeadMobno = models.CharField(max_length=15, null=True)
    teamMembers = models.CharField(max_length=300, null=True)
    postingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teamName

class Firereport(models.Model):
    FullName = models.CharField(max_length=250, null=True, db_column='fullname')
    MobileNumber = models.CharField(max_length=12, null=True, db_column='mobilenumber')
    Location = models.CharField(max_length=200, null=True, db_column='location')
    Message = models.CharField(max_length=200, null=True, db_column='message')
    AssignTo = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column='assignto_id')
    Status = models.CharField(max_length=150, null=True, db_column='status')
    Postingdate = models.DateTimeField(auto_now_add=True, db_column='postingdate')
    AssignedTime = models.CharField(max_length=150, null=True, db_column='assignedtime')
    #AssignedTime = models.DateTimeField(null=True)
    UpdationDate = models.DateTimeField(null=True, db_column='updationdate')
    Account_id = models.IntegerField(default=0, db_column='account_id')
    AssignBy = models.IntegerField(default=0, db_column='assignby')

    def __str__(self):
        return self.FullName

class Firetequesthistory(models.Model):
    firereport = models.ForeignKey(Firereport, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=200, null=True)
    remark = models.CharField(max_length=250, null=True)
    postingDate = models.DateTimeField(auto_now_add=True)
    AssignTo = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_column='assignto_id')
    AssignBy = models.IntegerField(default=0)
    def __str__(self):
        return self.status

