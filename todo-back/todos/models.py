from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 유저는 커스텀 유저를 사용 
# (default 유저를 사용하더라도 django 에서는 *강력히* 커스텀 유저를  사용하라고 권장)
class User(AbstractUser):
    pass

class Todo(models.Model):
    # user.related_name.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
