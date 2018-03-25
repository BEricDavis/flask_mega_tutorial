Working through Miguel Grinberg's 2017 revision of the Flask Mega-Tutorial
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Before launching, remember to run: 
* venv\Scripts\activate
* set FLASK_APP=microblog.py
* set MS_TRANSLATOR_KEY=<key>

#Notes
1: install of alembic seemed to be incorrect.  Received errors when trying to 
import User from app.models: Source code string cannot contain null bytes.
* created a new venv and installed libs through PyCharm
* this might have been because i used pip instead of conda?

2: So....the user table seems to have disappeared?
* tried running flask db migrate, but no effect
* renamed app.db to app.db.old
* migrations ran successfully
* test suite is tearing everything down!?
* I had misconfigured the sqloite connect string

3: To stand up a fake mailserver:
* python -m smtpd -n -c DebuggingServer localhost:25
* set MAIL_SERVER=localhost
* set MAIL_PORT=25
