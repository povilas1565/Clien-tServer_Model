# Clien-Server_Model
#It provides:
a simple multithreading server, it can listening many clients
a simple multithreading client with gui
storage client history in locale database
authenticate client on server and can dialogs with other clients
#Install:
pip install -r requirements.txt
cp geekmessenger/config/env.json.sample geekmessenger/config/env.json
#Testing
python -m pytest tests/test_server.py
