from init import *
from func import *

while True:
    
    screen.blit(bg,(0,0))

    if game=="start": start()
    elif game=="select": select()
    elif game=="stop": stop(score, high_score)
    elif game=="screen1":
        screen.blit(sp, sp_rect)
        move()

        move_chick(chick_lst)
        draw_chick(chick_lst)

        bullet_lst = move_bullet(bullet_lst)
        draw_bullet(bullet_lst)

        add_lst = move_add(add_lst)
        draw_add(add_lst)

        chick_lst, bullet_lst, boom_lst, score = cls_bullet_chick(chick_lst, bullet_lst, boom_lst, score)
        chick_lst, heart_max = cls_sp_chick(chick_lst, heart_max)
        add_lst, bullet_max = cls_sp_add(add_lst, bullet_max)

        draw_boom(boom_lst)
        draw_heart(heart_max)
        draw_score(score)
        if heart_max==0: game = "stop"; hades.stop()
        if high_score<score: high_score = score
        if score==speed_up_next and timer_chick>150:
            timer_chick -= 80
            pygame.time.set_timer(spawn_chick, timer_chick)
            speed_up_next *= 3
        
    elif game=="screen2":
        screen.blit(sp, sp_rect)
        move()

        if lst_chick_screen2==[[], [], [], []]: 
            ok_shoot = False
            boss_cnt += 1
            cnt = -25
            if boss_cnt%3!=0: 
                lst_chick_screen2 = create_chick_lst() 
            else:
                lst_chick_screen2.clear()
                hp = 120
                if boss_cnt==3: lst_chick_screen2.append(boss1.get_rect(center = (250, -100)))
                elif boss_cnt==6: lst_chick_screen2.append(boss2.get_rect(center = (250, -100)))

        if boss_cnt%3!=0:
            lst_chick_screen2, flap = draw_chick_screen2(lst_chick_screen2, flap)
        else:
            lst_chick_screen2, flap = draw_boss(lst_chick_screen2, flap, boss_cnt)
            draw_hp(lst_chick_screen2[0].centerx, hp)

        lst_chick_screen2, ok_shoot = move_chick_screen2(lst_chick_screen2, ok_shoot, boss_cnt)

        if ok_shoot:
            bullet_lst = move_bullet(bullet_lst)
            draw_bullet(bullet_lst)
        if boss_cnt%3!=0:
            for i in range(4):
                lst_chick_screen2[i], bullet_lst, boom_lst, score = cls_bullet_chick(lst_chick_screen2[i], bullet_lst, boom_lst, score)
                lst_chick_screen2[i], heart_max = cls_sp_chick(lst_chick_screen2[i], heart_max)
        else:
            lst_chick_screen2, bullet_lst, boom_lst, score, hp = cls_bullet_boss(lst_chick_screen2, bullet_lst, boom_lst, score, hp)

        lst_battle = move_battle(lst_battle)
        draw_battle(lst_battle)
        lst_battle, heart_max = cls_sp_thigh(lst_battle, heart_max)

        

        draw_boom(boom_lst)
        draw_heart(heart_max)
        draw_score(score)
        if heart_max==0: game = "stop"; hades.stop()
        if high_score<score: high_score = score
        if boss_cnt==6 and lst_chick_screen2==[[], [], [], []]: game="stop"; hades.stop()

    for event in  pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == spawn_chick and game=="screen1":
            new_chick, ok_chick = create_chick(ok_chick)
            for i in new_chick:
                chick_lst.append(i)
        if event.type == spawn_bullet and (game=="screen1" or game=="screen2" ):
            bullet_lst.append(create_bullet(bullet_max))
        if event.type == spawn_add and game=="screen1":
            add_lst.append(create_add())
        if event.type == spawn_flap and game=="screen2":
            cnt+=1
            if cnt%50==0 and direct=="up": direct = "down"
            elif cnt%50==0 and direct=="down": direct = "up"
            if direct=="up": flap = 2
            elif direct=="down": flap = -2
        if event.type == spawn_battle and game=="screen2":
            if lst_chick_screen2[0]!=[] or lst_chick_screen2[1]!=[] or lst_chick_screen2[2]!=[]:
                lst_battle.append(create_battle(lst_chick_screen2, boss_cnt))
        if event.type == pygame.MOUSEBUTTONUP and game=="select":
            x, y = pygame.mouse.get_pos()
            heart_max = 5;  bullet_max = 0; timer_chick = 500
            score = 0; speed = 750; speed_up_next = 100
            hp = 120; boss_cnt = 1
            bullet_lst.clear()
            lst_battle.clear()
            boom_lst.clear()
            pygame.time.set_timer(spawn_chick, timer_chick)
            if x>=26 and x<=465 and y>=32 and y<=250:
                    game = "screen1"
                    hades.play()
            if x>=26 and x<=465 and y>=282 and y<=500:
                    game = "screen2"
                    bullet_max = 1
                    lst_chick_screen2 = create_chick_lst()
                    hades.play()
            if check(x, y, 250, 650):
                game = "start"
        if event.type == pygame.MOUSEBUTTONUP and game=="start":
            x, y = pygame.mouse.get_pos()
            if check(x, y, 250, 600):
                game = "select"
        if event.type == pygame.MOUSEBUTTONUP and game=="stop":
            x, y = pygame.mouse.get_pos()
            chick_lst.clear()
            bullet_lst.clear()
            sp_rect.centerx = 250
            sp_rect.centery = 600
            if check(x, y, 250, 570):
                game = "select"
            if check(x, y, 250, 650):
                game = "start"
                
    pygame.display.update()
    clock.tick(120)