import boto3


s3 = boto3.client("s3")
response = s3.upload_file('./arreglo.py', 'ejerciciozappaa', 'arreglo.py')

def menor(arreglo):
    print("ya esta")
    return min(arreglo)
    


