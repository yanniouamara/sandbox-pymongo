# Sandbox MongoDB

## Install mongodb locally
Read documentation at https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

## Edit your Mongodb credentials
```python
# in settings.py
MONGODB_DSN = 'mongodb://user:pass@localhost:27017'
```

## Install Python dependencies
```bash
pip install -r requirements.txt
```

## Load datasets
```bash
python load_datasets.py
```

## Run training
```bash
python training_1.py
```

## Credits : 
 - https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/#resources