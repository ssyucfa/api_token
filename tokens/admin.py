from django.contrib import admin

from tokens.models import Token


@admin.register(Token)
class AdminToken(admin.ModelAdmin):
    pass
