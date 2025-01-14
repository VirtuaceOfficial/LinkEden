import getpass
import os
import requests

def get_user_input(prompt):
    return getpass.getpass(prompt)

client_id = get_user_input("Enter your Client ID: ")
client_secret = get_user_input("Enter your Client Secret: ")
access_token = get_user_input("Enter your Access Token: ")

save_to_env = input("Would you like to save this key to your environment variables? (y/n): ").strip().lower()

if save_to_env == 'y':
    os.environ['LINKEDIN_CLIENT_ID'] = client_id
    os.environ['LINKEDIN_CLIENT_SECRET'] = client_secret
    os.environ['LINKEDIN_ACCESS_TOKEN'] = access_token
    print("Your credentials have been securely stored on your local system. Access will persist upon future sessions. To remove these credentials, navigate to the Account section of the app. ")
else:
    print("Credentials will not be saved. Future sessions will require re-authentication.")
