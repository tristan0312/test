import pygame, sys
from pygame.locals import *
import random
import math
import time
pygame.init()
pygame.key.set_repeat(50)

class Player:
    def __init__(self, pos_x, pos_y):
        self.moving_left = False
        self.moving_right = False
        self.moving_down = False
        self.moving_high = False
        self.x = pos_x
        self.y = pos_y
        self.sprites_high = []
        self.sprites_high.append(pygame.image.load('up_0.png'))
        self.sprites_high.append(pygame.image.load('up_1.png'))
        self.sprites_high.append(pygame.image.load('up_2.png'))
        self.sprites_high.append(pygame.image.load('up_3.png'))
        self.sprites_down = []
        self.sprites_down.append(pygame.image.load('down_0.png'))
        self.sprites_down.append(pygame.image.load('down_1.png'))
        self.sprites_down.append(pygame.image.load('down_2.png'))
        self.sprites_down.append(pygame.image.load('down_3.png'))
        self.sprites_right = []
        self.sprites_right.append(pygame.image.load('right_0.png'))
        self.sprites_right.append(pygame.image.load('right_1.png'))
        self.sprites_right.append(pygame.image.load('right_2.png'))
        self.sprites_right.append(pygame.image.load('right_3.png'))
        self.sprites_left = []
        self.sprites_left.append(pygame.image.load('left_0.png'))
        self.sprites_left.append(pygame.image.load('left_1.png'))
        self.sprites_left.append(pygame.image.load('left_2.png'))
        self.sprites_left.append(pygame.image.load('left_3.png'))
        self.current_sprite = 0
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        self.vie = 50
        self.max_vie = 50
       
        
    def mouvement_haut(self):
        self.moving_high = True

        
    def mouvement_bas(self):
        self.moving_down = True

        
    def mouvement_droite(self):
        self.moving_right = True

        
    def mouvement_gauche(self):
        self.moving_left = True
    
    def draw(self):
        screen.blit(self.image, self.rect)
        
        
        
    def barre_vie(self):
        couleur_barre_vie = (111, 210, 46)
        couleur_fond_barre = (0, 0, 0)
        
        barre_position = [self.rect[0] + 10, self.rect[1] - 10, self.vie, 6]
        barre_position_fond = [self.rect[0] + 10, self.rect[1] - 10, self.max_vie, 6]
        
        pygame.draw.rect(screen, couleur_fond_barre, barre_position_fond)
        pygame.draw.rect(screen, couleur_barre_vie, barre_position)
   
                
                
                
    

    def update(self, speed):
        if self.moving_high == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_high):
                self.current_sprite = 0
                self.moving_high = False
            self.image = self.sprites_high[int(self.current_sprite)]
            
        if self.moving_down == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_down):
                self.current_sprite = 0
                self.moving_down = False
            self.image = self.sprites_down[int(self.current_sprite)]
            
            
        if self.moving_left == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_left):
                self.current_sprite = 0
                self.moving_left = False
            self.image = self.sprites_left[int(self.current_sprite)]
            
            
        if self.moving_right == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites_right):
                self.current_sprite = 0
                self.moving_right = False
            self.image = self.sprites_right[int(self.current_sprite)]

        
pygame.init()
clock = pygame.time.Clock()            

screen_width = 1800
screen_height = 1200
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("zombie attack")
            
player = Player(screen_width/2, screen_height/2)
BG = pygame.image.load('bg.png').convert_alpha()
position_BG = BG.get_rect()
position_BG.topleft = (-1100, -1300)

class Zombie:
    def __init__(self):
        self.monstre_image = pygame.image.load('0.png')
        self.taille = 10
        self.x = random.randint(0,  screen_width - self.taille)
        self.y = random.randint(0,  screen_height - self.taille)
        self.vitesse = 1
        self.vie = 50
        self.max_vie = 50
        self.deplacement = []
        self.deplacement.append(pygame.image.load('0.png'))
        self.deplacement.append(pygame.image.load('1.png'))
        self.deplacement.append(pygame.image.load('2.png'))
        self.deplacement.append(pygame.image.load('3.png'))
        self.sprite_actuelle = 0
        self.mouvement = False
        
    def mouvements(self):
        self.mouvement = True
        
    def affichage(self):
        screen.blit(self.monstre_image, (self.x, self.y))
        
    def mvt(self, target_x, target_y):
        distance_x = target_x - self.x
        distance_y = target_y - self.y
        distance = (distance_x**2 + distance_y**2)**0.5
        
        if distance <= 40:
            player.vie -= 0.5
        
        if distance <  600:
            if self.x < player.rect[0]:
                self.x += self.vitesse
            if self.x > player.rect[0]:
                self.x -= self.vitesse
            if self.y < player.rect[1]:
                self.y += self.vitesse
            if self.y > player.rect[1]:
                self.y -= self.vitesse
        else:
            self.x = self.x
            self.y = self.y
            
    def barre_vie(self):
        couleur_barre_vie = (255, 0, 0)
        couleur_fond_barre = (0, 0, 0)
        
        barre_position = [self.x + 10, self.y - 10, self.vie, 6]
        barre_position_fond = [self.x + 10, self.y - 10, self.max_vie, 6]
        
        pygame.draw.rect(screen, couleur_fond_barre, barre_position_fond)
        pygame.draw.rect(screen, couleur_barre_vie, barre_position)

            
    def update(self, speed):
        if self.mouvement == True:
            self.sprite_actuelle += speed
            if int(self.sprite_actuelle) >= len(self.deplacement):
                self.sprite_actuelle = 0
                self.mouvement = False
            self.monstre_image = self.deplacement[int(self.sprite_actuelle)]
            
            
class Bullet:
    def __init__(self,x, y,speed, targetx,targety):
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        angle = math.atan2(targety-y, targetx-x) 
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y
    
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect[0] = int(self.x)
        self.rect[1] = int(self.y)
        
    def affichage(self):
        screen.blit(self.image,(self.x, self.y))            
            
            
            
            
            

lst_zmb = [Zombie() for k in range(15)]

def loose():
    police = pygame.font.SysFont('John Hubbard',120)
    image_texte = police.render("game over", 1, (255,0,0))
    screen.blit(image_texte,(700 ,500))
    pygame.display.flip()


bullets = []
def main_jeux():   
    while True:
        screen.fill('blue')
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                b = Bullet(player.rect[0], player.rect[1],20, x,y)
                bullets.append(b)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.mouvement_droite()
                    position_BG[0] -= 25
                    for zmb in lst_zmb:
                        zmb.x -= 25
                if event.key == pygame.K_z:
                    position_BG[1] += 25
                    for zmb in lst_zmb:
                        zmb.y += 25
                    player.mouvement_haut()
                if event.key == pygame.K_s:
                    position_BG[1] -= 25
                    for zmb in lst_zmb:
                        zmb.y -= 25
                    player.mouvement_bas()
                if event.key == pygame.K_q:
                    player.mouvement_gauche()
                    position_BG[0] += 25
                    for zmb in lst_zmb:
                        zmb.x += 25
                  
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
                
            for b in bullets:
                b.move()
            
                

        screen.blit(BG, position_BG)
        
        if player.vie <= 0:
            loose()
            time.sleep(3)
            sys.exit()
            pygame.quit()
            
        for b in bullets:
            b.affichage()   
        for zmb in lst_zmb:
            zmb.affichage()
            zmb.barre_vie()
            zmb.mouvements()
            zmb.mvt(player.rect[0], player.rect[1])
            zmb.update(0.25)
            
        player.barre_vie()
        player.draw()
        player.update(0.25)
        
        pygame.display.flip()
        clock.tick(60)
                
                
main_jeux()