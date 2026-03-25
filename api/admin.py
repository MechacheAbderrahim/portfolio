from django.contrib import admin
from .models import (
    UserProfile,
    Education,
    Technology,
    Skill,
    PortfolioItem,
    Language,
    Publication,
    ContactMessage,
)

admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Technology)
admin.site.register(Skill)
admin.site.register(PortfolioItem)
admin.site.register(Language)
admin.site.register(Publication)
admin.site.register(ContactMessage)