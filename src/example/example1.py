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


def submit_batch_job():
    print("submit_batch_job")

    client = boto3.client('batch')

    response = client.submit_job(
        jobName='example-cli-job',
        jobQueue='example-fars',
        jobDefinition='example-s3',
        containerOverrides={
            'command': [
                '--calculate-merkle-hash', 'ferrari', 'mercedes', 'haas', 'renault'
            ]
        })

    print(response)
