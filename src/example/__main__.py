import sys
from .example2 import example_tree
from .example1 import print_s3_buckets
import argparse


def usage():
    print("")
    print("\tUsage: example string1 string2 string3 string4")
    print("")
    print("\tstring(1-4): 4 strings that you want to create a merkle tree hash root")
    print("\tDescription: create a merkle tree root hash")
    print("")


def my_main():

    parser = argparse.ArgumentParser(description='Example AWS Python project with many benefits.')

    parser.add_argument(
        '--calculate-merkle-hash',
        nargs = 4,
        metavar=('string1', 'string2', 'string3', 'string4'),
        help='compute the merkle hash of input strings')
    args = parser.parse_args()

    print(f"You have provided {len(sys.argv)} argument(s): ")
    print("")

    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    print_s3_buckets()

    if args.calculate_merkle_hash:
        print("Your merkle root hash is:")
        print(example_tree(
            args.calculate_merkle_hash[0],
            args.calculate_merkle_hash[1],
            args.calculate_merkle_hash[2],
            args.calculate_merkle_hash[3]))
    else:
        parser.print_help()
        exit(-1)


if __name__ == "__main__":
    my_main()
