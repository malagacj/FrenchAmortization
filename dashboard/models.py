from django.db import models
from finance.french_amortization import amortization_table


class Simulation(models.Model):
    capitalization = models.FloatField()
    interest = models.FloatField()
    periods = models.IntegerField()

    def __str__(self):
        return f'{self.capitalization} at {self.interest} for {self.periods} periods'

    def french_amortization(self):
        return amortization_table(
            self.capitalization,
            self.interest,
            self.periods
        )
