import pygame
from pygame.locals import *
from sanalista import *
import glob
import pyganim
import sys
import random

#Muutama globaali muuttuja lassin iloksi
#Luodaan "ruutu", jolle piirretaan size kokoon
#Asetetaan ruudun koko
#Muumi eli nainen baarissa
class Moomin:
    def __init__(self,posx,posy):
        self.time = 0
        self.state = 1
        self.x = posx
        self.y = posy 
        self.kuvat = glob.glob("img/nursey*.png")
        self.kuvat.sort()
        for i in range(len(self.kuvat)):
            self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
            self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
        self.img = self.kuvat[0]

        self.stand = pyganim.PygAnimation([(self.kuvat[0],0.2)])
        self.stand.play()
        
    def update(self,screen):

        self.img = self.kuvat[0]
        screen.blit(self.img,[self.x,self.y])

class Polizei:
    def __init__(self,posx,posy):
        self.time = 0
        self.state = 1
        self.x = posx
        self.y = posy 
        self.kuvat = glob.glob("img/thepolize*.png")
        self.kuvat.sort()
        for i in range(len(self.kuvat)):
            self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
            self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
        self.img = self.kuvat[0]

        self.stand = pyganim.PygAnimation([(self.kuvat[0],0.2)])
        self.stand.play()
        
    def update(self,screen):

        self.img = self.kuvat[0]
        screen.blit(self.img,[self.x,self.y])
    
class Valot:
    def __init__(self, posx, posy):
        self.state = 1
        self.x = posx
        self.y = posy
        self.kuvat = glob.glob("img/club_jate*.png")
        self.kuvat.sort()
        self.random_kuva = 0
        for i in range(len(self.kuvat)):
            self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
            self.kuvat[i] = pygame.transform.scale(self.img,[860,640])
        self.img = self.kuvat[0]

        self.bouncer = pyganim.PygAnimation([(self.kuvat[0],1)])
        self.bouncer.play()

    def update(self, screen, update_pic):
        screen.blit(self.img, [self.x, self.y])
        if update_pic:
            self.random_kuva = random.randint(0,len(self.kuvat)-1)
            self.img = self.kuvat[self.random_kuva]
            screen.blit(self.img, [self.x, self.y])
class Effect_holder:
    def __init__(self, posx, posy):
        self.state = 1
        self.x = posx
        self.y = posy
        self.kuvat = glob.glob("img/effect*.png")
        self.kuvat.sort()
        self.random_kuva = 0
        for i in range(len(self.kuvat)):
            self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
            self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
        self.img = self.kuvat[0]

        self.bouncer = pyganim.PygAnimation([(self.kuvat[0],1)])
        self.bouncer.play()

    def update(self, screen, update_pic):
        screen.blit(self.img, [self.x, self.y])
        if update_pic:
            self.x = 200+ random.randint(0,100)
            self.y = 200+ random.randint(0,100)
            self.random_kuva = random.randint(0,len(self.kuvat)-1)
            self.img = self.kuvat[self.random_kuva]
            screen.blit(self.img, [self.x, self.y])

class Hearts:
	def __init__(self,x,y):
		self.time = 0.5
		self.x = x
		self.y = y
		self.kuvat = glob.glob("img/heart*.png")
		self.kuvat.sort()
		for i in range(len(self.kuvat)):
			self.img = pygame.image.load(self.kuvat[i]).convert()
		self.img = pyganim.PygAnimation([(self.kuvat[0],0.1+self.time),
										(self.kuvat[1],0.05),
										(self.kuvat[2],0.05),
										(self.kuvat[3],0.05),
										(self.kuvat[4],0.05),
										(self.kuvat[3],0.05),
										(self.kuvat[2],0.05),
										(self.kuvat[1],0.05)])
	def update(self,screen):
		self.img.blit(screen,[self.x,self.y])

class Typy:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.kuvat = glob.glob("img/foxylady*.png")
		self.kuvat.sort()
		for i in range(len(self.kuvat)):
			self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
			self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
		self.img = pyganim.PygAnimation([(self.kuvat[0],1.0),(self.kuvat[1],1.5)])
	def update(self,screen):
		self.img.blit(screen,[self.x,self.y])

class Friendo:
	def __init__(self,posx,posy):
		self.x = posx
		self.y = posy
		self.kuvat = glob.glob("img/friendo*.png")
		self.kuvat.sort()
		for i in range(len(self.kuvat)):
			self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
			self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
		self.img = pyganim.PygAnimation([(self.kuvat[2],1.0), (self.kuvat[3], 0.2)])
	def update(self,screen):
		self.img.blit(screen,[self.x,self.y])
	

class Player:
#
	def __init__(self,posx,posy):
		self.pisteet = 0
		self.nekkid = False
		self.state = 1
		self.x = posx
		self.y = posy 
		self.kuvat = glob.glob("img/char*.png")
		self.kuvat.sort()
		for i in range(len(self.kuvat)):
			self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
			self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
		self.img = self.kuvat[0]
	
		self.dance = pyganim.PygAnimation([(self.kuvat[0],0.2), (self.kuvat[2],0.2)])
		self.dance.play()
		self.wiggle = pyganim.PygAnimation([(self.kuvat[1],0.2),
											(self.kuvat[4],0.2),
											(self.kuvat[1],0.2),
											(self.kuvat[5],0.2)])
		self.wiggle.play()
											
		self.sing = pyganim.PygAnimation([(self.kuvat[20],0.2),
											(self.kuvat[21],0.2),
											(self.kuvat[22],0.2),
											(self.kuvat[23],0.2)])
		self.sing.play()
		
		self.masturbate = pyganim.PygAnimation([(self.kuvat[7],0.1),
												(self.kuvat[8],0.2)])
		self.masturbate.play()
		
		self.moonwalk = pyganim.PygAnimation([(self.kuvat[12],0.1),
											(self.kuvat[13],0.1),
											(self.kuvat[15],0.1),
											(self.kuvat[14],0.1),
											(self.kuvat[13],0.1)])
		self.moonwalk.play()
		self.fight = pyganim.PygAnimation([(self.kuvat[16],0.1),(self.kuvat[17],0.1)])
		self.fight.play()

		self.jump = pyganim.PygAnimation([(self.kuvat[0], 0.3),
											(self.kuvat[19], 0.2),
											(self.kuvat[0], 0.3)])
		self.jump.play()
		self.fuck = pyganim.PygAnimation([(self.kuvat[18], 0.5),
											(self.kuvat[0], 0.5)])
		self.fuck.play()

		self.smoke = pyganim.PygAnimation([(self.kuvat[24], 0.2),
											(self.kuvat[25], 0.2),
											(self.kuvat[26], 0.2)])
		self.smoke.play()	
	def update(self,screen):
		#Vaatteet paalla
		if self.state == 1: 
			self.img = self.kuvat[0]
			screen.blit(self.img,[self.x,self.y])
		#nekkid
		elif self.state == 2:
			self.img = self.kuvat[1]
			screen.blit(self.img,[self.x,self.y])
		#suicide
		elif self.state == 4:
			self.img = self.kuvat[3]
			screen.blit(self.img,[self.x,self.y])
			#dance
		elif self.state == 5:
			self.dance.blit(screen,[self.x,self.y])
			#wiggle naked
		elif self.state == 6:
			self.wiggle.blit(screen,[self.x,self.y])
		elif self.state == 7:
			self.masturbate.blit(screen,[self.x,self.y])
		elif self.state == 8:
			self.sing.blit(screen,[self.x,self.y])
		elif self.state == 9:
			self.moonwalk.blit(screen,[self.x,self.y])
		elif self.state == 10:
			self.fight.blit(screen,[self.x,self.y])
		elif self.state == 11:
			self.wiggle.blit(screen,[self.x,self.y])
		elif self.state == 12:
			self.jump.blit(screen, [self.x,self.y])
		elif self.state == 13:
			self.fuck.blit(screen, [self.x,self.y])
		elif self.state == 14:
			self.smoke.blit(screen, [self.x, self.y])

class Bouncer:

    def __init__(self, posx, posy):
        self.state = 1
        self.x = posx
        self.y = posy
        self.health = 100
        self.kuvat = glob.glob("img/bouncer*.png")
        self.kuvat.sort()
        for i in range(len(self.kuvat)):
            self.img = pygame.image.load(self.kuvat[i]).convert_alpha()
            self.kuvat[i] = pygame.transform.scale(self.img,[200,200])
        self.img = self.kuvat[0]

        self.bouncer = pyganim.PygAnimation([(self.kuvat[0],0.2)])
        self.bouncer.play()

    def update(self, screen):
        if self.health > 0:
            self.img = self.kuvat[0]
            screen.blit(self.img, [self.x, self.y])
        else:
            self.img = self.kuvat[1]
            screen.blit(self.img, [self.x, self.y])
					
def main():
	#ALustetaan pygame
	pygame.init()
	#taustakuvan nimi
	bg = "img/background.png"
	beat = pygame.mixer.Sound("sounds/GGJ13_Theme.wav")
	beat.play(loops = -1)
	
	#FPS:aa varten kello
	clock = pygame.time.Clock()
	#ikkuna
	screen = pygame.display.set_mode([860,640])
	#kaljakoppa
	beer_case = pygame.image.load("img/koppa.png").convert_alpha()
	beer_case = pygame.transform.scale(beer_case,[130,130])
	#Game over bg
	gameoverpic = pygame.image.load("img/game_over_screen.png").convert()
	gameoverpic = pygame.transform.scale(gameoverpic, [600,600])
	MAX_X = screen.get_width()
	MAX_Y = screen.get_height()
	CENTER = [(MAX_X/2),(MAX_Y/2)]
	posx = 400
	posy = 400
	
	#Muutama vari rgb:na
	vari1 = (200,178,87)
	vari2 = (100,13,13)
	
	
	#pelisilmukan paattymisehto
	done = False
	#gameover ruudun paattymisehto
	gameover = False
	#sanat joihin tallennetaan & verrataan
	sana = ""
	kirjain = ""
	sanalista = []
	
	#Pelaajan luonti
	player = Player(posx,posy)
	#Friendon luonti
	friendo = Friendo(55,posy)
	#Typykka
	typykka = Typy(150,posy-12)
	#Sytamet
	sydan1 = Hearts(180,20)
	sydan2 = Hearts(260,20)
	sydan3 = Hearts(340,20)
	sydan4 = Hearts(420,20)
	sydan5 = Hearts(500,20)
	#Tausta
	background = pygame.image.load(bg).convert()
	
	#Kayttajan syottama teksti objekti fontti jne
	fontti = pygame.font.Font("freesansbold.ttf",20)
	tulostus = fontti.render(sana,True,vari2)
	
	#ALoitusviesti / palauteviesti
	message = "Try to earn a beer by doing stuff"
	
	#Vinkki/ hint pelaajalle
	a_hint = "Try typing a command"
	
	#Ladataan voittoruutu animaatio
	win_images = glob.glob("img/fireworks*.png")
	win_images.sort()
	win_anim = pyganim.PygAnimation([(win_images[0],0.2),
									(win_images[1],0.2),
									(win_images[2],0.2),
									(win_images[3],0.2),
									(win_images[4],0.2)])
	
	#Helikopteri ;)
	heli = glob.glob("img/kopteri*.png")
	heli.sort()
	for i in range(len(heli)):
		kuva = pygame.image.load(heli[i]).convert_alpha()
		heli[i] = pygame.transform.scale(kuva,[100,100])
	helikopteri = pyganim.PygAnimation([(heli[0],0.1),
									(heli[1],0.1),
									(heli[2],0.1),
									(heli[3],0.1)])
	helikopteri.play()
	
	#animoidaan friendo ja typykka
	friendo.img.play()
	typykka.img.play()
	sydan1.img.play()
	sydan2.img.play()
	sydan3.img.play()
	sydan4.img.play()
	sydan5.img.play()
	
	
	#Aloitusruutu
	bg = pygame.image.load("img/main_screen.png").convert()
	bg = pygame.transform.scale(bg,[860,640])
	show = True
	while show == True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					show = False
				elif event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
		screen.blit(bg,[0,0])
		pygame.display.update()
	
	
	#pelisilmukka 1 voitettu vai ei
	won1 = False
	
	#Pelisilmukka1
	#arvaukset ja vaarat arvaukset
	arvauksia = 10
	beer_x = 130
	beer_y = 240
	while done == False:
		
		#FPS = 60
		clock.tick(60)
		#katotaan eventit / 
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				#shifti pois aiheuttamasta erroreita
				if event.key == K_RSHIFT or event.key == K_LSHIFT or event.key == K_UP  or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
					continue
				if event.key == K_RETURN:
					sanalista = sana.split()
					sana = ""
					break
				#Muutetaan painallukset kirjain muotoon
				kirjain = str(chr(event.key))
				#lisataan painettu nappain sanaan
				sana += kirjain
				if event.key == K_BACKSPACE:
					sana = sana[0:-2] 
		screen.blit(background,[0,0])
		tulostus = fontti.render(">"+sana,True,vari2)
		screen.blit(tulostus,[0,605])
		
		#palaute viesti annetusta komennosta
		text1 = fontti.render(message,True,vari2,vari1)
		screen.blit(text1,[0,0])
		
		#hint, vinkki pelaajalle jos ei tajua mita pitaa teha
		hint = fontti.render(a_hint,True,vari2,vari1)
		screen.blit(hint,[0,150])
		
		#otetaan kirjoitetut komennot listaan, ja verrataan niita sanoihin
		command = etsisanat(sanalista)
		sanalista = []
		if command == "get_naked":
			beer_x += 10
			player.state = 2
			player.pisteet += 1
			if player.nekkid == False:
				player.nekkid = True
		elif command == "get_dressed":
			beer_x += 10
			player.pisteet += 1
			player.state = 1
		elif command == "move_left":
			player.x += -15
		elif command == "move_right":
			player.x += 15
		elif command == "suicide":
			player.state = 4
			done = True
			gameover = True
		elif command == "dance":
			beer_x += 10
			player.pisteet += 1
			player.state = 5
		elif command == "wiggle_wiggle":
			beer_x += 10
			player.pisteet += 2
			player.state = 6
		elif command == "get_first":
			message = "one does not simply drink beer without beer"
		elif command == "winwin":
			beer_x += 20
			player.pisteet += 5
			player.state = 7
		elif command == "sing":
			beer_x += 10
			player.state = 8
			player.pisteet += 2
		elif command == "dark_side":
			message = "Already tried, they didn't have cookies..."
		elif command == "unknown":
			arvauksia -= 1
			if arvauksia == 0:
				done = True
				gameover = True
			message = "Syntax Error, Key value error, division by zero!"
		elif command == "moonwalk":
			player.state = 9
			player.pisteet += 1
		elif command == "killed":
			friendo.img = pyganim.PygAnimation([(friendo.kuvat[1],0.2)])
			friendo.img.play()
		elif command == "heli":
			player.state = 11
		elif command == "beer":
			message = "Can't reach the beer, must use force"
		elif command == "force":
			beer_x += 2
			message = "Used THE FORCE, now thirsty"
		elif command == "skip":
			done = True
			won1 = True
		elif command == "penus":
			message = "Behold The mighty Penus Torvalds!"
		elif command == "smoke":
			message = "So you started smoking? huh?"
			player.state = 14
		elif command == "happy_ending":
			message = "You had a \"healthy\" massage.."
		elif command == "jump":
			player.state = 12
		elif command == "fuck_you":
			player.state = 13
		elif command == "stop":
			player.state = 1
		
	
		#ja piirretaan sen ruudulle
		#mittarin piirto
		friendo.update(screen)
		player.update(screen)
		#helikopteri purkka
		if player.state == 11:
			helikopteri.blit(screen,[player.x+50,player.y+100])
		typykka.update(screen)
		sydan1.update(screen)
		if arvauksia > 2:
			sydan2.update(screen)
			a_hint = "Play with yourself... furiously!(and yes we are monitoring your webcam)"
		if arvauksia > 4:
			sydan3.update(screen)
			a_hint = "HINT: What would pewds do. you can start by gettin rid of your clothes."
		if arvauksia > 6:
			sydan4.update(screen)
			a_hint = "HINT: Dance monkey DANCE!"
		if arvauksia > 8:
			a_hint = "HINT: keep an open mind. makers of this game ar nasty ppl"
			sydan5.update(screen)
		screen.blit(beer_case,[beer_x,beer_y])
		pygame.display.update()
		
		#Katsotaan ollaanko voitettu eli pisteet >= 8
		if player.pisteet >= 8:
			won1 = True
			done = True
		
	
	#Tason 1 voittoruutu:
	if won1 == True:
		player.state = 1
		win_anim.play()
		bg = pygame.image.load("img/level1_won.png").convert()
		bg = pygame.transform.scale(bg,[860,640])
		#Naytetaan voittoruutu, kunnes painetaan nappainta
		loop_dis = True
		while loop_dis == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					loop_dis = False
					break
			screen.blit(bg,[0,0])
			win_anim.blit(screen,[350,350])
			pygame.display.update()
	
	#Taso 2
	movex = 0
	if gameover == True:
		done = True
	else:
		done = False
	taustat = pyganim.PygAnimation([("img/jate01.png",1.0), ("img/jate02.png",1.0)])
	taustat.play()
	bouncer = Bouncer(100, 400)
	effects = Effect_holder(400, 400)
	update_pic = False
	damage = 0
	while done == False:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_UP or event.key == K_DOWN:
					player.state = 10
					damage = 0.2
				if event.key == K_LEFT:
					movex = -5
				if event.key == K_RIGHT:
					movex = 5
			if event.type == KEYUP:
					movex = 0
					player.state = 1
					damage = 0
		player.x += movex			
		taustat.blit(screen,[0,0])
		#ja piirretaan sen ruudulle
		bouncer.health -= damage
		player.update(screen)
		random_int = random.randint(0,100)
		if random_int < 5:
			update_pic = True
		if player.state == 10:
			effects.update(screen, update_pic)
		if bouncer.health <= 0:
			done = True
		update_pic = False
		text1 = fontti.render("The evil bouncer isn´t lettin ya in. BEAT HIM UP! (up and down arrows)",True,vari2,vari1)
		screen.blit(text1,[50,600])
		bouncer.update(screen)
		player.update(screen)
		pygame.display.update()
	if won1 == True:
		bouncer. x -= 50
		bouncer.y -= 140
		player.state = 1
		win_anim.play()
		bg = pygame.image.load("img/level_2_won.png").convert()
		bg = pygame.transform.scale(bg,[860,640])
		#Naytetaan voittoruutu, kunnes painetaan nappainta
		loop_dis = True
		while loop_dis == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					loop_dis = False
					break
			screen.blit(bg,[0,0])
			win_anim.blit(screen,[350,350])
			bouncer.update(screen)
			pygame.display.update()


	    #pelisilmukan paattymisehto
	done = False
    #sanat joihin tallennetaan & verrataan

    #Taso 3
    #Pelaajan luonti
	player = Player(posx,posy)
	tausta = Valot(0,0)
	polizei = Polizei(610,450)
	muumi = Moomin(90, 450)
	#animoidaan friendo
	#Pelisilmukka
	if gameover == True:
		player.state = 4
		player.img = player.kuvat[3]
	while done == False and gameover == False:
	    #FPS = 60
	    clock.tick(60)
	    #katotaan eventit / 
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            sys.exit()
	    #valojen vilkkumisen randomisuus
	    random_int = random.randint(0,100)
	    if random_int < 10:
	        update_pic = True
	    tausta.update(screen, update_pic)
	    update_pic = False
	    #ja piirretaan sen ruudulle
	    player.update(screen)
	    polizei.update(screen)
	    muumi.update(screen)
	    pygame.display.update()

	#Game over screen
	if gameover == True:
		loop_this = True
		while loop_this == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					loop_this = False
				if event.type == KEYDOWN:
					loop_this = False
			screen.blit(gameoverpic,[0,0])
			screen.blit(player.img,[player.x,player.y])
			pygame.display.update()
	pygame.quit()

main()
