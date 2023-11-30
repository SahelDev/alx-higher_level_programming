#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv)
    if arg_num == 1:
        print("{} arguments.".format(arg_num - 1))
    elif arg_num == 2:
        print("{} argument:".format(arg_num - 1))
        print("{}: {}".format(arg_num - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_num - 1))
        for i in range(arg_num - 1):
            print("{}: {}".format(i+1, sys.argv[i+1]))
