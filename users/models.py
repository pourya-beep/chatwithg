from django.db import models


class user(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    major = models.CharField(max_length=100,null=True, blank=True)
    grade = models.IntegerField(default=7, null=True, blank=True)
    NC = models.IntegerField(default=11111111)
    #role = models.Choices()
    
    
    
#region roles
    MG = "MANAGER"
    MO = "MODERATOR"
    ST = "STUDENT"
    
    ROLE_IN_SCHOOL = {
         "MG": "MANAGER",
         "MO": "MODERATOR",
         "ST": "STUDENT",
    #Should I add a role for us?>> I mean guys who do these...
    }
    role_IN_SCHOOL = [
    ("MG", "MANAGER"),
    ("MO", "MODERATOR"),
    ("ST", "STUDENT"),
    ]
    
    role_in_school = models.CharField(
        max_length=100,
        choices=role_IN_SCHOOL,
        default=ST,
    )
    #endregion
    
    
    
    
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}  in grade {self.grade} in major {self.major}'
    
    class Meta:
        db_table = 'all_users'
        