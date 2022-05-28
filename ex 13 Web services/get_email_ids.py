from __future__ import print_function
import os.path
from collections import Counter
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    """
    creds = None
    user_id = "me"
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    ### Call the Gmail API

    ### Show messages

    token = ''
    messages = service.users().messages().list(userId=user_id,pageToken=token).execute().get('messages', [])
    token = service.users().messages().list(userId=user_id,pageToken=token).execute().get('nextPageToken', [])
    print(messages,token)

    messages2 = service.users().messages().list(userId=user_id,pageToken=token).execute().get('messages', [])
    token2 = service.users().messages().list(userId=user_id,pageToken=token).execute().get('nextPageToken', [])
    print(messages2,token2)
    # all_messages = []
    # token = ''
    #
    # while True:
    #
    #     messages = service.users().messages().list(userId=user_id, pageToken=token).execute().get('messages', [])
    #     token = service.users().messages().list(userId=user_id, pageToken=token).execute().get('nextPageToken', [])
    #     if not messages:
    #         break
    #     print(messages)
    #     all_messages += messages
    #
    # print(all_messages)

if __name__ == '__main__':
    main()