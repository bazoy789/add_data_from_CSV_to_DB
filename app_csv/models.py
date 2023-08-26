from django.db import models


class ListNameStone(models.Model):

    name = models.CharField(max_length=500)


class Client(models.Model):
    username = models.CharField(max_length=100)
    spent_money = models.IntegerField(default=0)
    gems = models.ManyToManyField(ListNameStone)


class Stones(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    item = models.ForeignKey(ListNameStone, on_delete=models.CASCADE)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(null=True, blank=True)


