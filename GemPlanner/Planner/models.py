from django.db import models

# Create your models here.
class GemQueries(models.Model):
    prompt=models.TextField()
    func=models.SmallIntegerField()

    def __str__(self):
        return self.prompt

class GemPlans():
    name=models.CharField(max_length=300)
    date=models.DateTimeField()
    is_completed=models.BooleanField()

    def __str__(self) -> str:
        return self.name

