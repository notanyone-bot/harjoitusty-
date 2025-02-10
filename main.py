import pygame as p
import engine

WIDTH = HEIGHT = 512
DIMENSION = 8
MAX_FPS = 15
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}


def loadImages():
    pieces = ["wP", "wR", "wN", "wB", "wK", "wQ", "bP", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# user input and update graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # merkkimuuttujaa kun siirto tehdään
    loadImages()
    running = True
    sqSelected = () # pitää kirjaa vikasta klikista (tuple: (row, col))
    playerClicks = [] # myös pitää kirjaa klikeista (two tuples: (1, 1), (2, 1))
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # hiiri
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = () #valinta pois
                    playerClicks = [] # klikkien nollaaminen
                else :
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #appendataan eka ja toka klikki
                if len (playerClicks) == 2: # toisen klikin jälkein
                    move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = ()  # nollaa käyttäjän klikit
                    playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # takaisin kun painaa "z"
                    gs.undoMove() 
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, gs)

# vastaa graafiksasta
def drawGameState(screen, gs):
    drawBoard(screen) # Draw squares on the board
    drawPieces(screen, gs.board) # Draw pieces on the board

# piirtäää neliöt lautaan
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# piirtttää nappulat käyttäen tämänhetkistä GameState.board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # If empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()