from django.conf import settings
from django.db import models
from django.utils import timezone


class Language(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

def eng():
    return [Language.objects.get(name="English")]

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 200)
    text = models.TextField()
    brief_description =  models.TextField(blank =  True, null = True)
    authors_comment = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(blank = True, null = True)
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    # add (multiple) languages
    language= models.ManyToManyField(Language, blank= True, default=eng)

    def create_brief_description(self):
        print("calling create_brief_description")
        if self.brief_desription == None:
            self.brief_description = self.text[:500]
            print("created new description!")
            if len(self.text)<500 and not self.brief_description[-1] in [".", "?", "!"]:
                self.brief_description+=". . ."

    def publish(self):
        self.published_date = timezone.now()
        self.create_brief_description()
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:
        # default ordering
        ordering=["published_date"]

