import os
import firebase_admin
from firebase_admin import auth, credentials
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas.auth_schema import TokenProviderData

# quando o código estiver em produção, essa linha não deve existir.
os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"

firebase_credentials_path = os.getenv("FIREBASE_JSON_PATH")

cred = credentials.Certificate(firebase_credentials_path)

firebase_admin.initialize_app(cred)

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenProviderData:
    token = credentials.credentials

    try:
        decoded_token = auth.verify_id_token(token)
        return TokenProviderData(**decoded_token)
    except Exception:
        raise HTTPException(
                status_code=401,
                detail="Token inválido."
        )
