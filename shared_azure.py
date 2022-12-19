from azure.identity import ClientSecretCredential
from dotenv import load_dotenv
import os

load_dotenv()

def authenticate_by_client_token():

    tenant_id = os.environ.get('TENANT_ID')
    app_id = os.environ.get('APPLICATION_ID')
    client_secret = os.environ.get('SECRET')
    auth = 'https://analysis.windows.net/powerbi/api/.default'

    credentials = ClientSecretCredential(
        authority='https://login.microsoftonline.com/',
        tenant_id=tenant_id,
        client_id=app_id,
        client_secret=client_secret
    )

    access_token = credentials.get_token(auth)
    access_token = access_token.token

    return access_token


