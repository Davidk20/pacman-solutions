import os
import secrets
import string

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
absolute_path = os.path.dirname(__file__)
relative_path = "../../.env/serviceAccount.json"
cred = credentials.Certificate(os.path.join(absolute_path, relative_path))
firebase = firebase_admin.initialize_app(cred)
db = firestore.client()


def generate_api_key() -> str:
    """
    Generate a new API Key.

    Returns
    -------
    A 256-character long API Key.
    """
    characters: str = string.ascii_letters + string.digits + string.punctuation
    # remove potentially breaking characters
    characters_to_remove = ['"', "'", "`", "“", "”", "\\"]
    for char in characters_to_remove:
        characters = characters.replace(char, "")
    return "".join(secrets.choice(characters) for _ in range(256))


def authenticate(key: str) -> bool:
    """
    Check whether the request is authenticated.

    Parameters
    ----------
    `key` : `str`
        The key to check.

    Returns
    -------
    `True` if authenticated.
    """
    key_filter = firestore.firestore.FieldFilter("key", "==", key)
    api_keys_ref = db.collection("api-keys")
    query = api_keys_ref.where(filter=key_filter).limit(1)
    docs = query.get()
    # If any document is returned, the API key exists
    if docs:
        return True
    else:
        return False
