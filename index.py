from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from my_functions import *

# TODO: Refactor

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
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


    print("We have succesfully gain access to your gmail accout 👌.\n",
          "Be careful in how you use this program. \n",
          "Some changes are IRREVERSIBLE 😬.\n")


    def choose_a_number():
        while True:
            try:
                answer = int(input(("How many unread messages would you"
                                    "like to delete: (type an integer)")))
                return answer
            except ValueError:
                print("Your answer is invalid. Please enter an integer number")


    answer = choose_a_number()
    total_delations = answer

    # Call the Gmail API
    """
    Methods used:
    https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.users.messages.html


        - list(userId, includeSpamTrash=None, labelIds=None, maxResults=None, pageToken=None, q=None, x__xgafv=None)

        - batchDelete(userId, body=None, x__xgafv=None)
            for the body, we will create a an id_list with the list() method,
            which is defined in my_functions.py

    """

    my_messages_object = service.users().messages()

    # 1000 is the max Gmail API allows in batchDelete(), hance this if block
    if answer <= 1000:
        # Delete messages
        my_messages_object.batchDelete(
                            userId='me',
                            body={"ids": create_id_list(
                                            apiObject=my_messages_object,
                                            maxResults=answer,
                                            q="is:unread")}).execute()

    else:
        '''
        When greater than 1000 emails, we will first delete the the remainder,
        eg: if there are 1500 emails, we will delete 500 first, and then
        by the thousands.
        '''

        remainder = answer % 1000
        answer -= remainder  # set new value for the while loop

        my_messages_object.batchDelete(
                            userId='me',
                            body={"ids": create_id_list(
                                                apiObject=my_messages_object,
                                                maxResults=remainder,
                                                q="is:unread")}).execute()

        while answer > 0:

            my_messages_object.batchDelete(
                                userId='me',
                                body={"ids": create_id_list(
                                                apiObject=my_messages_object,
                                                maxResults=1000,
                                                q="is:unread")}).execute()
            answer -= 1000

    print((f"We have deleted {total_delations} messages!"
          "I hope we saved you precious time! 😅"))



    # Call the Gmail API - GMAIL EXAMPLE
    '''results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])'''

if __name__ == '__main__':
    main()
