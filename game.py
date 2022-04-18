import parameters as p
from Button import *
from Bullet import *
from sounds import *
from effects import *
from images import *


class Bot:
    def __init__(self, in_image, in_size_x, in_size_y, in_coord_x, in_coord_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(in_image), (in_size_x, in_size_y))
        self.rect = self.image.get_rect()
        self.rect.x = in_coord_x
        self.rect.y = in_coord_y
        self.size_x = in_size_x
        self.size_y = in_size_y

    def blit(self):
        display.blit(self.image, (self.rect.x, self.rect.y))


class MoveSprite(Bot):
    def __init__(self, in_image, in_size_x, in_size_y, in_coord_x, in_coord_y, in_speed):
        super().__init__(in_image, in_size_x, in_size_y, in_coord_x, in_coord_y)
        self.speed = in_speed

    def move(self, x, y, cooldown3):
        self.rect.x += self.speed*x
        self.rect.y += self.speed*y
        self.cooldown3 = 0


class EnemySprite(MoveSprite):
    direction = 1

    def move(self, x, y, cooldown3):
        self.cooldown3 = 0
        if self.rect.y <= 50:
            self.direction = 1
        if self.rect.y >= display_height - 50:
            self.direction = -1
        super().move(0, self.direction, 0)

    def kill(self):
        pass


bot = EnemySprite('players/bot.png', usr_height2, usr_width2, bot_x, bot_y, 5)


class Game:
    def __init__(self):
        pygame.display.set_caption('CubeStrike')

        self.img_counter = 0
        self.health = 3
        self.health2 = 3
        self.cooldown = 0
        self.cooldown2 = 0
        self.cooldown3 = 0

    def show_menu(self):
        menu_bckgr = pygame.image.load('backgrounds/menu.png')

        start_btn = Button(288, 70)
        start_btn2 = Button(288, 70)
        quit_btn = Button(120, 70)

        show = True
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_bckgr, (0, 0))
            start_btn.draw(350, 205, '1 player', self.start_game2, 50)
            start_btn2.draw(350, 325, '2 player', self.start_game, 50)
            quit_btn.draw(400, 500, 'Quit', self.quit, 50)

            pygame.display.update()
            clock.tick(60)

    def start_game(self):
        while self.game_cycle():
            self.health = 3
            self.health2 = 3

    def start_game2(self):
        while self.game_cycle2():
            self.health = 3
            self.health2 = 3

    def quit(self):
        quit()

    def game_cycle(self):
        game = True
        all_btn_bullets = []
        all_btn_bullets2 = []

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.pause()

            display.blit(background, (0, 0))
            display.blit(player, (p.usr_x, p.usr_y))
            display.blit(player2, (p.usr_x2, p.usr_y2))

            if not self.cooldown:
                if keys[pygame.K_q]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets.append(Bullet(p.usr_x + usr_width - 10, p.usr_y + 10))
                    self.cooldown = 50
            else:
                print_text('Cooldown time: ' + str(self.cooldown // 10), 20, 60)
                self.cooldown -= 1

            for bullet in all_btn_bullets:
                if not bullet.move():
                    all_btn_bullets.remove(bullet)
                #if pygame.collide_rect(bullet, player2):
                    #self.pause()

            if not self.cooldown2:
                if keys[pygame.K_RSHIFT]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets2.append(Bullet(p.usr_x2 - 10, p.usr_y2 + 10))
                    self.cooldown2 = 50
            else:
                print_text('Cooldown time: ' + str(self.cooldown2 // 10), 1090, 60)
                self.cooldown2 -= 1

            for bullet in all_btn_bullets2:
                if not bullet.move2():
                    all_btn_bullets2.remove(bullet)

            if keys[pygame.K_w] and p.usr_y >= 0:
                p.usr_y -= p.speed
            if keys[pygame.K_s] and p.usr_y <= display_height - 50:
                p.usr_y += p.speed
            if keys[pygame.K_a] and p.usr_x >= 0:
                p.usr_x -= p.speed
            if keys[pygame.K_d] and p.usr_x <= 545:
                p.usr_x += p.speed

            if keys[pygame.K_UP] and p.usr_y2 >= 0:
                p.usr_y2 -= p.speed
            if keys[pygame.K_DOWN] and p.usr_y2 <= display_height - 50:
                p.usr_y2 += p.speed
            if keys[pygame.K_LEFT] and p.usr_x2 >= 765:
                p.usr_x2 -= p.speed
            if keys[pygame.K_RIGHT] and p.usr_x2 <= display_width - 50:
                p.usr_x2 += p.speed

            display.blit(kust, (300, 100))
            display.blit(kust1, (1100, 600))
            display.blit(kust2, (80, 500))
            display.blit(kust3, (900, 250))
            self.show_health()
            self.show_health2()
            pygame.display.update()
            clock.tick(60)

    def game_cycle2(self):
        game2 = True

        all_btn_bullets = []
        all_btn_bullets3 = []

        while game2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.pause()

            display.blit(background, (0, 0))
            display.blit(player, (p.usr_x, p.usr_y))
            bot.blit()
            bot.move(bot_x, bot_y, 0)

            if not self.cooldown:
                if keys[pygame.K_q]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets.append(Bullet(p.usr_x + usr_width - 10, p.usr_y + 10))
                    self.cooldown = 50
            else:
                print_text('Cooldown time: ' + str(self.cooldown // 10), 20, 60)
                self.cooldown -= 1

            for bullet in all_btn_bullets:
                if not bullet.move():
                    all_btn_bullets.remove(bullet)

            if not self.cooldown3:
                pygame.mixer.Sound.play(bullet_sound)
                all_btn_bullets3.append(Bullet(p.bot_x - 10, p.bot_y + 10))
                self.cooldown2 = 50
            else:
                print_text('Cooldown time: ' + str(self.cooldown3 // 10), 1090, 60)
                self.cooldown3 -= 1

            for bullet in all_btn_bullets3:
                if not bullet.move2():
                    all_btn_bullets3.remove(bullet)

            if keys[pygame.K_w] and p.usr_y >= 0:
                p.usr_y -= p.speed
            if keys[pygame.K_s] and p.usr_y <= display_height - 50:
                p.usr_y += p.speed
            if keys[pygame.K_a] and p.usr_x >= 0:
                p.usr_x -= p.speed
            if keys[pygame.K_d] and p.usr_x <= 545:
                p.usr_x += p.speed

            if keys[pygame.K_UP] and p.usr_y2 >= 0:
                p.usr_y2 -= p.speed
            if keys[pygame.K_DOWN] and p.usr_y2 <= display_height - 50:
                p.usr_y2 += p.speed
            if keys[pygame.K_LEFT] and p.usr_x2 >= 765:
                p.usr_x2 -= p.speed
            if keys[pygame.K_RIGHT] and p.usr_x2 <= display_width - 50:
                p.usr_x2 += p.speed

            display.blit(kust, (300, 100))
            display.blit(kust1, (1100, 600))
            display.blit(kust2, (80, 500))
            display.blit(kust3, (900, 250))
            self.show_health()
            self.show_health2()
            #bot.move_bot()
            pygame.display.update()
            clock.tick(60)

    def pause(self):
        paused = True

        pygame.mixer.music.pause()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.show_menu()

            print_text('Paused. Press Enter to continue. ESC to menu', 350, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            pygame.display.update()
            clock.tick(15)

        #pygame.mixer.music.unpause()

    def show_health(self):
        show = 0
        x = 20
        while show != self.health:
            display.blit(health_img, (x, 20))
            x += 40
            show += 1

    def show_health2(self):
        show = 0
        x = 1230
        while show != self.health2:
            display.blit(health_img, (x, 20))
            x += 40
            show += 1

    def check_health(self):
        self.health -= 1
        if self.health == 0:
            pygame.mixer.Sound.play(loss_sound)
            return False
        else:
            pygame.mixer.Sound.play(fall_sound)
            return True

    def check_health2(self):
        self.health2 -= 1
        if self.health2 == 0:
            pygame.mixer.Sound.play(loss_sound)
            return False
        else:
            pygame.mixer.Sound.play(fall_sound)
            return True
