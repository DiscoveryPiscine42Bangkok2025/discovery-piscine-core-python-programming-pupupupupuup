from operator import add, sub


def find_king_position(board):
    n = len(board)
    for b in board:
        if len(b) != len(board):
            return

    for i in range(n):
        for j in range(n):
            if board[i][j] == "K" or board[i][j] == "k":
                return (i, j)
    return None




def enemy_pos(board, name):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == name:
                return (i, j)
    return None


def checkmate(board):
    pawn = ()
    rook = ()
    queen = ()
    bishop = ()
    knight = ()
    board = board.split("\n")

    king_pos = find_king_position(board)

    # Error check ถ้าไม่เจอ King หรือ Board ผิด
    if king_pos is None:
        print("Error")
        return
    

    # Pattern pieces

    # Pawn Position
    pawn_pattern = [(1, 1), (1, -1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "P" or board[i][j] == "p":
                pawn = (i, j)
                # print("pawn:", pawn)
    # Pawn Move
    if len(pawn) > 0:
        for p in pawn_pattern:
            pawn_mov = map(sub, pawn, p)
            if tuple(pawn_mov) == king_pos:
                print("Success")
                return

    # Rook Position
    # rook_pattern = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # rook_pattern = [[(0, 0), (0, -0), (0, 0), (-0, 0)],
    #                 [(0, 1), (0, -1), (1, 0), (-1, 0)],
    #                 [(0, 2), (0, -2), (2, 0), (-2, 0)],
    #                 [(0, 3), (0, -3), (3, 0), (-3, 0)]]
    rook_pattern = [[(0, i), (0, -i), (i, 0), (-i, 0)] for i in range(len(board))]
    #print(rook_pattern)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R" or board[i][j] == "r":
                rook = (i, j)
                # print("rook:", rook)
    # Rook Move
    if len(rook) > 0:
        for i in range(len(rook_pattern)):
            for j in range(len(rook_pattern[i])):
                rook_mov = map(add, rook, rook_pattern[i][j])
                if tuple(rook_mov) == king_pos:
                    print("Success")
                    return

    # bishop_pattern = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    bishop_pattern = [[(i, i), (-i, -i), (i, -i), (-i, i)] for i in range(len(board))]
    # print(bishop_pattern)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "B" or board[i][j] == "b":
                bishop = (i, j)
                # print("bishop:", bishop)
    # bishop Move
    if len(bishop) > 0:
        for i in range(len(bishop_pattern)):
            for j in range(len(bishop_pattern[i])):
                bishop_mov = map(add, bishop, bishop_pattern[i][j])
                if tuple(bishop_mov) == king_pos:
                    print("Success")
                    return

    # queen_pattern = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1),]
    queen_pattern = [
        [(0, i), (0, -i), (i, 0), (-i, 0), (i, i), (-i, -i), (i, -i), (-i, i)]
        for i in range(len(board))
    ]
    # print(quuen_pattern)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "Q" or board[i][j] == "q":
                queen = (i, j)
                # print("queen:", queen)
    # Queen Move
    if len(queen) > 0:
        for i in range(len(queen_pattern)):
            for j in range(len(queen_pattern[i])):
                queen_mov = map(add, queen, queen_pattern[i][j])
                if tuple(queen_mov) == king_pos:
                    print("Success")
                    return

    # Knight Pattern
    knight_pattern = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "H" or board[i][j] == "h":
                knight = (i, j)
                # print("knight:", knight)
    # Knight Move
    if len(knight) > 0:
        for i in knight_pattern:
            knight_mov = map(add, knight, i)
            if tuple(knight_mov) == king_pos:
                print("Success")
                return

    print("Fail")
    return
