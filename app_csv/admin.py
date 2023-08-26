from django.contrib import admin

from app_csv.models import Stones


@admin.register(Stones)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "total")