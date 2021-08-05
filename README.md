# Rasa-Chatbot
This project showcases the various files required for building a rasa chatbot with functionality for Entity Extraction, API Weather Calls, Email sending etc.

The various files are detailed as follows:
### Test.db
Contains the database in sqlite for the storage of all the real time interactions with the bot.

### Config.yml
Contains the code for the various configuration related purposes for the bot.

### Credentials.yml
Contains basically the bot and the security credentials for our listed bot

# Domain.yml
Contains all the functions and the action descrpitions to be performed along with other features like the intents listed, entities, slots, forms etc.

# NLU.yml
Contains the intents and the speech examples for the bot to recognise pattern and alot what intent the user statement belongs to.
 
# Stories.yml
Contains the set path stories for few cases like weather api call or sending emails etc.

# Rules.yml
Contains checkpoint rules to be executed if a particular scenario is encountered.

# Endpoints.yml
Contains the url for the host website and other functionalities such as database storing using sqlite

# Actions.py
Contains the python scripts for various classes like sending emails, weather api calls, entity extraction scripts etc.

# Weather.py
Contains the function for weather api call
