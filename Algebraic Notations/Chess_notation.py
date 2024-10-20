import pygame
import chess


# Initialize pygame and chess board
pygame.init()
board = chess.Board()

# Constants for window dimensions and colors
WIDTH, HEIGHT = 600, 750  # Larger window size
BOARD_SIZE = 512  # Chess board size
MARGIN = (WIDTH - BOARD_SIZE) // 2  # To center the board horizontally
TITLE_HEIGHT = 50  # Space for title
MOVE_HEIGHT = 180  # Space for move list at the bottom

SQ_SIZE = BOARD_SIZE // 8
LIGHT_BLUE = (173, 216, 230)  # Light blue for light squares
DARK_BLUE = (70, 130, 180)    # Steel blue for dark squares
HIGHLIGHT_COLOR = (255, 255, 0)  # Yellow highlight for selected square

# UI colors
BACKGROUND_COLOR = (50, 50, 70)  # Dark background
ALTERNATE_MOVE_COLORS = [(230, 230, 255), (210, 230, 255)]  # Alternating colors for move list

# Colors for moves
WHITE_MOVE_COLOR = (25, 53, 73)  # Black text for white moves
BLACK_MOVE_COLOR = (38, 44, 58)  # White text for black moves

# Load chess piece images
pieces = {}
for piece in ['p', 'r', 'n', 'b', 'q', 'k']:
    pieces[f'w_{piece}'] = pygame.image.load(f'pieces/w_{piece}.png')
    pieces[f'b_{piece}'] = pygame.image.load(f'pieces/b_{piece}.png')

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Fonts for the title and moves
title_font = pygame.font.Font(None, 48)
moves_font = pygame.font.Font(None, 28)
moves_number_font = pygame.font.Font(None, 24)

TEXT_COLOR = (255, 255, 255)
INPUT_BOX_COLOR = (255, 0, 0)
font = pygame.font.Font(None, 32)
input_box = pygame.Rect((WIDTH//2) - 200, 625, 400, 50)
input_text = ''


move_list = []  # List to store moves (white on left, black on right)
scroll_offset = 0  # Offset for scrolling moves

def draw_board(selected_square=None):
    """Draw the chessboard with a possible highlighted square."""
    for row in range(8):
        for col in range(8):
            color = LIGHT_BLUE if (row + col) % 2 == 0 else DARK_BLUE
            square_rect = pygame.Rect(MARGIN + col * SQ_SIZE, TITLE_HEIGHT + row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            pygame.draw.rect(screen, color, square_rect)

            # Highlight the selected square
            if selected_square == chess.square(col, 7 - row):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, square_rect, 4)  # Draw a border on the selected square

    # Draw a textbox, to enter the notation of next move
    pygame.draw.rect(screen, INPUT_BOX_COLOR, input_box, 2)
    text_surface = font.render(input_text, True, TEXT_COLOR)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))


def draw_pieces():
    """Draw the pieces on the board based on the current board state."""
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_color = 'w' if piece.color else 'b'
            piece_type = piece.symbol().lower()
            piece_image = pieces[f'{piece_color}_{piece_type}']
            x = MARGIN + chess.square_file(square) * SQ_SIZE + (SQ_SIZE - piece_image.get_width()) // 2
            y = TITLE_HEIGHT + (7 - chess.square_rank(square)) * SQ_SIZE + (SQ_SIZE - piece_image.get_height()) // 2
            screen.blit(piece_image, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

def draw_title():
    """Draw the game title at the top of the screen."""
    title_surface = title_font.render("Chess Game", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(WIDTH // 2, TITLE_HEIGHT // 2))
    screen.blit(title_surface, title_rect)

def get_square_under_mouse():
    """Get the square on the board based on mouse position."""
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = [int((v - MARGIN) // SQ_SIZE) for v in mouse_pos]
    if 0 <= x < 8 and TITLE_HEIGHT <= y * SQ_SIZE + TITLE_HEIGHT < TITLE_HEIGHT + BOARD_SIZE:
        return chess.square(x, 7 - int((mouse_pos[1] - TITLE_HEIGHT) // SQ_SIZE))  # Translate GUI to chess coords
    return None

def is_pawn_promotion(move):
    """Check if the move is a pawn promotion."""
    return board.piece_at(move.from_square).piece_type == chess.PAWN and (chess.square_rank(move.to_square) == 0 or chess.square_rank(move.to_square) == 7)

def pawn_promotion():
    """Handle pawn promotion by prompting the user for promotion type."""
    promotion_type = chess.QUEEN  # Default to queen for simplicity
    return promotion_type

selected_square = None
running = True

# Main loop
while running:
    screen.fill(BACKGROUND_COLOR)  # Fill background with custom dark color
    draw_title()  # Draw title at the top
    draw_board(selected_square)  # Draw the chess board and possibly highlight a square
    draw_pieces()  # Draw pieces on the board

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                move = chess.Move.from_uci(input_text)
                if move in board.legal_moves:
                    print(move)
                    print(board.san(move)) 
                    board.push_san(board.san(move))  # Push the move to the board
                    input_text = ''
                
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
          
    pygame.display.flip()

pygame.quit()
