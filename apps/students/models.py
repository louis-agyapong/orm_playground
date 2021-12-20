from django.db import models
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    age = models.IntegerField(_("Age"))
    class_room = models.IntegerField(_("Class Room"))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_("Teacher"))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
