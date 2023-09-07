from django.db import models


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} (ID: {self.product_id})"

class CustomerPreference(models.Model):
    preference_id = models.CharField(max_length=10)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.preference_id} - {self.product_id.name}"

class Orders(models.Model):
    customer_id = models.CharField(max_length=255)
    preference =models.CharField(max_length=10)
    date = models.DateField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order by {self.customer_id} - {self.preference} on {self.date}"