#TODO: handle errors:

  # this one occurs when the amount requested is greater than the available messages to delete
  #Note: The api still deletes the available amount and the throws this error:

    # googleapiclient.errors.HttpError: <HttpError 500 when requesting https://gmail.googleapis.com/gmail/v1/users/me/messages/batchDelete?
    # returned "Internal error encountered.". Details: "[{'message': 'Internal error encountered.', 'domain': 'global', 'reason': 'backend
    # Error'}]">

#TODO: handle error when there are not messages to be deleted - preconditon not met
#  eg: the user does not have unread messages
