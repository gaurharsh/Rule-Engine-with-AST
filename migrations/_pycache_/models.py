from django.db import models
from django.contrib.postgres.fields import JSONField  # Use JSONField for PostgreSQL, or Django's JSONField for SQLite.

class Rule(models.Model):
    name = models.CharField(max_length=255)
    ast = models.JSONField()  # Stores the AST as JSON for the rule
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserData(models.Model):
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    experience = models.FloatField()

    def __str__(self):
        return f"{self.department} | Age: {self.age} | Salary: {self.salary}"
 
