from django.db import models
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey

# Create your models here.
class Section(Page):
    content = RichTextField(blank=False)

    content_panels = Page.content_panels + [FieldPanel('content', classname='full'), InlinePanel('section_image')]

    search_fields = Page.search_fields + [
        index.SearchField('content')
    ]

    pass

class SectionImage(Orderable):
    page = ParentalKey(Section, on_delete=models.CASCADE, related_name='section_image')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE)
    credit = models.CharField(blank=True, max_length=250)
    caption = models.CharField(blank=True, max_length=500)

    panels = [ImageChooserPanel('image'), FieldPanel('credit'), FieldPanel('caption')]

    pass