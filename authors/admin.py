from cProfile import Profile

from django.contrib import admin

from authors.models import Profile  # noqa: F811


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
