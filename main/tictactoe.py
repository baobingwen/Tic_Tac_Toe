import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BOARD_COLOR = WHITE

class Tictactoe:
    def __init__(self, board_size = 3, tile_size = 80):
        
        # 前端初始化棋盘
        self.board_size = board_size
        self.tile_size = tile_size
        self.border_size = tile_size

        self.width = self.height = (self.board_size + 1) * self.tile_size

        self.display_width = self.width + self.border_size
        self.display_height = self.height + self.border_size

        pygame.init()
        pygame.display.set_caption("Tictactoe")
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        self.font = pygame.font.Font(None, 36)

        # 后端初始化棋盘

        # 3*3的棋盘
        self.board = [['.' for _ in range(0, self.board_size + 2)] for _ in range(0, self.board_size + 2)]
        # 边界一周（0和board_size+1）为既叉（noughts）又圈（crosses）不可行棋区
        for x in range(self.board_size + 2):
            self.board[x][0] = '*'
            self.board[x][self.board_size + 1] = '*'
        for y in range(self.board_size + 2):
            self.board[0][y] = '*'
            self.board[self.board_size + 1][y] = '*'

        # 当前棋子颜色
        self.player = 'N'

    # 前端绘制棋盘
    def draw_board(self):

        self.screen.fill(BOARD_COLOR)

        # 绘制网格线
        for x in range(1, self.board_size + 2):
            pygame.draw.line(self.screen, BLACK, (x * self.tile_size, self.tile_size), (x * self.tile_size, (self.board_size + 1) * self.tile_size), 2)
        for y in range(1, self.board_size + 2):
            pygame.draw.line(self.screen, BLACK, (self.tile_size, y * self.tile_size), ((self.board_size + 1) * self.tile_size, y * self.tile_size), 2)

    # 前端绘制开始界面
    def start_game(self):
        pass

    # 前端消息界面
    def draw_message(self, message):
        self.screen.fill(WHITE)
        text = pygame.font.Font(None, 74).render(message, True, BLACK)
        self.screen.blit(text, (self.display_width // 2 - text.get_width() // 2, self.display_height // 2 - text.get_height() // 2))
    
    # 前端绘制胜利界面
    def draw_Win_Screen(self, winner):
        
        self.draw_message(winner+' wins!')

    # 前端绘制平局界面
    def draw_Draw_Screen(self):
        
        self.draw_message('It\'s a draw!')

    # 前端绘制棋子
    def draw_tiles(self):
        for x in range(1, self.board_size + 1):
            for y in range(1, self.board_size + 1):
                if self.board[x][y] != '.':

                    # 计算棋子的中心位置，确保它位于网格中心
                    center_x = (x+0.5) * self.tile_size
                    center_y = (y+0.5) * self.tile_size

                    # 黑棋，即crosses
                    if self.board[x][y] == 'C':
                        # crosses
                        pygame.draw.line(self.screen, BLACK, (center_x - self.tile_size // 3, center_y - self.tile_size // 3), (center_x + self.tile_size // 3, center_y + self.tile_size // 3), 6)
                        pygame.draw.line(self.screen, BLACK, (center_x + self.tile_size // 3, center_y - self.tile_size // 3), (center_x - self.tile_size // 3, center_y + self.tile_size // 3), 6)

                    # 白棋，即noughts
                    else :
                        # noughts
                        pygame.draw.circle(self.screen, BLACK, (int(center_x), int(center_y)), self.tile_size // 2 - 8, 0)
    # 后端落子
    def drop_tiles(self, pos):
        # 处理棋子位置
        x, y = pos
        
        x //= self.tile_size
        y //= self.tile_size

        if 1 <= x <= self.board_size and 1 <= y <= self.board_size and self.board[x][y] == '.':
            self.board[x][y] = self.player
            self.player = 'C' if self.player == 'N' else 'N'

    # 后端判断棋局状态
    def judge_state(self):
        # 胜利
        for x in range(1, self.board_size + 1):
            tmp_tile = self.board[x][1]
            if tmp_tile == '.':
                continue
            for y in range(2, self.board_size + 1):
                if tmp_tile != self.board[x][y]:
                    break
            else:
                # print(tmp_tile, 'wins!')
                return 'WIN',tmp_tile
            
        for y in range(1, self.board_size + 1):
            tmp_tile = self.board[1][y]
            if tmp_tile == '.':
                continue
            for x in range(2, self.board_size + 1):
                if tmp_tile != self.board[x][y]:
                    break
            else:
                # print(tmp_tile, 'wins!')
                return 'WIN',tmp_tile
        
        for x in range(1):
            # 对角线检测
            tmp_tile = self.board[1][1]
            if tmp_tile == '.':
                break
            for x in range(2, self.board_size + 1):
                if self.board[x][x] != tmp_tile:
                    break
            else:
                # print(tmp_tile, 'wins!')
                return 'WIN',tmp_tile
        
        for x in range(1):
            # 反对角线检测
            tmp_tile = self.board[self.board_size][1]
            
            if tmp_tile == '.':
                break
            for x in range(2, self.board_size + 1):
                if self.board[self.board_size - x + 1][x] != tmp_tile:
                    break
            else:
                #print(1)
                #game.draw_Win_Screen(tmp_tile)
                return 'WIN',tmp_tile

        
        # 平局
        for x in range(1, self.board_size + 1):
            for y in range(1, self.board_size + 1):
                # 尚未分出胜负
                if self.board[x][y] == '.':
                    return 'gaming'
        print(2)
        # print('draw')
        return 'draw'
                
    
if __name__ == '__main__':
    game = Tictactoe(board_size=3, tile_size = 80)
    pygame.init()
    pygame.display.set_caption("Tictactoe")
    game.screen = pygame.display.set_mode((game.display_width, game.display_height))
    game.font = pygame.font.Font(None, 36)

    judge_state = 'gaming'

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 左键点击
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                game.drop_tiles(event.pos)
                for x in range(5):
                    print(game.board[x])
        
        if judge_state == 'gaming':
            game.draw_board()
            game.draw_tiles()
            judge_state = game.judge_state()
        elif judge_state == 'draw':
            game.draw_Draw_Screen()
        else:
            if judge_state[1] == 'N':
                game.draw_Win_Screen('Nought')
            else:
                game.draw_Win_Screen('Cross')
            
        pygame.display.flip()