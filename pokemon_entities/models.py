from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(
        blank=False,
        max_length=200,
        verbose_name='Название на русском языке'
    )
    title_en = models.CharField(
        blank=True,
        max_length=200,
        verbose_name='Название на английском языке'
    )
    title_jp = models.CharField(
        blank=True,
        max_length=200,
        verbose_name='Название на японском языке'
    )
    image = models.ImageField(
        blank=False,
        upload_to='pokemons_images',
        verbose_name='Изображение'
    )
    description = models.TextField(blank=False, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='next_evolution',
        verbose_name='Родитель'
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
        blank=False
    )
    lat = models.FloatField(verbose_name='Широта', blank=False)
    lon = models.FloatField(verbose_name='Долгота', blank=False)
    appeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время появления'
    )
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время исчезновения'
    )
    level = models.IntegerField(
        null=True,
        blank=False,
        verbose_name='Уровень'
    )
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Здоровье'
    )
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Выносливость'
    )
