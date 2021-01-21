from django.contrib import admin

from .models import Guild, Plant, PlantInGuild, Animal, AnimalInGuild, FunctionalGuild, Implantation, SimplifiedGuild

admin.site.register(Guild)
admin.site.register(Plant)
admin.site.register(PlantInGuild)
admin.site.register(Animal)
admin.site.register(AnimalInGuild)
admin.site.register(FunctionalGuild)
admin.site.register(Implantation)
admin.site.register(SimplifiedGuild)
