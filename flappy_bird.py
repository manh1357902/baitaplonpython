from email.mime import image
import pygame
import random

pygame.init()
#bắt đầu
start = 0
start2 =0
start_1=0
check_1=0
check_2= 0
check_3=0
check_4=0
game_over = 0
game_over_2 = 0
pipe_frequency = 2000
last_pipe = pygame.time.get_ticks() - pipe_frequency
last_pipe_2 = pygame.time.get_ticks() - pipe_frequency
p_pass = 0
p_pass_2 = 0
score = 0
score2 = 0
#màn hình
width = 1200
height = 900
displaysurf = pygame.display.set_mode((width,height))
font = pygame.font.SysFont('Bauhaus 93', 60)
#set up tên cửa sổ
pygame.display.set_caption('Flappy Bird')
#background + sàn
floor = pygame.image.load('img/ground.png')
floor = pygame.transform.scale(floor,(width+70,168))
floor_1 = pygame.transform.scale(floor,(width//2+70,168))
floor_move =0
floor_move_2=width//2
background = pygame.image.load('img/bg.png')
background = pygame.transform.scale(background,(width,height)) 
botton_load = pygame.image.load('img/restart.png')
botton_1 = pygame.image.load('img/1player.png')
botton_1 = pygame.transform.scale(botton_1,(160,100))
botton_2 = pygame.image.load('img/2player.png')
botton_2 = pygame.transform.scale(botton_2,(160,100))
#âm thanh
bird_wing = pygame.mixer.Sound('sound/sfx_wing.wav')
# bird_die = pygame.mixer.Sound('sound/sfx_die.wav')
bird_point = pygame.mixer.Sound('sound/sfx_point.wav')
# bird_swooshing = pygame.mixer.Sound('sound/sfx_swooshing.wav')
bird_hit = pygame.mixer.Sound('sound/sfx_hit.wav')
#Chim
class Bird(pygame.sprite.Sprite) :
    def __init__(self,x,y):
        super(Bird, self).__init__()
        self.imgs = []
        self.count = 0
        self.index = 0
        self.v=0
        for i in range(1,4):
            self.imgs.append(pygame.image.load(f'img/bird{i}.png'))
        self.image = self.imgs[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    #chuyển động chim
    def update(self):
        #rơi
        if start == 1:
            self.v += 0.7
            if self.rect.bottom < height-132:
                self.rect.y += int(self.v)  
            if self.v == 8:
                self.v = 8  
        #bay
        if game_over == 0:
            if pygame.key.get_pressed()[pygame.K_SPACE]==1:
                bird_wing.play()
                self.v = 0
                self.v -= 10    
            self.count += 1
            if self.index == len(self.imgs):
                self.index = 0
            self.image = self.imgs[self.index]
            self.image  = pygame.transform.rotate(self.image,self.v*-1)
            if self.count > 11:
                self.index += 1
                self.count = 0    
        else:        
            self.image  = pygame.transform.rotate(self.imgs[0],-90)
class Bird_2(pygame.sprite.Sprite) :
    def __init__(self,x,y):
        super(Bird_2, self).__init__()
        self.imgs = []
        self.count = 0
        self.index = 0
        self.v=0
        for i in range(1,4):
            self.imgs.append(pygame.transform.scale(pygame.image.load(f'img/bird_{i}.png'),(51,36)))
        self.image = self.imgs[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    #chuyển động chim
    def update(self):
        #rơi
        if start2 == 1:
            self.v += 0.7
            if self.rect.bottom < height-132:
                self.rect.y += int(self.v)  
            if self.v == 8:
                self.v = 8  
        #bay
        if game_over_2 == 0:
            if pygame.mouse.get_pressed()[2]==1:
                bird_wing.play()
                self.v = 0
                self.v -= 10           
            self.count += 1
            if self.index == len(self.imgs):
                self.index = 0
            self.image = self.imgs[self.index]
            self.image  = pygame.transform.rotate(self.image,self.v*-1)
            if self.count > 11:
                self.index += 1
                self.count = 0    
        else:        
            self.image  = pygame.transform.rotate(self.imgs[0],-90)            
#ống nước
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y,pos):
        super(Pipe,self).__init__()
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        if pos == -1:
            self.rect.topleft = (x,y+100)
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = (x,y-100)
    def update(self):
        self.rect.x -=4
        if self.rect.right < 0:
            self.kill() 
class Pipe2(pygame.sprite.Sprite):
    def __init__(self, x,y,pos):
        super(Pipe2,self).__init__()
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        if pos == -1:
            self.rect.topleft = (x,y+100)
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = (x,y-100)
    def update(self):
        self.rect.x -=4
        if self.rect.right < width//2+90:
            self.kill()            
#nút             
class Botton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.x = x
        self.y = y
    def draw(self):
        displaysurf.blit(self.image,(self.x,self.y))    
    def check(self):
        action = 0
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = 1 
        return action           
bird = Bird(100,int(height/2))
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
bird_group.add(bird)
botton = Botton(int(width/2)-60,int(height/2),botton_load)
bird1 = Bird_2(width//2+100,int(height/2))
bird_group_2 = pygame.sprite.Group()
bird_group_2.add(bird1)
pipe_group_2 = pygame.sprite.Group()
floor_2 = pygame.transform.scale(floor,(20,168))
#vẽ chữ
def draw_text(text,font,color,x,y):
    img = font.render(text,True, color)
    displaysurf.blit(img,(x,y))
botton1 = Botton(int(width/2)-260,int(height/2)-200,botton_1)   
botton2 = Botton(int(width/2)+100,int(height/2)-200,botton_2)    
seperate = pygame.image.load('img/ngancach.png')
seperate = pygame.transform.scale(seperate,(10,height))
floor_3 = pygame.image.load('img/aa.png')
floor_3 = pygame.transform.scale(floor_3,(20,168))
clock = pygame.time.Clock()
    
run =1
while run:         
    clock.tick(60)   
    displaysurf.blit(background,(0,0))  
    if start == 0:
        displaysurf.blit(pygame.transform.scale(background,(width,height)) ,(0,0))
        botton1.draw()
        botton2.draw() 
        if botton1.check() and start == 0 and game_over == 0:
            start_1 = 0
            start = 1  
            check_1=0 
            check_3=0 
        if botton2.check() and start == 0 and game_over == 0 and start2 ==0 and game_over_2 == 0:
            start_1 = 1
            start = 1
            start2 = 1     
            check_2=0
            check_1=0  
            check_3 = 0
            check_4=0
    if start_1 == 0:   
        background = pygame.transform.scale(background,(width,height))
        if start == 1 and game_over ==0  :
            if check_3 == 0:
                displaysurf.blit(pygame.transform.scale(pygame.image.load('img/bird1.png'),(51,36)),(100,height//2))
            if pygame.key.get_pressed()[pygame.K_SPACE]==1:
                check_3 = 1 
            if check_3:
                bird_group.draw(displaysurf) 
                bird_group.update()  
                pipe_group.draw(displaysurf)
        #kiem tra va cham
        if check_3:
            if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or bird.rect.top < 0:
                if game_over== 0:
                    bird_hit.play()
                game_over = 1 
            if bird.rect.bottom >=height-132:
                if game_over == 0:
                    bird_hit.play()
                game_over = 1
            displaysurf.blit(floor,(floor_move,height -132))  
            #di chuyển ống + sàn
            if game_over == 0 and start == 1:
                pipe_now = pygame.time.get_ticks()
                if pipe_now - last_pipe > pipe_frequency and start ==1:
                    pipe_h = random.randint(-200,200)
                    top_pipe = Pipe(width,int(height/2)+pipe_h,1)
                    bottom_pipe = Pipe(width,int(height/2)+pipe_h-30,-1)
                    pipe_group.add(bottom_pipe)
                    pipe_group.add(top_pipe)
                    last_pipe = pipe_now
                if floor_move <= -40:
                    floor_move = 0    
                floor_move -=4
                pipe_group.update() 
            #điểm    
            if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and  bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and p_pass == 0:
                    p_pass = 1  
                if p_pass == 1 and bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:    
                    bird_point.play()
                    score += 1
                    p_pass = 0
            if start ==1:
                draw_text(str(score),font,(255,255,255,255),int(width/2),0)
            #restart
            if game_over == 1 and start ==1:
                botton.draw() 
                if botton.check():
                    start = 0
                    pipe_group.empty()
                    bird.rect.x = 100
                    bird.rect.y = int(height / 2)
                    score = 0
                    game_over = 0
                    bird.v=0
    else:
        #player 1
        displaysurf.blit(background,(0,0))  
        if start == 1:
            if check_1 == 0:
                displaysurf.blit(pygame.transform.scale(pygame.image.load('img/bird1.png'),(51,36)),(100,height//2))
            if pygame.key.get_pressed()[pygame.K_SPACE]==1:
                check_1 = 1 
            if check_1:
                check_4 = 1
                bird_group.draw(displaysurf)
                bird_group.update()  
                pipe_group.draw(displaysurf)
            #kiem tra va cham
        if check_1:    
            if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or bird.rect.top < 0:
                if game_over == 0:
                    bird_hit.play()
                game_over = 1 
            if bird.rect.bottom >=height-132:
                if game_over == 0:
                    bird_hit.play()
                game_over = 1
            displaysurf.blit(floor_1,(floor_move,height -132))  
            #di chuyển ống + sàn
            if game_over == 0 and start == 1:
                pipe_now = pygame.time.get_ticks()
                if pipe_now - last_pipe > pipe_frequency and start ==1:
                    pipe_h = random.randint(-200,200)
                    top_pipe = Pipe(width//2,int(height/2)+pipe_h,1)
                    bottom_pipe = Pipe(width//2,int(height/2)+pipe_h-20,-1)
                    pipe_group.add(bottom_pipe)
                    pipe_group.add(top_pipe)
                    last_pipe = pipe_now
                if floor_move <= -40:
                    floor_move = 0    
                floor_move -=4
                pipe_group.update() 
            if game_over == 1:
                displaysurf.blit(floor,(floor_move,height -132))       
            #điểm    
            if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and  bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and p_pass == 0:
                    p_pass = 1  
                if p_pass == 1 and bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:  
                    bird_point.play()  
                    score += 1
                    p_pass = 0
            if start ==1:
                draw_text(str(score),font,(255,255,255,255),int(width/4),0)  
        #player2        
        displaysurf.blit(background,(width//2,0)) 
        if start2 == 1:
            if check_2 == 0 :
                displaysurf.blit(pygame.transform.scale(pygame.image.load('img/bird_1.png'),(51,36)),(width//2+100,height//2))
            if  pygame.mouse.get_pressed()[2]==1:
                check_2=1 
            if check_2==1:   
                bird_group_2.draw(displaysurf) 
                bird_group_2.update()  
                pipe_group_2.draw(displaysurf)  
            #kiem tra va cham
                if pygame.sprite.groupcollide(bird_group_2,pipe_group_2,False,False) or bird1.rect.top < 0:
                    if game_over_2 == 0:
                        bird_hit.play()
                    game_over_2 = 1 
                if bird1.rect.bottom >=height-132:
                    if game_over_2 == 0:
                        bird_hit.play()
                    game_over_2 = 1
                displaysurf.blit(floor_1,(floor_move_2,height-132))  
                #di chuyển ống + sàn
                if game_over_2 == 0 and start2 == 1:
                    pipe_now_1 = pygame.time.get_ticks()
                    if pipe_now_1 - last_pipe_2 > pipe_frequency and start2 ==1:
                        pipe_h = random.randint(-200,200)
                        top_pipe = Pipe2(width,int(height/2)+pipe_h,1)
                        bottom_pipe = Pipe2(width,int(height/2)+pipe_h-20,-1)
                        pipe_group_2.add(bottom_pipe)
                        pipe_group_2.add(top_pipe)
                        last_pipe_2 = pipe_now_1
                    if floor_move_2 <= width//2-20:
                        floor_move_2 = width//2  
                    floor_move_2 -=4
                    pipe_group_2.update() 
                #điểm    
                if len(pipe_group_2):
                    if bird_group_2.sprites()[0].rect.left > pipe_group_2.sprites()[0].rect.left and  bird_group_2.sprites()[0].rect.right < pipe_group_2.sprites()[0].rect.right and p_pass_2 == 0:
                        p_pass_2 = 1  
                    if p_pass_2 == 1 and bird_group_2.sprites()[0].rect.left > pipe_group_2.sprites()[0].rect.right:    
                        bird_point.play()
                        score2 += 1
                        p_pass_2 = 0
                if start2 ==1:
                    draw_text(str(score2),font,(255,255,255,255),int(width*3/4),0)  
            if check_1 and check_2:        
                displaysurf.blit(floor_2,(width//2-20,height-132))    
            if check_4 == 0 and check_2 ==1:
                displaysurf.blit(floor_3,(width//2-20,height-132))            
            displaysurf.blit(seperate,(width//2,0)) 
            #restart
            if game_over == 1 and start ==1 and game_over_2==1 and start2==1:
                displaysurf.blit(pygame.transform.scale(background,(width,height)),(0,0))
                botton.draw() 
                if botton.check():
                    start = 0
                    start2=0
                    pipe_group.empty()
                    pipe_group_2.empty()
                    bird.rect.x = 100
                    bird.rect.y = int(height / 2)
                    bird1.rect.x = width//2+100
                    bird1.rect.y = int(height / 2)
                    bird1.v=0
                    bird.v = 0
                    score = 0
                    score2 = 0
                    game_over = 0
                    game_over_2 = 0  
                    background = pygame.transform.scale(background,(width//2,height))       
    if start == 0:
        displaysurf.blit(pygame.transform.scale(background,(width,height)) ,(0,0))
        botton1.draw()
        botton2.draw() 
        if botton1.check() and start == 0 and game_over == 0:
            start_1 = 0
            start = 1  
            check_1=0  
        if botton2.check() and start == 0 and game_over == 0 and start2 ==0 and game_over_2 == 0:
            start_1 = 1
            start = 1
            start2 = 1     
            check_2=0
            check_1=0  
            check_3 = 0   
            check_4 = 0     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0                  
    pygame.display.update()
  
pygame.quit()