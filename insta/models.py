from django.db import models

class Gamsung(models.Model):
    subject = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # JAVA 의 toString 과 유사한 __str__
    def __str__(self):
        return f"[{self.id}]{self.subject}"

