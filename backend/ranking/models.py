from django.db import models

from account.models import User


class Ranking(models.Model):
    CUR_GENERATION = 11

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ranking", help_text="사용자 ID"
    )  # type: ignore
    generation = models.PositiveIntegerField(help_text="운동 기간")  # type: ignore
    week = models.PositiveIntegerField(help_text="운동 주차")  # type: ignore
    score = models.FloatField(default=0.0, help_text="운동 점수")  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 시각")  # type: ignore

    class Meta:
        db_table = "ranking"
        ordering = ["week"]
