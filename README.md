# Gmail-crush

This desktop program is a work in progress. It aims to give you better control over google resources, such as deleting files permanently from gmail, by bypassing the trash folder.

## Motivation:

I had over 30k emails in my gmail account and it was hard to delete them by the 50s (which is the number of emails you see per page in your gmail interface).

On top of that, they were going to the trash folder, which was not helping me to free up any space at all until I emptied that folder too. Such a painful process, to say the least.

Thankfully, I thought there should be a more efficient way to do this, so I researched about gmail APIs and found that I could build a program to make this process faster.

I hope you too, find this program useful!

## Before Running the Program:

To use this program, you can clone my repository to your local machine, but you may need to set up a project with your Google Cloud Platform account (I’ll provide a link below with the instructions). This is because they share my client_secrete when you are using their Auth0 service to receive an authentication token. There is a lot of ambiguous information out there regarding this issue. Therefore, I prefer to play on the safer side and keep this information private.

Once you set up the project in the Google Cloud, then you can attach your credentials to the project folder and you should be able to use (and improve) my script. 


## Running the program:

1. Clone this repository to your local machine (it may be good to set up a virtual environment for this project)

2. Create a project in your Workspace Developer at Google. https://developers.google.com/workspace/guides/getstarted-overview

3. Follow instructions to set up project and receive credentials. When you download the credentials, the json file has a different name (something like client_secret_<other_info>.json. Make sure to change that file name to ‘credentials.json’

4. Add the credentials.json file to the the local repository

5. Run python3 index.py in your terminal 

Note: The first time you run the program, google will open a browser and ask you to give the program permission to access your api.
