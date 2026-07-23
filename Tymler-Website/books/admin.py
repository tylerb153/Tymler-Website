from django.contrib import admin, messages
from .models import Book, Link
from django.utils.translation import ngettext
from django.db.models import Case, When, BooleanField

# Register your models here.
class LinkInline(admin.TabularInline):
    model = Link
    extra = 0

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'releaseDate', 'featured']
    list_filter = ['featured', 'author']
    search_fields = ['title', 'author']
    actions = ['toggleFeatured']
    inlines = [LinkInline]

    @admin.action(description="Toggle Featured")
    def toggleFeatured(self, request, queryset):
        amountUpdated = queryset.update(
            featured=Case(
                When(featured=True, then=False),
                When(featured=False, then=True),
                output_field=BooleanField()
            ))

        self.message_user(
            request,
            ngettext(
                '%d Book accepted successfully.',
                '%d Books accepted successfully.',
                amountUpdated
            )
            % amountUpdated,
            messages.SUCCESS
        )


@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    list_display = ['__str__', 'book', 'service']
    list_filter = ['service', 'book']
    search_fields = ['service', 'book']
