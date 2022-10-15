from django.conf import settings
from django.db import models
from django.utils import timezone



# no need for this anymore
class Language(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name




class Tag(models.Model):
    # languages are also tags now
    COLOR_CHOICES=(
        ("lb","lightblue"),
        ("pb","pastelblue"),
        ("pp","pastelpurple"),
        ("sg", "seagreen"),
    )
    TYPE_CHOICES=(
        ("l", "language tag"),
        ("o", "other"),
    )
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=2, choices=COLOR_CHOICES, default="pb")
    type = models.CharField(max_length=1, choices = TYPE_CHOICES, default="o")

    def __str__(self):
        return self.name

eng = Tag(name="English",color="pp", type="l")

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 200)
    text = models.TextField()
    brief_description =  models.TextField(blank =  True, null = True)
    authors_comment = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(blank = True, null = True)
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    # add (multiple) tags
    tags= models.ManyToManyField("Tag", related_name = "tags")

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
        ordering=["-published_date"]

