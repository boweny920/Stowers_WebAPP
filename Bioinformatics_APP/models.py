from django.db import models

# Create your models here.
class pubData_RunData(models.Model):
    """
    Model to store the run data for public data submissions.
    """
    Identifiers = models.CharField(max_length=1000)
    Reference = models.CharField(max_length=100)
    UserID = models.CharField(max_length=10)
    Lab = models.CharField(max_length=100)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Analysis = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.UserID} - {self.Lab} - {self.CreatedAt.strftime('%Y-%m-%d %H:%M:%S')}"