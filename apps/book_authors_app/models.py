from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Books(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ManyToManyField(Authors, related_name = 'books')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


def __repr__(self):
        return f"<Books object: {self.id}, {self.title}>"