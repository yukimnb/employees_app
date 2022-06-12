from django.db import models


class Employee(models.Model):
    """従業員の個人データモデル"""

    gender_choices = [
        ("", "選択してください"),
        ("男性", "男性"),
        ("女性", "女性"),
    ]

    post_choices = [
        ("", "選択してください"),
        ("スタッフ", "スタッフ"),
        ("副院長", "副院長"),
        ("院長", "院長"),
        ("リーダー", "リーダー"),
        ("スーパーバイザー", "スーパーバイザー"),
        ("エリアマネージャー", "エリアマネージャー"),
        ("取締役/副社長", "取締役/副社長"),
        ("代表取締役/社長", "代表取締役/社長"),
        ("代表取締役/会長", "代表取締役/会長"),
    ]

    age_choices = [
        ("", "選択してください"),
    ]
    for i in range(1, 60):
        age_choices.append((i, i))

    team_choices = [
        ("", "選択してください"),
    ]
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        team_choices.append((char, char))

    name = models.CharField(verbose_name="名前", max_length=30)
    sub_name = models.CharField(verbose_name="フリガナ", max_length=30, blank=True, null=True)
    post = models.CharField(
        verbose_name="役職", max_length=30, blank=True, null=True, choices=post_choices
    )
    gender = models.CharField(
        verbose_name="性別", max_length=10, blank=True, null=True, choices=gender_choices
    )
    age = models.IntegerField(
        verbose_name="年齢", blank=True, null=True, choices=age_choices
    )
    birthday = models.DateField(verbose_name="生年月日", blank=True, null=True)
    address = models.CharField(verbose_name="住所", max_length=100, blank=True, null=True)
    phone = models.CharField(verbose_name="携帯番号", max_length=30, blank=True, null=True)
    assignment = models.CharField(verbose_name="配属先", max_length=100, blank=True, null=True)
    team = models.CharField(
        verbose_name="TEAM", max_length=10, blank=True, null=True, choices=team_choices
    )
    license = models.TextField(verbose_name="所持資格", blank=True, null=True)
    experience = models.IntegerField(verbose_name="経験年数", blank=True, null=True)
    joined_date = models.DateField(verbose_name="入社日")
    retired_date = models.DateField(verbose_name="退社日", blank=True, null=True)
    evaluation = models.TextField(verbose_name="人事評価", blank=True, null=True)
    photo = models.ImageField(verbose_name="写真", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        verbose_name_plural = "従業員"

    def __str__(self):
        return self.name
