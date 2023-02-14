from django.contrib import admin
from .models import Post
from .models import Choice
# Register your models here.

""" Registering two models on the admin sites.
This helps admin can post the articles and questions along with voting choices. 
"""

admin.site.register(Post)
admin.site.register(Choice)