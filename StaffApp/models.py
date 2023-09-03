from django.db import models

class Tag(models.Model):
    INDUSTRY_CHOICES = [
        (1, "Chemistry"),
        (2, "Pharmacy"),
    ]
    industry = models.PositiveSmallIntegerField(choices=INDUSTRY_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=255, verbose_name="Име изписано на латинеца")
    email = models.EmailField(verbose_name="Служебен Email")
    CATEGORY_CHOICES = [
        (1, "AFM laboratory"),
        (2, "CF laboratory"),
        (3, "Technicians"),
        (4, "Students involved in projects"),
    ]
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)
    research_interests = models.TextField(verbose_name="Research Interests", blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    short_cv = models.TextField(blank=True, null=True, verbose_name="По желание - кратко CV")
    full_cv = models.TextField(blank=True, null=True, verbose_name="По желание - пълно научно CV/списък с публикации")
    scopus = models.URLField(blank=True, null=True)
    google_scholar = models.URLField(blank=True, null=True)
    web_of_science = models.URLField(blank=True, null=True)
    orcid = models.URLField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True, verbose_name="Друга информация, която бихте желали да има в личната Ви страница")

    def __str__(self) -> str:
        return self.name

class Research(models.Model):
    title = models.CharField(max_length=200)    
    LABORATORY_CHOICES = [
        (1, "AFM laboratory"),
        (2, "CF laboratory"),
    ]
    laboratory = models.PositiveSmallIntegerField(choices=LABORATORY_CHOICES)
    link = models.URLField(blank=True, null=True)
    writers = models.ManyToManyField(Member, related_name='written_researches')
    document = models.FileField(upload_to='research/', blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title