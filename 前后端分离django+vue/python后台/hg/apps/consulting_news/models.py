from django.db import models


class ConsultingNews(models.Model):
    release_time = models.DateTimeField(
        verbose_name="发布时间",
        auto_now_add=True,
        null=False,
        help_text="发布时间",
    )
    title = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        help_text="标题(不超过20个字符",
        verbose_name="标题",
    )
    content = models.TextField(
        null=False,
        blank=False,
        help_text="内容",
        verbose_name="内容"
    )

    class Meta:
        verbose_name = "咨询动态"
        verbose_name_plural = "咨询动态"
        ordering = ['-release_time']

    def __str__(self):
        return self.title
