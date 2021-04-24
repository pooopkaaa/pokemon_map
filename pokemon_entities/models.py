from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(blank=True, max_length=200)
    title_en = models.CharField(blank=True, max_length=200)
    title_jp = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='pokemons_images')
    description = models.TextField(blank=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='next_evolution')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)