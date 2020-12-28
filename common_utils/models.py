
from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=datetime.now(), null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        abstract=True # Set this model as Abstract

