from operator import sub,add

def fk(board):
    n = len(board)
    for l in board:
        if len(l) != len(board):
            return 
    for i in range(n):
        for j in range(n):
            if board[i][j] == "K" or board[i][j]=="k":
                return (i, j)
    return None


def checkmate(board):
    p=()
    r =()
    b=()
    q = ()
    board = board.split("\n")

    n = len(board)

    k_pos = fk(board)

    if k_pos is None:
        print("Error")
        return

    p_pattern = [(1, 1), (1, -1)]

    for i in range(n):
        for j in range(n):

            if board[i][j] == "P"or board[i][j] == "p":

                p = (i, j)

                for pawn in p_pattern:

                    pawn_m = tuple(map(sub, p, pawn))

                    if pawn_m == k_pos:
                        print("Success")
                        return
    
    r_pattern = [[(0,i),(0,-i),(i,0),(-i,0)] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] == "R"or board[i][j] == "r":
                r = (i, j)
            
    if len(r)>0:
        for i in range(len(r_pattern)):
            for j in range(len(r_pattern[i])):
                rook_m = tuple(map(add,r, r_pattern[i][j]))

                if rook_m == k_pos:
                    print("Success")
                    return
    b_pattern = [[(i,i),(-i,-i),(i,-i),(-i,i)]for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] == "B"or board[i][j] == "b":
                b = (i, j)
            
    if len(b)>0:
        for i in range(len(b_pattern)):
            for j in range(len(b_pattern[i])):
                bishop_m = tuple(map(add,b, b_pattern[i][j]))

                if bishop_m == k_pos:
                    print("Success")
                    return
                
    q_pattern = [[(0,i),(0,-i),(i,0),(-i,0),(i,i),(-i,-i),(i,-i),(-i,i)]for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] == "Q"or board[i][j] == "q":
                q = (i, j)
            
    if len(q)>0:
        for i in range(len(q_pattern)):
            for j in range(len(q_pattern[i])):
                queen_m = tuple(map(add,q, q_pattern[i][j]))

                if queen_m == k_pos:
                    print("Success")
                    return
                  
    

    print("Error")
    return