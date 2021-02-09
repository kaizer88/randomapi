from django.db import models

# Create your models here.


class Log(models.Model):

    _from = models.CharField(max_length=255, null=False, blank=False)
    to = models.CharField(max_length=255, null=False, blank=False)
    # q = models.IntegerField(null=False, blank=False)
    ans = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(null=False,auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self._from, self.to)
