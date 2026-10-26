bb = 0 # Blanks
xx = 1
oo = -1

ai = None
human = None

def best_move(board):
    best_score = float('-inf')
    move = None

    for i in range(len(board)):
        # Check if spot is available
        if board[i] == bb:
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = bb
            if score > best_score:
                best_score = score
                move = i
        #print(move)

    #print(f"Best move: {move}")

    return move

def minimax(board, depth, is_maximizing):    
    winner = check_winner(board)    
    free_spaces = board.count(bb)

    if free_spaces <= 1:
        return 0

    # Future ref: Idk how i arrived to this, but it seems to work in terms of the AI being difficult to beat
    # I was just doing trial and error and seeing what crap sticks
    if human == oo: # If human is second-mover
        if winner == ai:
            return ai
        elif winner == human:
            return human
    elif human == xx: # If human is first-mover
        if winner == ai:
            return human
        elif winner == human:
            return ai

    if is_maximizing:
        best_score = float('-inf')
        for i in range(len(board)):
            # Check if spot is available
            if board[i] == bb:
                board[i] = ai

                #print("\n===maximizing")
                #print_board(board)
                
                score = minimax(board, depth + 1, False)
                
                board[i] = bb
                
                best_score = max(best_score, score)

                #print(f"Maximizing: {best_score}, {score}")

        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            # Check if spot is available
            if board[i] == bb:
                board[i] = human
                
                #print("\n===minimizing")
                #print_board(board)
                
                score = minimax(board, depth + 1, True)

                board[i] = bb
                best_score = min(best_score, score)

                #print(f"Minimizing: {best_score}, {score}")

        return best_score

def check_winner(board):
    winner = None

    # Row check
    for i in range(0, len(board), 3):
        if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != bb:
            winner = board[i]
        #if all(p == xx for p in board[i:i+3]):
            

    # Column check
    for i in range(0, len(board) // 3):
        if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != bb:
            winner = board[i]
        #if all(p == xx for p in [board[i], board[i+3], board[i+6]]):
            

    # Diagonal check
    topleft_diagonal = board[0] == board[4] and board[4] == board[8] and board[0] != bb
    topright_diagonal = board[2] == board[4] and board[4] == board[6] and board[2] != bb
    
    if topleft_diagonal:
        winner = board[0]
    elif topright_diagonal:
        winner = board[2]

    return winner

def print_board(board):

    b = board
    b = ['-' if x == 0 or x == None else x for x in b]
    b = ['o' if x == oo else x for x in b]
    b = ['x' if x == xx else x for x in b]
    
    
    print(f"""
        {b[0]}, {b[1]}, {b[2]},
        {b[3]}, {b[4]}, {b[5]},
        {b[6]}, {b[7]}, {b[8]},
          """)

def main():
    
    board = [
        bb, bb, bb,
        bb, bb, bb,
        bb, bb, bb    
    ]

    global human
    global ai
    
    player = input("Pick 'x' or 'o': ")
    if player == 'x':
        human = xx 
        ai = oo
    else:
        human = oo 
        ai = xx

    # Initial AI turn

    if ai == xx:
        ai_move = best_move(board)
        board[ai_move] = ai
        
    while check_winner(board) == None:
        print_board(board)

        # Human turn
        p_move = int(input("Your move: "))

        board[p_move - 1] = human

        # AI turn
        ai_move = best_move(board)
        board[ai_move] = ai

    if check_winner(board) == human:
        print("You won!")
    elif check_winner(board) == ai:
        print("You lost!")
    elif check_winner(board) == 0:
        print("Tie!")

    print_board(board)

main()

#print(f"Best move {value}")
    
