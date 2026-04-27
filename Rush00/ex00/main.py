from checkmate import checkmate


def main():
    board = """\
........
........
........
........
........
...K.R..
........
........\
"""
    # data = board.split('\n')
    checkmate(board)


if __name__ == "__main__":
    main()
