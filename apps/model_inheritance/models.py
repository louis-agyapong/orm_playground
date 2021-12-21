from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseItem(models.Model):
    """Abstract base class for all models."""

    title = models.CharField(_("title"), max_length=100)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ["title"]


class ItemA(BaseItem):
    content = models.TextField(_("content"))

    class Meta(BaseItem.Meta):
        ordering = ["-created_at"]


class ItemB(BaseItem):
    file = models.FileField(_("file"), upload_to="files")


class ItemC(BaseItem):
    image = models.ImageField(_("image"), upload_to="images")


class ItemD(BaseItem):
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
