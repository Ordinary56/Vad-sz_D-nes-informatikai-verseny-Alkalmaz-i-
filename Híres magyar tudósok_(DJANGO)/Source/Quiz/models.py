from django.db import models

# Create your models here.

class QuesModel(models.Model):
    '''
    Represents our model, in which case, the Quiz model
    '''
    question_title = models.CharField(max_length=100,null=True)
    option1 = models.CharField(max_length=100,null=True)
    option2 = models.CharField(max_length=100,null=True)
    option3 = models.CharField(max_length=100,null=True)
    option4 = models.CharField(max_length=100,null=True)
    option5 = models.CharField(max_length=100,null=True)
    ID = models.BigIntegerField()
    ans = models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.question_title
    
