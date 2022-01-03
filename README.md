
# Install mongodb locally
Read documentation at [https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

# Edit your Mongodb credentials
```python
# in settings.py
MONGODB_DSN = 'mongodb://user:pass@localhost:27017'
```

# Install Python dependencies
```bash
pip install -r requirements.txt
```