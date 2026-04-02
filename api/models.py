from django.db import models

# ------------------------
# USER PROFILE
# ------------------------
class UserProfile(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    google_scholar_url = models.URLField(blank=True)
    cv_url = models.URLField(blank=True)
    photo_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


# ------------------------
# EDUCATION
# ------------------------
class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    field = models.CharField(max_length=255, blank=True)
    institution = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    rank_info = models.CharField(max_length=255, blank=True)
    order_index = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ------------------------
# TECHNOLOGY
# ------------------------
class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)
    icon_url = models.URLField(blank=True)

    display = models.BooleanField(default=False)
    order_index = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ------------------------
# SKILL
# ------------------------
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)

    display = models.BooleanField(default=False)
    order_index = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ------------------------
# PORTFOLIO ITEM
# ------------------------
class PortfolioItem(models.Model):
    TYPE_CHOICES = [
        ('research', 'Research'),
        ('teaching', 'Teaching'),
        ('industry', 'Industry'),
        ('academic', 'Academic'),
        ('personal', 'Personal'),
    ]

    EMPLOYMENT_CHOICES = [
        ('phd', 'PhD'),
        ('internship', 'Internship'),
        ('fixed_term', 'Fixed Term'),
        ('permanent', 'Permanent'),
        ('freelance', 'Freelance'),
        ('temporary', 'Temporary'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_CHOICES, blank=True)

    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    image_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)

    highlight = models.BooleanField(default=False)
    order_index = models.IntegerField(default=0)

    technologies = models.ManyToManyField(Technology, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-order_index']

    def __str__(self):
        return self.title


# ------------------------
# LANGUAGE
# ------------------------
class Language(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True)
    order_index = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ------------------------
# PUBLICATION
# ------------------------
class Publication(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    year = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, blank=True)

    order_index = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ------------------------
# CONTACT MESSAGE
# ------------------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)