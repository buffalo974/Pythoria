# v 0.5  __20/12/2014___
# buffalo
# corrections indentations, ajout des objets simple et complexe



# ============================================================================   *** CLASSE MERE ***  =======================================================

class Item():

	def __init__(self, description=''):
		self.description = "Classe mere pour obtenir les classes Vivres,Arme,Protection,Ecritures,SimpleObjet,ComplexObjet   => Attributs name , typeItem , poid, place, usure"
		self.name = None
		self.typeItem = None # ===> Vivres = aliment / boisson ; arme ; protection ; ecritures ;  materiel craftable ; artefact
		# courte lame par defaut
		
		self.poid = 1
		self.place = 1
		self.usure = 0  # armes emoussees, armures cabossees, aliments avaries...
		
		
	def get_description(self):
		return self.description

# ============================================================================____MANGER ET BOIRE_____=======================================================		
		
class Vivres(Item):

	def __init__(self, description=''):
		self.description = "Classe heritant de Item et engendrant la classe Mangeable et la classe Buveable  => Attributs typeVivres , SatieteBonus , HydratationBonus, place, UsureCoeff"
		self.typeVivres = mangeable # par defaut :risque de pourrir, compact  ; buvable = necessite recipient,peu compacte,lourd.

		self.SatieteBonus = 1 # par defaut 
		self.HydratationBonus = 1 # par defaut : la pasteque rehydrate un peu , le jambon assoife.
		self.UsureCoeff = 1 # par defaut ; les viandes auront un fort coefficient d'usure, mais sont tres rassasiantes. Les aliments sales se conservent mais donnent soif.





	def get_description(self):
		return description		

class Mangeable(Vivres):

	def __init__(self, description=''):
		self.description = description




	def get_description(self):
		return description			

class Buveable(Vivres):

	def __init__(self, description=''):
		self.description = description




	def get_description(self):
		return description		
		
# ===============================================================================____ SE BATTRE ____=================================================================================





class Arme(Item):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les armes   => Attributs typeArme , degat , portee, conso_mana, conso_ammo"
		self.typeArme = courte_lame

		# courte lame par defaut ; longue lame ; rapiere ;  lance ; javelot ; arc ; arbalete ; fouet ; fumigene ; hache ; marteau ; fleau
		self.degat = 1
		self.portee = 1

		self.conso_mana = 0
		self.conso_ammo = 0


	def get_description(self):
		return description



		
class Protection(Item):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les protections   => Attributs typeProtection , anatomie , absorption"
		self.typeProtection = maille
		# courte lame par defaut ; maille , plaque , ecailles,mythril
		self.anatomie = thorax # par defaut ; 
		# liste_equip_slot = ['tete','cou','main_D','main_G','poignet_D','poignet_G','carquoi','thorax','rachis','abdomen','jambe_D','jambe_G','pied_D','pied_G']
		self.absorption = 1 # par defaut



	def get_description(self):
		return description	


# ===============================================================================____ LE SAVOIR ET LA MAGIE ____===================================================================

# frequence_ecritures = dict(list(frequence_livre.items()) + list(frequence_grimoire.items()) + list(frequence_parchemin.items()))



class Ecriture(Item):

	def __init__(self, description=''):
		self.description = "Classe qui engendre les classes Livre, Grimoire et Parchemin  => Attributs titre"
		self.titre = None


	def get_description(self):
		return description

		
class Livre(Ecriture):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les livres    => Attributs contenu , TimeForReading , SavoirBonus"
		self.contenu = None
		self.TimeForReading = None # Nombre de tour pour livre un livre et donc augmenter son savoir, ne pas lire quand on est poursuivi par des monstres !
		self.SavoirBonus = None # Un tres bon livre est leger, rapide a lire, et offre un max de points de savoir ; le contre exemple est un annuaire telephonique. 

	def get_description(self):
		return description

		
class Grimoire(Ecriture):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les grimoires    => Attributs EcoleMagique , Sortilege , RequiredSavoir, RequiredMana"
		self.EcoleMagique = None
		self.Sortilege = None
		self.RequiredSavoir = None
		self.RequiredMana = None


	def get_description(self):
		return description

		
		
class Parchemin(Ecriture):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les parchemins    => Attributs Incantation "
		self.Incantation = None


	def get_description(self):
		return description

# ===============================================================================    Objets  simples   ===================================================================

# A FAIRE______en cours

class SimpleObjet(Item):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les objets basiques comme une clef     => Attributs ???? "
		# self.type = None



	def get_description(self):
		return description

# ===============================================================================    Objets  complexe   ===================================================================

class ComplexObjet(Item):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les objets complexes comme un tonneau rempli de poudre et de clous     => Attributs ???? "
		# self.type = None



	def get_description(self):
		return description
