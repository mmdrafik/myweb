from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=25)
    group_permission = models.CharField(max_length=50)
    def __str__(self):
        return self.group_name

class Member(models.Model):
    group = models.ForeignKey(Group)
    member_name = models.CharField(max_length=30)
    def __str__(self):
        return self.member_name
