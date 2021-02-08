import boto3

print("loading example1")

def example1():
    print("example1()")

    return 0

def print_s3_buckets():
    print("print_s3_buckets")

    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
         print(f'  {bucket["Name"]}')

