import pygame

# Creating variables used in this project
_green = (0, 255, 0)
_blue = (0, 0, 128)
_black = (0, 0, 0)
_white = (255, 255, 255)
_height = 500
_width = 500


# Creating Game class(main)
class Game:
    def __init__(self):
        self.board = []
        self.players = [None, None]
        self.boardArea = {
            0: pygame.Rect(90, 90, 100, 100),
            1: pygame.Rect(200, 90, 100, 100),
            2: pygame.Rect(310, 90, 100, 100),
            3: pygame.Rect(90, 200, 100, 100),
            4: pygame.Rect(200, 200, 100, 100),
            5: pygame.Rect(310, 200, 100, 100),
            6: pygame.Rect(90, 310, 100, 100),
            7: pygame.Rect(200, 310, 100, 100),
            8: pygame.Rect(310, 310, 100, 100)
        }
        self.drawArea = [
            [300, 300],
            [500, 300],
            [700, 300],
            [300, 500],
            [500, 500],
            [700, 500],
            [300, 700],
            [500, 700],
            [700, 700]
        ]

    def start(self):
        self.board = [None for _ in range(9)]
        drawBoard()

    def setPlayer(self, n, name, action):
        self.players[n] = {
            "name": name,
            "action": action
        }

    def available(self, pos):
        if self.board[pos] is None:
            return True
        print("Invalid move")
        return False

    def move(self, i, player):
        if self.board[i] is None:
            self.board[i] = player
            self.draw(i, self.players[player]['action'])
            return True
        return False

    def draw(self, position, action):
        if action == 'X':
            drawX(position)
        else:
            drawO(position)
        pygame.display.update()

    def check(self):
        answer = None
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            answer = self.board[0]
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            answer = self.board[0]
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            answer = self.board[0]
        elif self.board[1] == self.board[4] and self.board[7] == self.board[4]:
            answer = self.board[1]
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            answer = self.board[2]
        elif self.board[2] == self.board[4] and self.board[6] == self.board[4]:
            answer = self.board[2]
        return answer

    def checkFull(self):
        for pos in self.board:
            if pos is None:
                return False
        return True


def drawBoard():
    gameDisplay.fill(_white)
    pygame.draw.line(gameDisplay, _black, (200, 100), (200, 400), 10)
    pygame.draw.line(gameDisplay, _black, (100, 200), (400, 200), 10)
    pygame.draw.line(gameDisplay, _black, (300, 100), (300, 400), 10)
    pygame.draw.line(gameDisplay, _black, (100, 300), (400, 300), 10)
    pygame.display.update()


def diplayGameEnd(t):
    gameDisplay.fill((0, 0, 0))
    text = font.render(t, True, _white)
    textRect = text.get_rect()
    textRect.center = (250, 220)
    gameDisplay.blit(text, textRect)
    pygame.display.update()


def drawX(pos):
    text = XO.render('X', True, _black)
    textRect = text.get_rect()
    textRect.center = (game.drawArea[pos][0] // 2, game.drawArea[pos][1] // 2)
    gameDisplay.blit(text, textRect)


def drawO(pos):
    text = XO.render('O', True, _black)
    textRect = text.get_rect()
    textRect.center = (game.drawArea[pos][0] // 2, game.drawArea[pos][1] // 2)
    gameDisplay.blit(text, textRect)


playArea = pygame.Rect(220, 290, 50, 20)

def displayPlay():
    text = playFont.render("Play", True, _white)
    textRect = text.get_rect()
    textRect.center = (250, 300)
    gameDisplay.blit(text, textRect)
    pygame.display.update()


pygame.init()

# screen = pygame.display.Info()
gameDisplay = pygame.display.set_mode((_width, _height))
pygame.display.set_caption('Tik Tak Toe')
clock = pygame.time.Clock()
XO = pygame.font.SysFont("Arial", 70)
font = pygame.font.SysFont("Arial", 40)
playFont = pygame.font.SysFont("Arial", 20)
gameDisplay.fill((0, 0, 0))
text = font.render("Welcome", True, _white)
textRect = text.get_rect()
textRect.center = (250, 220)
gameDisplay.blit(text, textRect)
pygame.display.update()
game = Game()


def togglePlayer(p):
    if p == 1:
        return 0
    return 1


def mainloop():
    game.setPlayer(0, "Player 1", "X")
    game.setPlayer(1, "Player 2", "O")
    game.start()
    result = True
    active = 0
    while result:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range(9):
                        if game.boardArea[i].collidepoint(event.pos):
                            if game.available(i):
                                if game.move(i, active):
                                    active = togglePlayer(active)
                                    winned = game.check()
                                    if not winned is None:
                                        result = False
                                        diplayGameEnd(game.players[winned]['name'] + " Won")
                                    elif game.checkFull():
                                        result = False
                                        diplayGameEnd("Game Tied")
                            break
    return True


def MenuLoop():
    displayPlay()
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if playArea.collidepoint(event.pos):
                        menu = False

    return True


running = True
while True:
    running = MenuLoop()
    if not running:
        pygame.quit()
        break
    running = mainloop()
    if not running:
        pygame.quit()
        break