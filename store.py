from google.cloud import firestore

collection_ref = firestore.Client().collection('strava_twitter_bot')

def get_data(document):
    doc = collection_ref.document(document).get()
    return doc.to_dict()

def get_twitter_settings():
    return get_data('twitter_settings')

def get_strava_settings():
    return get_data('strava_settings')

def get_access_data():
    return get_data('access_data')

def save_access_data(data):
    doc_ref = collection_ref.document('access_data')
    doc_ref.set(data)
