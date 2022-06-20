from django.db import models


class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    max_price = models.FloatField()
    min_price = models.FloatField()

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    max_price = models.FloatField()
    min_price = models.FloatField()


class Toppings(models.Model):
    name = models.CharField(max_length=64)


class Subs(models.Model):
    name = models.CharField(max_length=64)
    max_price = models.FloatField()
    min_price = models.FloatField()


class SubsExtras(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()


class Pasta(models.Model):
    name = models.CharField(max_length=64)
    max_price = models.FloatField()
    min_price = models.FloatField()

class Salads(models.Model):
    name = models.CharField(max_length=64)
    max_price = models.FloatField()
    min_price = models.FloatField()


class DinnerPlatters(models.Model):
    name = models.CharField(max_length=64)
    max_price = models.FloatField()
    min_price = models.FloatField()


class OrderList(models.Model):
    name = models.CharField(max_length=64)
    pizzaname = models.CharField(max_length=1000)
    count = models.IntegerField()
    status = models.CharField(max_length=64)
    total = models.FloatField()


class Cart(models.Model):
    name = models.CharField(max_length=64)
    details = models.CharField(max_length=1000)
    price = models.FloatField()