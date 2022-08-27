import pygame
import random

pygame.init()               # 초기화 (중요)

# 화면 크기 설정
screen_width = 480          # 가로 
screen_height = 640         # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 회면 타이틀 설정
pygame.display.set_caption("Game")               # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 캐릭터 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size              # 이미지의 크기를 구해옴
character_width = character_size[0]              # 캐릭터의 가로 크기
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 점수판 점수 변수 정의
score = 0

# 캐릭터 이동 속도
character_speed = 0.6

# 적 위치 램덤 생성
px_of_enemy = random.randint(0, 420)
py_of_enemy = random.randint(0, 500)

# 적(enemy) 캐릭터
enemy  = pygame.image.load("yellow.png")
enemy_size = enemy.get_rect().size        # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]               # 적 가로 크기
enemy_height = enemy_size[1]              # 적 세로 크기
enemy_x_pos = px_of_enemy
enemy_y_pos = py_of_enemy

# 게임폰트 정의
moveFont = pygame.font.Font(None, 50)  

# 이벤트 루프
running = True              # 게임이 진행 중인가?
while running:
       dt = clock.tick(60) # 초당 플레임 설정(해상도)

       for event in pygame.event.get():          # 어떤 이벤트가 발생하였는가?
              if event.type == pygame.QUIT:             # 창이 단히는 이벤트가 발생하였는가?
                     running = False             # 게임이 진행 중이 아님
              
              if event.type == pygame.KEYDOWN:   # 키가 눌렀을 때(작동)
                     if event.key == pygame.K_LEFT:             # LEFT 키
                            to_x -= character_speed
                     elif event.key == pygame.K_RIGHT:          # RIGHT 키
                            to_x += character_speed
                     elif event.key == pygame.K_UP:             # UP 키
                            to_y -= character_speed
                     elif event.key == pygame.K_DOWN:           # DOWN 키
                            to_y += character_speed
              
              if event.type == pygame.KEYUP:     # 키를 떼었을 때(멈춤)
                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            to_x = 0
                     elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            to_y = 0

       character_x_pos += to_x*dt
       character_y_pos += to_y*dt

       # 가로 경계값 처리(벽)
       if character_x_pos < 0:
              character_x_pos = 0
       elif character_x_pos > screen_width - character_width:
              character_x_pos = screen_width - character_width

       # 세로 경계값 처리(벽)
       if character_y_pos < 0:
              character_y_pos = 0
       elif character_y_pos > screen_height - character_height:
              character_y_pos = screen_height - character_height

       # 충돌 처리를 위한 rect 정보 업데이트
       character_rect = character.get_rect()
       character_rect.left = character_x_pos
       character_rect.top = character_y_pos

       enemy_rect = enemy.get_rect()
       enemy_rect.left = enemy_x_pos
       enemy_rect.top = enemy_y_pos

       # 충돌 체크
       if character_rect.colliderect(enemy_rect):
              print("충돌")
              # 적 위치 램덤 생성
              px_of_enemy = random.randint(0, 420)
              py_of_enemy = random.randint(0, 500)
              enemy_x_pos = px_of_enemy
              enemy_y_pos = py_of_enemy
              score += 100

       screen.blit(background, (0,0))            # 배경 그리기

       screen.blit(character, (character_x_pos, character_y_pos))            # 캐릭터 그리기
       screen.blit(enemy, (enemy_x_pos, enemy_y_pos))                 # 적 그리기

       scoreText = moveFont.render(str(score) ,True,(255,255,255))                # 출력글, 글자색상 정의 
       screen.blit(scoreText, (15, 10))                            # 점수판 그리기

       pygame.display.update()            # 게임화면을 다시 그리기

pygame.quit()               # pygame 종료