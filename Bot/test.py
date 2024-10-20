import chess

board = chess.Board()

def bot_move(mode):
    moves = list(board.legal_moves)
    
    if mode == 'easy':
        return random.choice(moves) if moves else None
    elif mode == 'medium':
        captures = [move for move in moves if board.is_capture(move)]
        if captures:
            piece_values = {chess.PAWN: 1, chess.KNIGHT: 3,
                            chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
            captures_by_value = {}
            for capture in captures:
                value = piece_values[board.piece_at(
                    capture.to_square).piece_type]
                captures_by_value.setdefault(value, []).append(capture)
            best_captures = captures_by_value[max(captures_by_value.keys())]
            return random.choice(best_captures)
        return random.choice(moves)
    return None




import random

def medium_mode_move(): 
    moves = list(board.legal_moves)
    best_move = None
    best_score = float('-inf')
    for move in moves:
        make_move(move)
        score = evaluate_board()
        undo_move(move)
        if score > best_score:
            best_score = score
            best_move = move
    make_move(best_move)

def make_move(move):
    # Implement logic to make a move on the board
    pass
def evaluate_board():
    # Implement a basic evaluation function for the board
    pass
def undo_move(move):
    # Implement logic to undo a move on the board
    pass


def hard_mode_move():
    depth = 3  # Depth for Minimax
    best_move = minimax(depth, float('-inf'), float('inf'), True)[1]
    make_move(best_move)

def minimax(depth, alpha, beta, is_maximizing):
    if depth == 0 or list(board.legal_moves):
        return evaluate_board(), None

    valid_moves = list(board.legal_moves)
    best_move = None

    if is_maximizing:
        max_eval = float('-inf')
        for move in valid_moves:
            make_move(move)
            eval = minimax(depth - 1, alpha, beta, False)[0]
            undo_move(move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in valid_moves:
            make_move(move)
            eval = minimax(depth - 1, alpha, beta, True)[0]
            undo_move(move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move