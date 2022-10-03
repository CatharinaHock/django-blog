from django.conf import settings
from django.db import models
from django.utils import timezone


class Language(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 200)
    text = models.TextField()
    #brief_description =  models.TextField(blank =  True, null = True)
    authors_comment = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(blank = True, null = True)
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    # add (multiple) languages
    language= models.ManyToManyField(Language, help_text= "Language(s) of text", default=Language.objects.get(name="English"))

    def publish(self):
        self.published_date = timezone.now()
        if not self.brief_description:
            self.brief_description = self.text[:500]
            if len(self.text)<500:
                self.brief_description+=". . ."
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:
        # default ordering
        ordering=["published_date"]

