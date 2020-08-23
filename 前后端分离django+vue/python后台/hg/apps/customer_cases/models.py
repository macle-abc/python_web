from django.db import models


class CustomerCases(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="模型名(不超过30个字符)",
        null=False,
        blank=False,
        db_index=True,
        verbose_name="模型名",
    )

    class Meta:
        verbose_name = "模型"
        verbose_name_plural = "模型"
        ordering = ['-name']

    def __str__(self):
        return self.name


class CustomerCasesImages(models.Model):
    image = models.ImageField(
        verbose_name="模型详情图",
        help_text="模型详情图",
        upload_to="images/detail/%Y/%m/%d",
    )
    case_id = models.ForeignKey(
        CustomerCases,
        related_name="customer_cases_images",
        on_delete=models.CASCADE,
        verbose_name="模型id",
        help_text="模型id",
    )

    class Meta:
        verbose_name = "模型详情图"
        verbose_name_plural = "模型详情图"
        ordering = ['case_id']


class CustomerCasesVideos(models.Model):
    case_id = models.ForeignKey(
        CustomerCases,
        related_name="customer_cases_videos",
        on_delete=models.CASCADE,
        verbose_name="模型id",
        help_text="模型id",
    )
    video_effect = models.FileField(
        upload_to="customer_cases/videos/%Y/%m/%d",
        null=False,
        blank=False,
        help_text="模型视频",
        verbose_name="模型视频",
    )

    class Meta:
        verbose_name = "模型效果视频"
        verbose_name_plural = "模型效果视频"
        ordering = ['case_id']
