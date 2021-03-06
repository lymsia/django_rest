import datetime
from django.db import models


class History(models.Model):

    purchaser = models.ForeignKey('Purchaser', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'history'

    def __str__(self):
        return 'Purchaser: {}, Product: {}, Date: {})'.format(
            self.purchaser,
            self.product,
            self.created_at.date()
        )

