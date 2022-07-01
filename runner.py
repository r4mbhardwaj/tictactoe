import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:

    for event in pygame.event.get(): # event handling loop
        if event.type == pygame.QUIT: # window close button clicked
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None: # User hasn't chosen a player yet.

        # user choosing screen openning

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton) # Draw X button
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton) # Draw O button
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed() # Get mouse position
        if click == 1: # Mouse is clicked
            mouse = pygame.mouse.get_pos() # Get mouse position
            if playXButton.collidepoint(mouse): # If X button is clicked
                time.sleep(0.2)
                user = ttt.X # User is X
            elif playOButton.collidepoint(mouse): # If O button is clicked
                time.sleep(0.2)
                user = ttt.O # User is O

    else: # User has chosen a player.

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3): # Draw 3x3 board
            row = [] # Create a new row
            for j in range(3): # Draw 3 tiles per row
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size, # Tile is tile_size wide
                    tile_origin[1] + i * tile_size, # Tile is tile_size tall
                    tile_size, tile_size # Tile is tile_size wide and tall
                )
                pygame.draw.rect(screen, white, rect, 3) # Draw tile

                if board[i][j] != ttt.EMPTY: # Draw X or O on tile (if not empty)
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect) # Add tile to row
            tiles.append(row) # Add row to board
        
        game_over = ttt.terminal(board) # Check if game is over
        player = ttt.player(board) # Check if it's user's turn

        # Show title
        if game_over: # If game is over
            winner = ttt.winner(board) # Get winner
            if winner is None: # If tie
                title = f"Game Over: Tie."
            else: # If there is a winner
                title = f"Game Over: {winner} wins."
        elif user == player: # If it's user's turn
            title = f"Play as {user}"
        else: # If it's AI's turn
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white) # Draw title
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect) # Draw title

        # Check for AI move
        if user != player and not game_over: # If it's AI's turn
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed() # Get mouse position
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse): # If again button is clicked
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip() # flip the display
