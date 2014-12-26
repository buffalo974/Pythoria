# ============================================================================   *** CLASSE MERE ***  =======================================================

class Item():

	def __init__(self, description='',name,typeItem,poid,place,usure):
		self.description = "Classe mere pour obtenir les classes Vivres,Arme,Protection,Ecritures,SimpleObjet,ComplexObjet   => Attributs name , typeItem , poid, place, usure"
		self.name = name
		self.typeItem = typeItem # ===> Vivres = aliment / boisson ; arme ; protection ; ecritures ;  materiel craftable ; artefact
		
		
		self.poid = poid
		self.place = place
		self.usure = usure  # armes emoussees, armures cabossees, aliments avaries...
		
		
	def get_description(self):
		return self.description

# ============================================================================____MANGER ET BOIRE_____=======================================================		
		
class Vivres(Item):

	def __init__(self, description='',name,typeItem,poid,place,usure,typeVivres,SatieteBonus,HydratationBonus,UsureCoeff):
	
	
		Item.__init__(self, description='',name,typeItem,poid,place,usure)
	
	
		self.description = "Classe heritant de Item et engendrant la classe Mangeable et la classe Buveable  => Attributs typeVivres , SatieteBonus , HydratationBonus, place, UsureCoeff"
		self.typeVivres = mangeable # par defaut :risque de pourrir, compact  ; buvable = necessite recipient,peu compacte,lourd.

		self.SatieteBonus = SatieteBonus # par defaut 
		self.HydratationBonus = HydratationBonus # par defaut : la pasteque rehydrate un peu , le jambon assoife.
		self.UsureCoeff = 1 # par defaut ; les viandes auront un fort coefficient d'usure, mais sont tres rassasiantes. Les aliments sales se conservent mais donnent soif.





	def get_description(self):
		return description		


		
# ===============================================================================____ SE BATTRE ____=================================================================================





class Arme(Item):

	def __init__(self, description='',name,typeItem,poid,place,usure,degat,portee,conso_mana,conso_ammo):
	
		Item.__init__(self, description='',name,typeItem,poid,place,usure)
		self.description = "Classe pour instancier les armes   => Attributs typeArme , degat , portee, conso_mana, conso_ammo"
		self.typeArme = typeArme

		# courte lame par defaut ; longue lame ; rapiere ;  lance ; javelot ; arc ; arbalete ; fouet ; fumigene ; hache ; marteau ; fleau
		self.degat = degat
		self.portee = portee

		self.conso_mana = conso_mana
		self.conso_ammo = conso_ammo


	def get_description(self):
		return description



		
class Protection(Item):

	def __init__(self, description='',name,typeItem,poid,place,usure,typeProtection,anatomie,absorption):
	
		Item.__init__(self, description='',name,typeItem,poid,place,usure)
		self.description = "Classe pour instancier les protections   => Attributs typeProtection , anatomie , absorption"
		self.typeProtection = typeProtection
		# courte lame par defaut ; maille , plaque , ecailles,mythril
		self.anatomie = anatomie 
		# liste_equip_slot = ['tete','cou','main_D','main_G','poignet_D','poignet_G','carquoi','thorax','rachis','abdomen','jambe_D','jambe_G','pied_D','pied_G']
		self.absorption = absorption 



	def get_description(self):
		return description	


# ===============================================================================____ LE SAVOIR ET LA MAGIE ____===================================================================

# frequence_ecritures = dict(list(frequence_livre.items()) + list(frequence_grimoire.items()) + list(frequence_parchemin.items()))



class Ecriture(Item):

	def __init__(self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading):
	
	
		Item.__init__(self, description='',name,typeItem,poid,place,usure)
		self.description = "Classe qui engendre les classes Livre, Grimoire et Parchemin  => Attributs titre"
		self.titre = titre
		self.txt = txt
		self.RequiredSavoir = RequiredSavoir
		self.TimeForReading = TimeForReading # Nombre de tour pour livre un livre et donc augmenter son savoir, ne pas lire quand on est poursuivi par des monstres !
		

	def get_description(self):
		return description

		
class Livre(Ecriture):

	def __init__(self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading,SavoirBonus):
	
		Ecriture.__init__(self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading)
		self.description = "Classe pour instancier les livres    => Attributs contenu , TimeForReading , SavoirBonus"
		
		self.SavoirBonus = SavoirBonus # Un tres bon livre est leger, rapide a lire, et offre un max de points de savoir ; le contre exemple est un annuaire telephonique. 

	def get_description(self):
		return description

		
class Grimoire(Ecriture):

	def __init__(self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading,EcoleMagique,Sortilege,RequiredMana):
		Ecriture.__init__(self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading)
		self.description = "Classe pour instancier les grimoires    => Attributs EcoleMagique , Sortilege , RequiredSavoir, RequiredMana"
		self.EcoleMagique = EcoleMagique
		self.Sortilege = Sortilege
		
		self.RequiredMana = RequiredMana


	def get_description(self):
		return description

		
		
class Parchemin(Ecriture):

	def __init__self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading,Incantation):
	
		Ecriture.__init__(self, description='',name,typeItem,poid,place,usure,titre,txt,RequiredSavoir,TimeForReading)
		self.description = "Classe pour instancier les parchemins    => Attributs Incantation "
		self.Incantation = Incantation


	def get_description(self):
		return description

# ===============================================================================    Objets  simples   ===================================================================



class SimpleObjet(Item):

	def __init__(self, description=''):
		
		
		Item.__init__(self, description='',name,typeItem,poid,place,usure)
		self.description = "Classe pour instancier les objets basiques comme une clef     => Attributs ???? "
		self.clef = clef
		self.eclairage = eclairage # ex : torche
		self.outil = outil
		
		

	def get_description(self):
		return description

# ===============================================================================    Objets  complexe   ===================================================================

class ComplexObjet(Item):

	def __init__(self, description=''):
		self.description = "Classe pour instancier les objets complexes comme un tonneau rempli de poudre et de clous     => Attributs ???? "
		# reflechir



	def get_description(self):
		return description
