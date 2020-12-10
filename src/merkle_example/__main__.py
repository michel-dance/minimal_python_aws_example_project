import sys


def usage():
    print("")
    print("\tUsage: merkle_example run")
    print("")
    print("\tDescription: This is an example main entry point")
    print("")


def my_main():
    print("executing main entry point for merkle_example")

    print(f"You have provided {len(sys.argv)} argument(s): ")
    print("")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    if len(sys.argv) <= 1:
        usage()
        exit(-1)
    else:
        print("running the merkle_example")
        exit(0)


if __name__ == "__main__":
    my_main()
