from init import *

#function
def move():
    sp_move = 2.5
    button = pygame.key.get_pressed()
    if button[pygame.K_UP]:
        if sp_rect.top>=20: sp_rect.centery-=sp_move
    if button[pygame.K_DOWN]:
        if sp_rect.bottom<=750: sp_rect.centery+=sp_move
    if button[pygame.K_LEFT]:
        if sp_rect.centerx>=5: sp_rect.centerx-=sp_move
    if button[pygame.K_RIGHT]:
        if sp_rect.centerx<=495: sp_rect.centerx+=sp_move
def draw_line(n):
    a = n-108
    b = n+110
    pygame.draw.line(screen, (0,255,0), (26,a), (475,a))
    pygame.draw.line(screen, (0,255,0), (26,b), (475,b))
    pygame.draw.line(screen, (0,255,0), (26,a), (26,b))
    pygame.draw.line(screen, (0,255,0), (475,a), (475,b))
def check(x, y, a, b):
    x_mn, x_mx = a-55, a+55
    y_mn, y_mx = b-27, b+27
    if x>=x_mn and x<=x_mx and y>=y_mn and y<=y_mx:
        return True
    return False
def button(a, b):
    x_mn, x_mx = a-55, a+55
    y_mn, y_mx = b-27, b+27
    pygame.draw.line(screen, (0,255,0), (x_mn, y_mn), (x_mx, y_mn))
    pygame.draw.line(screen, (0,255,0), (x_mn, y_mx), (x_mx, y_mx))
    pygame.draw.line(screen, (0,255,0), (x_mn, y_mn), (x_mn, y_mx))
    pygame.draw.line(screen, (0,255,0), (x_mx, y_mn), (x_mx, y_mx))

def create_chick(ok):
    cnt = 1
    lst = []
    cnt = random.randint(1,3)
    if ok: 
        x = random.randint(40,250)
        ok = False
    else:
        x = random.randint(250,460)
        ok = True
    lst.append(chick.get_rect(center = (x,-50)))
    if cnt>=2: lst.append(chick.get_rect(center = (x-30,-50)))
    if cnt==3: lst.append(chick.get_rect(center = (x+30,-50)))
    
    return lst, ok
def move_chick(lst):
    for chick in lst:
        chick.centery += 1.2
def draw_chick(lst):
    for chick_rect in lst:
        screen.blit(chick, chick_rect)

def create_bullet(bullet_max):
    lst = []
    lst.append(bullet.get_rect(center = (sp_rect.centerx, sp_rect.centery-60)))
    x = 5
    y = 58
    for i in range(0,bullet_max): 
        lst.append(bullet.get_rect(center = (sp_rect.centerx-x, sp_rect.centery-y)))
        lst.append(bullet.get_rect(center = (sp_rect.centerx+x, sp_rect.centery-y)))
        x += 5
        y -= 2
        
    return lst
def move_bullet(lst):
    for bullet in lst:
        for i in bullet:
            i.centery -= 5
            if i.centery<=0: bullet.remove(i)
        if len(bullet)==0: lst.remove(bullet)
    return lst
def draw_bullet(lst):
    for bullet_lst in lst:
        for bullet_rect in bullet_lst:
            screen.blit(bullet, bullet_rect)

def create_add():
    x = random.randint(50, 450)
    add_rect = add.get_rect(center = (x, -50))
    return add_rect
def move_add(lst):
    for add in lst:
        add.centery += 1.2
        if add.centery>=750: lst.remove(add)
    return lst
def draw_add(lst):
    for add_rect in lst:
        screen.blit(add,add_rect)

def draw_boom(lst):
    for boom_rect in lst:
        if boom_rect[1]==0: lst.remove(boom_rect)
        else:
            screen.blit(boom, boom_rect[0])
            boom_rect[1]-=1
def draw_heart(cnt):
    pos = 0
    for i in range(cnt):
        screen.blit(heart, (5 + pos, 2))
        pos += 25
def draw_score(score):
    score_show = font.render("Score: {}".format(score), True, (255,255,255))
    score_rect = score_show.get_rect(center = (400,35))
    screen.blit(score_show, score_rect)

#screen2
def create_chick_lst():
    lst = [[], [], [], []]
    pos = 85
    for i in range(7):
        lst[0].append(chick.get_rect(center = (pos, -240)))
        lst[1].append(chick1.get_rect(center = (pos, -170)))
        lst[2].append(chick2.get_rect(center = (pos, -100)))
        lst[3].append(chick3.get_rect(center = (pos, -30)))
        pos += 55
    return lst
def draw_chick_screen2(lst, flap):
    for i in range(len(lst[0])): 
        lst[0][i].centerx += flap
        screen.blit(chick, lst[0][i])
    for i in range(len(lst[1])): 
        lst[1][i].centerx -= flap
        screen.blit(chick1, lst[1][i])
    for i in range(len(lst[2])): 
        lst[2][i].centerx += flap
        screen.blit(chick2, lst[2][i])  
    for i in range(len(lst[3])): 
        lst[3][i].centerx -= flap
        screen.blit(chick3, lst[3][i])  
    return lst, 0 
def draw_boss(lst, flap, boss_cnt):
    lst[0].centerx += flap
    if boss_cnt==3: screen.blit(boss1, lst[0])
    elif boss_cnt==6: screen.blit(boss2, lst[0]) 
    return lst, flap
def move_chick_screen2(lst, ok_shoot, boss_cnt):
    global bullet_lst
    speed = 5
    if boss_cnt%3!=0:
        if lst[0]==[] or lst[0][0].centery==100 or not ok_shoot: 
            ok_shoot = True
            return lst, ok_shoot
        for i in range(len(lst[0])): lst[0][i].centery += speed
        for i in range(len(lst[1])): lst[1][i].centery += speed
        for i in range(len(lst[2])): lst[2][i].centery += speed
        for i in range(len(lst[3])): lst[3][i].centery += speed
    else:
        if lst[0].centery==200:
            ok_shoot = True
            return lst, ok_shoot
        lst[0].centery += speed
    bullet_lst.clear()
    return lst, ok_shoot

def create_battle(lst_chick, boss_cnt):
    global sp_rect
    global heart_max
    n = m = -1
    if boss_cnt%3!=0:
        while n==-1 or m==-1:
            n = random.randint(0,3)
            if len(lst_chick[n])!=0: m = random.randint(0, len(lst_chick[n])-1)
        return battle.get_rect(center = (lst_chick[n][m].centerx, lst_chick[n][m].centery+20))
    else:
        return battle.get_rect(center = (lst_chick[0].centerx, lst_chick[0].centery))
def move_battle(lst_battle):
    for i in lst_battle:
        i.centery += 1
    return lst_battle
def draw_battle(lst_battle):
    for i in lst_battle:
        screen.blit(battle, i)

def draw_hp(x, hp):
    pygame.draw.rect(screen, (0,0,0), (x-60, 300, 120, 5))
    pygame.draw.rect(screen, (0,255,0), (x-60, 300, hp, 5))

#collision
def cls_bullet_chick(lst_chick, lst_bullet, lst_boom, score):
    for chick in lst_chick:
        for bullet in lst_bullet:
            for i in bullet:
                if chick.colliderect(i) and abs(chick.centerx-i.centerx)<25 and chick.centery>=10:
                    kill.play()
                    x = chick.centerx
                    y = chick.centery
                    lst_chick.remove(chick)
                    lst_bullet.remove(bullet)
                    lst_boom.append([boom.get_rect(center = (x,y)), 15])
                    score += 10
                    break
    return lst_chick, lst_bullet, lst_boom, score
def cls_sp_chick(lst, heart_max):
    global game
    a = sp_rect.centery-(sp.get_height()/2)
    b = sp_rect.centery+20
    c = sp_rect.centery+(sp.get_height()/2)
    for chick_rect in lst:
        n = chick_rect.centery-(chick.get_height()/2)
        m = chick_rect.centery+(chick.get_height()/2)
        ok = True
        if (n>=a and n<=b) or (m>=a and m<=b):
            if abs(sp_rect.centerx-chick_rect.centerx)<15: 
                die.play()
                heart_max-=1
                lst.remove(chick_rect)
                ok = False
        if (n>=b and n<=c) or (m>=b and m<=c) and ok:
            if abs(sp_rect.centerx-chick_rect.centerx)<60: 
                die.play()
                heart_max-=1
                lst.remove(chick_rect)
        if heart_max==0: return lst, heart_max
    return lst, heart_max
def cls_sp_add(lst, bullet_max):
    a = sp_rect.centery-(sp.get_height()/2)
    b = sp_rect.centery+20
    c = sp_rect.centery+(sp.get_height()/2)
    for add_rect in lst:
        n = add_rect.centery-(add.get_height()/2)
        m = add_rect.centery+(add.get_height()/2)

        if (n>=a and n<=b) or (m>=a and m<=b):
            if abs(sp_rect.centerx-add_rect.centerx)<15: 
                level_up.play()
                bullet_max+=1
                lst.remove(add_rect)
        if (n>=b and n<=c) or (m>=b and m<=c):
            if abs(sp_rect.centerx-add_rect.centerx)<60: 
                level_up.play()
                bullet_max+=1
                lst.remove(add_rect)
    return lst, bullet_max

def cls_sp_thigh(lst, heart_max):
    a = sp_rect.centery-(sp.get_height()/2)
    b = sp_rect.centery+20
    c = sp_rect.centery+(sp.get_height()/2)
    for thigh in lst:
        n = thigh.centery-(battle.get_height()/2)
        m = thigh.centery+(battle.get_height()/2)
        ok = True
        if (n>=a and n<=b) or (m>=a and m<=b):
            if abs(sp_rect.centerx-thigh.centerx)<15: 
                die.play()
                heart_max-=1
                lst.remove(thigh)
                ok = False
        if (n>=b and n<=c) or (m>=b and m<=c) and ok:
            if abs(sp_rect.centerx-thigh.centerx)<60: 
                die.play()
                heart_max-=1
                lst.remove(thigh)
        if heart_max==0: return lst, heart_max
    return lst, heart_max
def cls_bullet_boss(lst_chick_screen2, bullet_lst, lst_boom, score, hp):
    x = lst_chick_screen2[0].centerx
    y = lst_chick_screen2[0].centery
    for bullet in bullet_lst:
        for i in bullet:
            if abs(x-i.centerx)<80 and abs(y-i.centery)<80:
                hp -= 2
                kill.play()
                bullet_lst.remove(bullet)
                if hp==0:
                    score += 1000
                    lst_chick_screen2 = [[], [], [], []]
                    lst_boom.append([boom.get_rect(center = (x,y)), 15])
                    return lst_chick_screen2, bullet_lst, lst_boom, score, hp
                break
    return lst_chick_screen2, bullet_lst, lst_boom, score, hp

#run
def start():
    welcome = font.render("Welcome to spaceship!", True, (255,0,0))
    ready = font.render("Are you ready?", True, (255,255,255))

    screen.blit(welcome, welcome.get_rect(center = (250,180)))
    screen.blit(ready, ready.get_rect(center = (250,250)))
    screen.blit(sp, sp.get_rect(center = (250, 450)))
    screen.blit(play, play.get_rect(center = (250,600)))
    button(250, 600)
def stop(score, high_score):
    name = font.render("Space ship".format(score), True, (255,0,0))
    score_sur = font.render("Score: {}".format(score), True, (255,255,255))
    high_sur = font.render("High score: {}".format(high_score), True, (255,255,255))

    screen.blit(name, name.get_rect(center = (250,180)))
    screen.blit(score_sur, score_sur.get_rect(center = (250,250)))
    screen.blit(high_sur, high_sur.get_rect(center = (250,300)))
    screen.blit(sp, sp.get_rect(center = (250, 450)))
    screen.blit(new, new.get_rect(center = (250,570)))
    button(250, 570)
    screen.blit(back, back.get_rect(center = (250,650)))
    button(250, 650)
def select():
    #background
    bg2 = pygame.image.load("assets/bg2.png")
    bg2 = pygame.transform.rotate(bg2, -90)
    bg2 = pygame.transform.scale_by(bg2, 3)
    screen.blit(bg2, (0,0))

    #screen1
    screen1 = pygame.image.load("assets/screen1.png")
    screen1 = pygame.transform.scale_by(screen1, 0.45)
    screen.blit(screen1, screen1.get_rect(center = (250, 140)))
    draw_line(140)
    #screen2
    screen2 = pygame.image.load("assets/screen2.png")
    screen2 = pygame.transform.scale_by(screen2, 0.45)
    screen.blit(screen2, screen2.get_rect(center = (250, 390)))
    draw_line(390)
    #back
    screen.blit(back, back.get_rect(center = (250,650)))
    button(250,650)