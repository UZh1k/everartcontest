from django.db import models
import random, string


class Exhibition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    clients_visited = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['id']

    def generate_code(self):
        if self.code is None:
            letters_and_digits = string.ascii_letters + string.digits
            result_str = ''.join((random.choice(letters_and_digits) for i in range(10)))
            self.code = result_str

    def __str__(self):
        if not self.title:
            return self.id
        else:
            return str(self.id) + " " + self.title


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client_ip = models.CharField(max_length=100, blank=True, null=True)
    exhibitions = models.ManyToManyField(Exhibition, blank=True, related_name="clients")
    is_participant = models.BooleanField(blank=True, null=True, default=False)
    special_code = models.CharField(max_length=100, blank=True, null=True)
    exhibitions_visited = models.IntegerField(blank=True, null=True)

    def generate_special_code(self):
        if self.special_code is None:
            letters_and_digits = string.ascii_letters + string.digits
            result_str = ''.join((random.choice(letters_and_digits) for i in range(10)))
            self.special_code = result_str

    def __str__(self):
        return str(self.id)

# Create your models here.
