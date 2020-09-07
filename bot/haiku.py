import json
import random

class Haiku:
	def __init__(self):
		self.words = self.get_data()

	def get_data(self):
		""" Reads in all words stored in data.json """
		with open('../data/data.json') as d:
			data = json.load(d)
		return data

	def type_1(self):
		""" Format based off "The Old Pond"	by Matsuo Basho """
		haiku_string = "The " + random.choice(self.words["adjectives"]["1"]) +" "+ random.choice(self.words["adjectives"]["2"]) +" "+ random.choice(self.words["objects"]["1"]) + "\n"
		haiku_string += "The " + random.choice(self.words["animals"]["1"]) +" "+ random.choice(self.words["actions"]["1"]) + "s into the " + random.choice(self.words["objects"]["1"]) + "\n"
		haiku_string += random.choice(self.words["onomatopoeia"]["1"]) + "! " + random.choice(self.words["adjectives"]["2"]) + " again"
		return haiku_string

	def type_2(self):
		""" Formatted after "Over the Wintry" by Natsume Sōseki """
		haiku_string = "Over the " + random.choice(self.words["adjectives"]["2"]) + "\n"
		haiku_string += random.choice(self.words["objects"]["2"]) + ", " + random.choice(self.words["objects"]["1"])+ "s " + random.choice(self.words["actions"]["1"]) + " in " + random.choice(self.words["emotions"]["1"]) + "\n"
		haiku_string += "With no " + random.choice(self.words["objects"]["2"]) + " to " + random.choice(self.words["actions"]["1"])
		return haiku_string
 
	def type_3(self):
		""" Formatted by myself """ 
		haiku_string = random.choice(self.words["animals"]["2"])+" "+random.choice(self.words["objects"]["3"])+"\n"
		haiku_string += random.choice(self.words["adjectives"]["1"])+" "+random.choice(self.words["objects"]["2"])+", "+random.choice(self.words["adjectives"]["1"])+" "+random.choice(self.words["objects"]["2"])+"- "+random.choice(self.words["actions"]["1"])+"\n"
		haiku_string += random.choice(self.words["adjectives"]["2"])+" "+random.choice(self.words["objects"]["3"])
		return haiku_string

	def generate_haiku(self):
		decider = random.random()

		if decider <= 0.1:
			return self.type_1()
		elif decider <= 0.2:
			return self.type_2()
		else:
			return self.type_3()
