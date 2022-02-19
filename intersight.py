import os
import string  # Importing the OS module which allows us to import env variables. 
import requests
from intersight_auth import IntersightAuth #Importing IntersightAuth class to authenticate
import argparse

parser = argparse.ArgumentParser(description='Find server my model number')
parser.add_argument('-m', '--model', type=str)
parser.add_argument('-c', '--chassis', type=int)
args = parser.parse_args()

def main():
    secret_file = os.environ["SECRET_FILE"]
    api_key = os.environ['API_KEY']
    auth = IntersightAuth(secret_key_filename=secret_file, api_key_id=api_key)
    get_request = requests.get("https://intersight.com/api/v1/compute/PhysicalSummaries", auth=auth)
    results = get_request.json()['Results']

    for result in results:
        dn = result['Dn']
        model = result['Model']
        if model == args.model and dn.startswith(f'sys/chassis-{args.chassis}'):
                print(f'DN: {dn}')
                print(f'Model: {model}\n')



if __name__ == "__main__":
    main()


