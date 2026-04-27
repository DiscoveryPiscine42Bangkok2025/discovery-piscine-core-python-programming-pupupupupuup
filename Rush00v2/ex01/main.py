from checkmate import checkmate
import sys



def main():
    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            if i > 0:
                file = open(sys.argv[i])
                readfile = file.read()
                board = readfile
                checkmate(board)

if __name__ == "__main__":
    main()
