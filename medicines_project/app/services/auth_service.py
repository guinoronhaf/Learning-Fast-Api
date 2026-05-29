import os
import firebase_admin
from firebase_admin import auth, credentials
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

firebase_credentials_path = os.getenv("FIREBASE_JSON_PATH")

cred = credentials.Certificate(firebase_credentials_path)

firebase_admin.initiliaze_app(cred)

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        decoded_token = auth.verify_id_token(token)
    except Exception:
        raise HTTPException(
                status_code=401,
                detail="Token inválido."
        )
