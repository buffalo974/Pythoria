# ============================================================================   *** CLASSE MERE ***  =======================================================

class Item():

	def __init__(self, name, poid, place, usure, description=''):
	
		self.description = "Classe mere pour obtenir les classes Vivres,Arme,Protection,Ecritures,SimpleObjet,ComplexObjet   => Attributs name , poid, place, usure"
		self.name = name
		
		
		self.poid = poid
		self.place = place
		self.usure = usure  # armes emoussees, armures cabossees, aliments avaries...
		
		
	def get_description(self):
		return self.description

# ============================================================================____MANGER ET BOIRE_____=======================================================		
		
class Vivres(Item):

	def __init__(self, name, poid, place, usure, description='', satiete_bonus, hydratation_bonus):
	
	
		super(Vivres, self).__init__(self, name, poid, place, usure, description='')	
	
		self.description = "Classe heritant de Item et engendrant la classe Mangeable et la classe Buveable  => Attributs type_vivres , satiete_bonus , hydratation_bonus, place, usure_coeff"
		
		self.satiete_bonus = satiete_bonus # par defaut 
		self.hydratation_bonus = hydratation_bonus # par defaut : la pasteque rehydrate un peu , le jambon assoife.
		

	def get_description(self):
		return self.description		

# ===============================================================================____ SE BATTRE ____=================================================================================
class Arme(Item):

	def __init__(self, name, poid, place, usure, description='', degat, portee, precision, conso_mana, conso_ammo):
	
		
		super(Arme, self).__init__(self, name, poid, place, usure, description='')
		self.description = "Classe pour instancier les armes   => Attributs typeArme , degat , portee, conso_mana, conso_ammo"
		self.typeArme = typeArme
		
		self.degat = degat
		self.portee = portee
		self.precision = precision

		self.conso_mana = conso_mana
		self.conso_ammo = conso_ammo


	def get_description(self):
		return self.description

		
class Protection(Item):

	def __init__(self, name, poid, place, usure, description='', anatomie, absorption, malus_dxt):
	
		super(Protection, self).__init__(self, name, poid, place, usure, description='')
		
		self.description = "Classe pour instancier les protections   => Attributs typeProtection , anatomie , absorption"
		
		self.anatomie = anatomie 
		# liste_equip_slot = ['tete','cou','main_D','main_G','poignet_D','poignet_G','carquoi','thorax','rachis','abdomen','jambe_D','jambe_G','pied_D','pied_G']
		self.absorption = absorption 
		self.malus_dxt = malus_dxt

	def get_description(self):
		return self.description	


# ===============================================================================____ LE SAVOIR ET LA MAGIE ____===================================================================

class Ecriture(Item):

	def __init__(self, name, poid, place, usure, description='', required_savoir, time_for_reading):
	
	
		super(Ecriture, self).__init__(self, name, poid, place, usure, description='')
		self.description = "Classe qui engendre les classes Livre, Grimoire et Parchemin  => Attributs titre"
		
		self.required_savoir = required_savoir
		self.time_for_reading = time_for_reading # Nombre de tour pour livre un livre et donc augmenter son savoir, ne pas lire quand on est poursuivi par des monstres !
		
	def get_description(self):
		return self.description

		
class Livre(Ecriture):

	def __init__(self, name, poid, place, usure, description='', required_savoir, time_for_reading, savoir_bonus):
	
		super(Livre, self).__init__(self, name, poid, place, usure, description='', required_savoir, time_for_reading)
		self.description = "Classe pour instancier les livres    => Attributs contenu , time_for_reading , savoir_bonus"
		
		self.savoir_bonus = savoir_bonus # Un tres bon livre est leger, rapide a lire, et offre un max de points de savoir ; le contre exemple est un annuaire telephonique. 

	def get_description(self):
		return self.description

		
class Grimoire(Ecriture):

	def __init__(self, name, poid, place, usure, description='', required_savoir, time_for_reading, ecole_magique, sortilege, required_mana):
	
		super(Grimoire, self).__init__(self, name, poid, place, usure, description='', required_savoir, time_for_reading)
		
		self.description = "Classe pour instancier les grimoires    => Attributs ecole_magique , sortilege , required_savoir, required_mana"
		self.ecole_magique = ecole_magique
		self.sortilege = sortilege
		
		self.required_mana = required_mana


	def get_description(self):
		return self.description
		
		
class Parchemin(Ecriture):

	def __init__self(self, name, poid, place, usure, description='', required_savoir, time_for_reading, Incantation):
	
		super(Parchemin, self).__init__(self, name, poid, place, usure, description='', required_savoir, time_for_reading)
		self.description = "Classe pour instancier les parchemins    => Attributs Incantation "
		self.Incantation = Incantation

	def get_description(self):
		return self.description

# ===============================================================================    Objets  simples   ===================================================================
class SimpleObjet(Item):

	def __init__(self, name, poid, place, usure, description='', clef, eclairage, outil):
		
		
		super(SimpleObjet, self).__init__(self, description='', name, poid, place, usure)
		self.description = "Classe pour instancier les objets basiques comme une clef     => Attributs ???? "
		self.clef = clef
		self.eclairage = eclairage # ex : torche
		self.outil = outil
		

	def get_description(self):
		return self.description

