from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    
    role=models.CharField(max_length=20,blank=False)
    
    def __str__(self):
        return self.username
    

class SuperVisor(models.Model):
      
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="employees")
    supervisor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="supervisors")
    supervisor_type=models.CharField(max_length=50,blank=False)
    
    
    def __str__(self):
        return  f"{self.supervisor}-{self.supervisor_type}"
    
class LeaveType(models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    paid = models.BooleanField()
    halfday_allowed = models.BooleanField()

    def __str__(self):
        return self.type
    
class LeaveDateType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
  
class Leave(models.Model):
    
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    from_date=models.DateField()
    to_date=models.DateField()
    from_date_type = models.ForeignKey(
        LeaveDateType, on_delete=models.SET_NULL, null=True, blank=True,related_name="from_dates"
    )
    to_date_type = models.ForeignKey(
        LeaveDateType, on_delete=models.SET_NULL, null=True, blank=True,related_name="to_dates"
    )
    reason=models.CharField(max_length=50,blank=False)
    updated_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True,related_name="updated_leaves"
    )
    updated_at=models.DateTimeField(auto_now=True)
    
    
    
    
