import sys
from .example2 import example_tree


def usage():
    print("")
    print("\tUsage: merkle_example2 string1 string2 string3 string4")
    print("")
    print("\tstring(1-4): 4 strings that you want to create a merkle tree hash root")
    print("\tDescription: create a merkle tree root hash")
    print("")


def my_main():

    print(f"You have provided {len(sys.argv)} argument(s): ")
    print("")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    if len(sys.argv) < 5:
        usage()
        exit(-1)
    else:
        print("Your merkle root hash is:")
        print(example_tree(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
        exit(0)


if __name__ == "__main__":
    my_main()
