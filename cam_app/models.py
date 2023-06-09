from django.db import models
from django.shortcuts import render

from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

import sqlite3, datetime, os

# Create your models here.
class VideoPage(Page):
    """Video Page."""

    template = "cam_app/video2.html"

    max_count = 2

    name_title = models.CharField(max_length=100, blank=True, null=True)
    name_subtitle = RichTextField(features=["bold", "italic"], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("name_title"),
                FieldPanel("name_subtitle"),

            ],
            heading="Page Options",
        ),
    ]
    
    def serve(self, request):
        return  render(request, "cam_app/video2.html", {'page': self})
