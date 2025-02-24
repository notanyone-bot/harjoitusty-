import pygame as p
import engine, chessAI

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
    gameOver = False
    playerOne = False # jos ihminen pelaa valkoisilla, niin tämä on True, jos AI False
    playerTwo = False # sama, kuin yllä, mutta mustille
    while running:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # hiiri
            elif e.type == p.MOUSEBUTTONDOWN and not gameOver:
                if not gameOver and humanTurn:
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
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                sqSelected = ()  # nollaa käyttäjän klikit
                                playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # takaisin kun painaa "z"
                    gs.undoMove() 
                    moveMade = True
                elif e.key == p.K_r:  # restarttaa peli jos painaa "r"
                    gs = engine.GameState()
                    validMoves = gs.getValidMoves()
                    moveMade = False
                    gameOver = False  # restarttaa game state

        # AI askel etsintä
        if not gameOver and not humanTurn:
            AIMove = chessAI.findRandomMove(validMoves)
            gs.makeMove(AIMove)
            moveMade = True


        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen, gs, validMoves, sqSelected)
        print(f"Checkmate: {gs.checkmate}, Stalemate: {gs.stalemate}")
        if gs.checkmate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, "Black wins by checkmate")
            else:
                drawText(screen, "White wins by checkmate")
        elif gs.stalemate:
            gameOver = True
            drawText(screen, "Stalemate")
        
        clock.tick(MAX_FPS)
        p.display.flip()

def highlightSqeares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ("w" if gs.whiteToMove else "b"):
            # maalaa valittu nappula
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(p.Color("blue"))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            # maalaa mahdolliset liikkeet
            s.fill(p.Color("yellow"))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol*SQ_SIZE, move.endRow*SQ_SIZE))


# vastaa graafiksasta
def drawGameState(screen, gs, validMoves, sqSelected):
    drawBoard(screen) # Draw squares on the board
    highlightSqeares(screen, gs, validMoves, sqSelected)
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

def drawText(screen, text):
    font = p.font.SysFont("Helvitca", 32, True, False)
    textObject = font.render(text, 0, p.Color("Black"))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)

if __name__ == "__main__":
    main()