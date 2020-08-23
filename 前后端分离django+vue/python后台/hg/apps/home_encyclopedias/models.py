from django.db import models


class HomeEncyclopedias(models.Model):
    problem = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        help_text="问题(不超过20个字符)",
        verbose_name="问题"
    )
    answer = models.TextField(
        null=False,
        blank=False,
        help_text="答案",
        verbose_name="答案"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        null=False,
        help_text="创建时间",
        verbose_name="创建时间",
    )

    class Meta:
        verbose_name = "居家百科问答"
        verbose_name_plural = "居家百科问答"
        ordering = ['-create_time']

    def __str__(self):
        return self.problem
