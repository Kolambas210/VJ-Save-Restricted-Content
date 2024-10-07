import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26948104"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5cd7c8dbc4331f9db28e83c25b8fe12e")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://aaradhyverma256:8CR1AaSBP650mpNT@cluster0.0pghe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
