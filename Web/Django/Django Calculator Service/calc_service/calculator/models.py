from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.

class Operation(models.Model):
    """docstring"""

    OPERATION_CHOICES = (
        ('SUM', '+'),
        ('SUB', '-'),
        ('MUL', '*'),
        ('DIV', '/'),
        ('POW', '^')
    )

    x_value = models.FloatField()
    y_value = models.FloatField()
    result = models.FloatField(editable=False, null=True)

    op = models.CharField(max_length=3,
                          choices=OPERATION_CHOICES,
                          blank=True)

    user = models.ForeignKey(User, related_name='operations', null=True)

    class Meta:
        ordering = ('-result', )

    def __str__(self):
        return self.op


# class VisitorUser(User):

#     class Meta:
#         proxy = True

#     def get_absolute_url(self):
#         return reverse({"calculator:user_detail", kwargs={"id": self.id}})