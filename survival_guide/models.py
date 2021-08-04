from django.db import models
from django.db.models.deletion import RESTRICT
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey

class Section(Page):
    content = RichTextField(blank=False)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.RESTRICT)
    image_credit = models.CharField(blank=True, max_length=250)
    image_caption = models.CharField(blank=True, max_length=500)

    content_panels = Page.content_panels + [FieldPanel('content', classname='full'), ImageChooserPanel('image'), FieldPanel('image_credit'), FieldPanel('image_caption')]

    search_fields = Page.search_fields + [
        index.SearchField('content')
    ]

    pass
