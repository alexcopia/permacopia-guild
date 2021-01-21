from django.db import models

class Plant(models.Model):
	"""	Plant modelize any plants from the naturalist master data
		More precisely, it's the plantae kingdom taxonomic rank of the biological classification
	"""

	#Should be at least the binomial name (Genus species)
	botanical_name = models.CharField(max_length=254)
	common_names = models.CharField(max_length=1024,blank=True)
	miniature_uri = models.CharField(max_length=8000,blank=True)

	def __str__(self):
		return self.botanical_name

class PlantInGuild(models.Model):
	"""	Detail the relationship between a plant and its guild
	"""

	#These might be parameters (not hardcoded)
	ECOLOGICAL_SERVICES = (
		('Biodiversity','Improve biodiversity'),
	)
	#For SUPPORT guild
	PLANT_USE = (
		('Feeders','Feeders: Feed humans or animals'),
		('Fertilisers', 'Fertilisers: Improve the fertility of the soil'),
		('Diggers', 'Diggers: Improve soil strucutre'),
		('Mulchers', 'Mulchers: Cover bare soil'),
		('Climbers', 'Climbers: Grow up on supports'),
		('Supporters', 'Supporters: Provide framework for climbers'),
		('Protectors', 'Protectors: Protect plants from pest attack, disease or competition'),
		('Attractors', 'Attractors: Attract beneficial species into the guild'),
	)
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	details = models.TextField(blank=True)
	ecological_services = models.CharField(
		choices=ECOLOGICAL_SERVICES,
		blank=True,
		max_length=12,
	)
	use = models.CharField(
		choices=PLANT_USE,
		blank=True,
		max_length=12,
	)
	#miniature = models.ImageField()

	def __str__(self):
		return str(self.plant) + ":" + str(self.use) + "-" + str(self.ecological_services)


class Animal(models.Model):
	"""	Animal modelize any animals from the naturalist master data
		More precisely, it's the animalia kingdom taxonomic rank of the biological classification
	"""

	#Should be at least the binomial name (Genus species)
	scientific_name = models.CharField(max_length=254,blank=False,null=True)
	common_names = models.CharField(max_length=1024,blank=True)
	miniature_uri = models.CharField(max_length=8000,blank=True) #Should be externalized
	ECOLOGICAL_SERVICES = (

	)
	ANIMAL_USE = (

	)

	def __str__(self):
		return self.scientific_name

class AnimalInGuild(models.Model):
	pass

class SimplifiedGuild(models.Model):
	"""	A simplified guild is a set of plant that can be used together without explanation.
		The purpose is to easily and quickly gathered data from users.

		Should be used only with a dedicated Implantation class ?
	"""

	plants = models.ManyToManyField(Plant, related_name="plants")

class Guild(models.Model):
	"""	An abstract set of plants
	"""

	#This might be parameters (not hardcoded)
	TYPE_OF_GUILD = (
		('SUPPORT', 'Mutual support guild'),
		('PARTITIONING','Resource partitioning guild'),
		('ESTABLISHMENT','Establishment guild'),
		('MATURE', 'Mature guild'),
		('FUNCTIONAL','Functional guild??'), #Might (should?) be implemented with FunctionalGuild
	)

	name = models.CharField(max_length=254)
	main_plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	# Simplify adding plants for users
	undetermined_layer = models.ManyToManyField(PlantInGuild, related_name="undetermined", blank=True)
	# Layers
	canopy_layer = models.ManyToManyField(PlantInGuild, related_name="canopy", blank=True)
	tree_layer = models.ManyToManyField(PlantInGuild, related_name="tree", blank=True)
	shrub_layer = models.ManyToManyField(PlantInGuild, related_name="shrub", blank=True)
	herb_layer = models.ManyToManyField(PlantInGuild, related_name="herb", blank=True)
	ground_cover_layer = models.ManyToManyField(PlantInGuild, related_name="ground_cover", blank=True)
	climbing_layer = models.ManyToManyField(PlantInGuild, related_name="climbing", blank=True)
	root_layer = models.ManyToManyField(PlantInGuild, related_name="root", blank=True)
	aquatic_layer = models.ManyToManyField(PlantInGuild, related_name="aquatic", blank=True)
	#animals = models.ManyToManyField(AnimalInGuild, blank=True)
	#aquatic_layer => hydrophytes_layer + helophytes_layer ?
	#mycelian_layer?

	def __str__(self):
		return self.name + ": " + self.main_plant


class FunctionalGuild(models.Model):
	"""	The 'community function guild' from 'Edible forest garden'
	"""

	name = models.CharField(max_length=254)
	description = models.CharField(max_length=254)
	plants = models.ManyToManyField(Plant)

	def __str__(self):
		return self.name

class Implantation(models.Model):
	"""	The real geocoded guild
	"""

	guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
	#GPS coordinates
	lat = models.FloatField()
	lng = models.FloatField()

	# Should mentionned the plants that are actually planted
	# Might be implemanted in another structure
	# Might be timestamped
	# TODO

	def __str__(self):
		return self.guild.name + " - lat:" + self.lat + ", lng:" + self.lng


class Biotope(models.Model):
	# Not yet for the moment
	pass