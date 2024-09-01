from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
    
    def save(self, *args, **kwargs):
        # Ensure created_by is set only when the object is created
        if not self.pk and not self.created_by:
            self.created_by = self._created_by_full_name
        super(Client, self).save(*args, **kwargs)
    
    
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name