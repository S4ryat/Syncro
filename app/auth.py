import secrets
# from typing import Annotated

# from fastapi import Depends, HTTPException
# from fastapi.security import HTTPBasicCredentials, HTTPBasic
# from starlette.status import HTTP_401_UNAUTHORIZED

# security = HTTPBasic()


# def get_current_username(
#     credentials: Annotated[HTTPBasicCredentials, Depends(security)],
# ):
#     current_username_bytes = credentials.username.encode("utf8")
#     correct_username_bytes = b"stanleyjobson"
#     is_correct_username = secrets.compare_digest(
#         current_username_bytes, correct_username_bytes
#     )
#     current_password_bytes = credentials.password.encode("utf8")
#     correct_password_bytes = b"swordfish"
#     is_correct_password = secrets.compare_digest(
#         current_password_bytes, correct_password_bytes
#     )
#     if not (is_correct_username and is_correct_password):
#         raise HTTPException(
#             status_code=HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username
