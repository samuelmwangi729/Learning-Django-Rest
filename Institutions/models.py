from django.db import models

class InstitutionStatus:
    ACTIVE="active"
    DELETED="deleted"
    SUSPENDED="suspended"


    choices = (
        (ACTIVE,"active"),
        (DELETED,"deleted"),
        (SUSPENDED,"SUSPENDED"),
    )

class Institution(models.Model):
    institution_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    institution_status = models.CharField(max_length=15,choices=InstitutionStatus.choices,default=InstitutionStatus.ACTIVE)

    def __str__(self):
        return self.institution_name