import hashlib


def hash_password(password: str):
    password_bytes = password.encode("utf-8")
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password


def check_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password
