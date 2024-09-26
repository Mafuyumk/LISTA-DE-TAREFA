from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Entrega", null=False, blank=False, default=timezone.now)
    finished_at = models.DateField(null=True, blank=True)  # Agora com o mesmo comportamento que deadline

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = timezone.now()
            self.save()
