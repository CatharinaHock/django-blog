from django.conf import settings
from django.db import models
from django.utils import timezone, safestring



# no need for this anymore
class Language(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Tag(models.Model):
    # languages are also tags now
    STYLE_CHOICES=(
        ("lb","lightblue"),
        ("pb","pastelblue"),
        ("pp","pastelpurple"),
        ("sg", "seagreen"),
        ("ds", "dark sky"),
        ("nb", "navy blue"),
        ("lg", "light grey"),
        ("dd", "delve deeper special"),
        ("sv", "silver"),
        ("gd", "gold"),
    )
    TYPE_CHOICES=(
        ("l", "language tag"),
        ("o", "other"),
    )
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=2, choices=STYLE_CHOICES, default="pb")
    type = models.CharField(max_length=1, choices = TYPE_CHOICES, default="o")

    def __str__(self):
        return self.name

eng = Tag(name="English",style="pp", type="l")

class Post(models.Model):
    TITLE_ALIGN_CHOICES = (
        ("c", "align-center"),
        ("t", "algin-top"),
        ("b", "align-bottom"),
    )

    TITLE_COLOR_CHOICES = (
        ("wh", "white"),
        ("lb","lightblue"),
        ("pb","pastelblue"),
        ("pp","pastelpurple"),
        ("pr","purple"),
        ("sg", "seagreen"),
        ("bl", "inkblack"),
    )

    TITLE_BACKGROUND_CHOICES = (
        ("no", "none"),
        ("gr", "grey"),
        ("bl", "black"),
        ("wh", "white"),
        ("wt", "white-transparent"),
    )

    BACKGROUND_COLOR_CHOICES = (
        ("rbl", "delve deeper rainbow  to bottom left"),
        ("rbr", "delve deeper rainbow  to bottom right"),
        ("gd", "golden"),
        ("wh", "white"),
        ("bl","black"),
        ("lb","lightblue"),
        ("pb","pastelblue"),
        ("pp","pastelpurple"),
        ("pr", "purple"),
        ("sg", "seagreen"),
    )

    POST_TYPE_CHOICES = (
        ("tex", "text-based post"),
        ("pic", "picture-based post"),
        ("art", "artwork"),
        
    )
    
    PICTURE_ORIENTATION_CHOICES = (
        ("h", "horizontal"),
        ("v", "vertical"),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 200)
    text = models.TextField()
    brief_description =  models.TextField(blank =  True, null = True)
    authors_comment = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(blank = True, null = True, upload_to="pictures/")
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    
    title_align = models.CharField(max_length=1, choices=TITLE_ALIGN_CHOICES, default = "c")
    title_color = models.CharField(max_length=2, choices=TITLE_COLOR_CHOICES, default = "bl")
    title_background = models.CharField(max_length=2, choices=TITLE_BACKGROUND_CHOICES, default = "no")

    show_whole_thumbnail = models.BooleanField(default = False)
    background_color = models.CharField(max_length = 3, choices= BACKGROUND_COLOR_CHOICES, default="rbl")
    show_title_in_header = models.BooleanField(default=True)
    show_title_below_header = models.BooleanField(default = True)

    post_type = models.CharField(max_length=3, choices = POST_TYPE_CHOICES, default="tex")
    picture_orientation = models.CharField(max_length = 1, choices = PICTURE_ORIENTATION_CHOICES, default = "v")

    # add (multiple) tags
    tags= models.ManyToManyField("Tag", related_name = "tags")

    def create_brief_description(self):
        print("calling create_brief_description")
        if not self.brief_description:
            self.brief_description = self.text[:500]
            print("created new description!")
            if len(self.text)<500 and not self.brief_description[-1] in [".", "?", "!"]:
                self.brief_description+=". . ."

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:
        # default ordering
        ordering=["-published_date"]

"""
class PicturePost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title =  models.CharField(max_length = 200)
    text = models.TextField()
    picture = models.ImageField(blank = True, null = True, upload_to="pictures/")
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
"""