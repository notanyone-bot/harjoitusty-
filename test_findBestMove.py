import pytest
from chessAI import findBestMove

# Fake game state class, voit muokata tätä tarvittaessa
class GameState:
    def __init__(self):
        self.whiteToMove = True
        self.checkMate = False
        self.staleMate = False
        self.board = [[None] * 8 for _ in range(8)]

    def getValidMoves(self):
        # Palauttaa esimerkkilistan siirroista
        return ['e2e4', 'd2d4']

    def makeMove(self, move):
        pass

    def undoMove(self):
        pass

# Testi normaalille pelitilanteelle
def test_findBestMove_normal_case():
    gs = GameState()
    validMoves = gs.getValidMoves()
    
    move, moves, score = findBestMove(gs, validMoves)
    
    assert move is not None
    assert moves == validMoves
    assert isinstance(score, int)  # score pitäisi olla kokonaisluku

# Testi mattitilanteelle
def test_findBestMove_checkmate():
    gs = GameState()
    gs.checkMate = True  # Asetetaan mattitilanne
    validMoves = gs.getValidMoves()

    move, moves, score = findBestMove(gs, validMoves)
    
    assert move is None
    assert moves == validMoves
    assert score == -CHECKMATE  # Mattitilanteessa score on negatiivinen CHECKMATE

# Testi pattitilanteelle
def test_findBestMove_stalemate():
    gs = GameState()
    gs.staleMate = True  # Asetetaan pattitilanne
    validMoves = gs.getValidMoves()

    move, moves, score = findBestMove(gs, validMoves)
    
    assert move is None
    assert moves == validMoves
    assert score == 0  # Pattitilanteessa score on 0

# Testi, jossa ei ole mattia eikä pattia
def test_findBestMove_no_checkmate_or_stalemate():
    gs = GameState()
    gs.checkMate = False
    gs.staleMate = False
    validMoves = gs.getValidMoves()
    
    move, moves, score = findBestMove(gs, validMoves)
    
    assert move is not None
    assert moves == validMoves
    assert isinstance(score, int)  # score on kokonaisluku, ei mattitilanteessa
