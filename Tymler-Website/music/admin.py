from django.contrib import admin, messages
from .models import Song, Link
from django.utils.translation import ngettext
from django.db.models import Case, When, BooleanField

class LinkInline(admin.TabularInline):
    model = Link
    extra = 0

@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    list_display = ['title', 'artist', 'genre', 'releaseDate', 'featured']
    list_filter = ['featured', 'genre', 'artist']
    search_fields = ['title', 'artist', 'genre']
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
                '%d song accepted successfully.',
                '%d songs accepted successfully.',
                amountUpdated
            )
            % amountUpdated,
            messages.SUCCESS
        )


@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    list_display = ['__str__', 'song', 'service']
    list_filter = ['service', 'song']
    search_fields = ['service', 'song']
