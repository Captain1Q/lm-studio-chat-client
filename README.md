A simple python chat client for LM Studio with conversation history.

Usage:
1- install python on your pc

2- install the requests library via:

python -m pip install requests

3- download the lm_client.py script

4- Download and install LM Studio, download a model, load it, make sure server is active via the left "Developer Settings" menu.

5- Copy the model name and put it int the 'payload= {'model' : 'YOUR MODEL'}

6- Run via any IDE you have (VScode, etc...) or any CLI you want (cmd, powershell...etc) using the command (run from inside the same folder as the script):

python lm_client.py

7- Start chatting!

features:
- Simple quick running
- conversation history during the current session
- Handles connection failures, timeouts, and HTTP errors

limitations:
- No permanent memory
- No tool calling
- Model, server URL, and timeout are currently configured by editing the code
- Conversation will eventually exceed model context limit, history trimming isnt implemented.
