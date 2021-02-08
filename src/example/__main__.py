from .example2 import example_tree
from .example1 import print_s3_buckets
from .example1 import submit_batch_job
import argparse


def main():

    parser = argparse.ArgumentParser(description='Example AWS Python project with many benefits.')

    parser.add_argument(
        '--calculate-merkle-hash',
        nargs=4,
        metavar=('string1', 'string2', 'string3', 'string4'),
        help='compute the merkle hash of input strings')
    parser.add_argument(
        '--print-s3-buckets',
        action='store_true',
        help='show the s3 buckets in this account')
    parser.add_argument(
        '--submit-batch-job',
        action='store_true',
        help='submit a job to AWS for batch processing')
    args = parser.parse_args()

    if args.calculate_merkle_hash:
        print("Your merkle root hash is:")
        print(example_tree(
            args.calculate_merkle_hash[0],
            args.calculate_merkle_hash[1],
            args.calculate_merkle_hash[2],
            args.calculate_merkle_hash[3]))
    if args.print_s3_buckets:
        print_s3_buckets()
    if args.submit_batch_job:
        submit_batch_job()
    else:
        parser.print_help()
        exit(-1)


if __name__ == "__main__":
    main()
