import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((500,750))
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load("assets/logo.png"))
pygame.display.set_caption("Spaceship")

#font
font = pygame.font.Font(None,35)
play = font.render(" Play ", True, (0,255,0))       #1
new = font.render(" New ", True, (0,255,0))    #2
back = font.render(" Back ", True, (0,255,0))       #3

#sounds
kill = pygame.mixer.Sound("sounds/kill.wav")
die = pygame.mixer.Sound("sounds/die.wav")
level_up = pygame.mixer.Sound("sounds/levelup.wav")
hades = pygame.mixer.Sound("sounds/hades.wav")

#global
game = "start"
score = 0
high_score = 0
ok_chick = True
speed_up_next = 100

#screen2 - global
cnt = -25
flap = 2
direct = "up"
ok_shoot = False
boss_cnt = 1
hp = 120

#background
bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale_by(bg, 3/7)
bg = pygame.transform.rotate(bg, -90)

#spaceship
sp = pygame.image.load("assets/sp.png")
sp_rect = sp.get_rect(center = (250,600))

#chicken
chick = pygame.image.load("assets/chick.png")
chick1 = pygame.image.load("assets/chick1.png")
chick2 = pygame.image.load("assets/chick2.png")
chick3 = pygame.image.load("assets/chick3.png")
chick_lst = []
lst_chick_screen2 = []

boss1 = pygame.image.load("assets/boss1.png")
boss2 = pygame.image.load("assets/boss2.png")

#bullet
bullet = pygame.image.load("assets/bullet.png")
bullet = pygame.transform.scale_by(bullet, 0.08)
bullet_lst = []
bullet_max = 0

#heart
heart = pygame.image.load("assets/heart.png")
heart = pygame.transform.scale_by(heart, 0.25)
heart_max = 5

#boom
boom = pygame.image.load("assets/boom.png")
boom = pygame.transform.scale_by(boom, 0.18)
boom_lst = []

#add bullet
add = pygame.image.load("assets/add.png")
add_lst = []

#battle
battle = pygame.image.load("assets/thigh.png")
# battle = pygame.transform.rotate(battle, 180)
battle = pygame.transform.scale_by(battle, 0.12)
lst_battle = []

#timer
timer_chick = 500
spawn_chick = pygame.USEREVENT
pygame.time.set_timer(spawn_chick, timer_chick)

spawn_bullet = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_bullet, 100)

spawn_add = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_add, 12000) 

spawn_flap = pygame.USEREVENT + 3
pygame.time.set_timer(spawn_flap, 20)

spawn_battle = pygame.USEREVENT + 4
pygame.time.set_timer(spawn_battle, 1600) 