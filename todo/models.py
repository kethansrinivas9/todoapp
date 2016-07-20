from __future__ import unicode_literals

from django.db import models

# Create your models here.
class addToList(models.Model):
    list_text = models.CharField(max_length=40)
    is_selected = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    def text(self):
        return self.list_text
	def is_selected(self):
		return self.is_selected
	def is_completed(self):
		return self.is_completed
	
