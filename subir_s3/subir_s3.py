import boto3
import os 

##### Definir o nome do arquivo local 

local_file_path = './data/data.json'
bucket_name = 'projeto-scrapy'

s3_client = boto3.client('s3')

# Obter o nome do arquivo do caminho local
file_name = os.path.basename(local_file_path)

# Fazer o upload do arquivo para o S3
try:
    response = s3_client.upload_file(local_file_path, bucket_name, file_name)
    print(f'Arquivo {file_name} enviado com sucesso para o bucket {bucket_name}')
except Exception as e:
    print(f'Erro ao enviar o arquivo para o S3: {e}')