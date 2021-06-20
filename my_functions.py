
def create_id_list(apiObject, maxResults, q):
    unread_messages = apiObject.list(
                            userId='me',
                            labelIds=None,
                            maxResults=maxResults,
                            q=q).execute()

    messages = unread_messages.get('messages', [])

    id_list = []
    for message in messages:
        id_list.append(message['id'])

    return id_list
