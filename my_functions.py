def print_message(message, extra=None):
    if message == "welcome":
        print("We have gain access to your gmail accout 👌.\n",
              "Be careful in how you use this program. \n",
              "Some changes are IRREVERSIBLE 😬.\n")
    elif message == "summary":
        print((f"\nWe have deleted {extra} messages! "
               "I hope we saved you precious time! 😅"))


# choose_a_number()
#    Asks the user for an integer. If input is not an integer,
#    the condition evaluates

def choose_a_number():
    while True:
        try:
            answer = int(input(("How many unread messages would you"
                                "like to delete: (type an integer) ")))
            return answer

        except ValueError:
            print("\nYour input is invalid. Please enter an integer number")


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
