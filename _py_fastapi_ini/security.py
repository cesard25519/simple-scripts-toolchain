from typing import NamedTuple, Self


class Namespace(NamedTuple):
    oauth_response: str
    access_token: str
    err: str
    mod: str


    @classmethod
    def as_fold(cls) -> Self:
        return cls(
            oauth_response=oauth_response,
            access_token=access_token,
            err=err,
            mod=mod,
        )


mod: str = """from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

_SCHEMA: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl='/auth/login',
)

BEARER_TOKEN_STR_HEADER = Annotated[str, Depends(dependency=_SCHEMA)]


from .access_token import AccessToken as AT


ACCESS_TOKEN_DEPENDENCY = Depends(dependency=AT.extractor)
ACCESS_TOKEN_EXTRACTOR = Annotated[AT, ACCESS_TOKEN_DEPENDENCY]
"""

oauth_response: str = '''
from pydantic import BaseModel


from config import SETTINGS


class OAuthSchemaResponse(BaseModel):
    access_token: str
    expires_in: int = SETTINGS.TOKEN_KEY_EXPIRE_TIME
    refresh_token: str | None = None
    token_type: str = \'Bearer\'
    scope: str | None = None
'''


access_token: str = '''from typing import NamedTuple, Self
import json


from pyseto import encode, decode


from api.err import InternalServerError
from config import SETTINGS

from .err import Forbiden, UnAuthorizated, RFCExpiredToken
from . import BEARER_TOKEN_STR_HEADER


class AccessToken(NamedTuple):
    sub: int
    capabilities: dict[str, str]

    exp: int = 0


    def can_create_or_raise(self, capability: str) -> None:
        """ C """

        permision: str = self.capabilities.get(capability, '')

        if not permision or not int(permision[0]):
            raise UnAuthorizated()

    def can_read_or_raise(self, capability: str) -> None:
        """ R """

        permision: str = self.capabilities.get(capability, '')

        if not permision or not int(permision[1]):
            raise UnAuthorizated()

    def can_modify_or_raise(self, capability: str) -> None:
        """ U """

        permision: str = self.capabilities.get(capability, '')

        if not permision or not int(permision[2]):
            raise UnAuthorizated()

    def can_delete_or_raise(self, capability: str) -> None:
        """ D """

        permision: str = self.capabilities.get(capability, '')
        if not permision or not int(permision[3]):
            raise UnAuthorizated()


    def as_token(self) -> str:
        try:
            return encode(
                exp=SETTINGS.TOKEN_KEY_EXPIRE_TIME,
                key=SETTINGS.KEY_INTERFACE,
                    payload=self._asdict(),
                    serializer=json,
                ).decode()
        except Exception as e: print(e)
        raise InternalServerError()


    @classmethod
    def extractor(cls, v: BEARER_TOKEN_STR_HEADER) -> Self:
        try:
            token: bytes | dict = decode(
                keys=[SETTINGS.KEY_INTERFACE],
                deserializer=json,
                token=v,
            ).payload

            if isinstance(token, dict):
                return cls(**token)

        except ValueError as e: raise RFCExpiredToken() from e

        except Exception as e:
            print(e)
            raise Forbiden() from e

        raise UnAuthorizated()
'''

err: str = """from fastapi import HTTPException, status


class UnAuthorizated(HTTPException):
    def __init__(self) -> None:
        super().__init__( status_code=status.HTTP_401_UNAUTHORIZED )


class Forbiden(HTTPException):
    def __init__(self) -> None:
        super().__init__( status_code=status.HTTP_403_FORBIDDEN )


class RFCExpiredToken(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                'error': 'invalid_token',
                'error_description': 'The access token expired',
            },
            headers={
                'WWW-Authenticate': (
                    'Bearer '
                    + 'realm="api", '
                    + 'error="invalid_token", '
                    + 'error_description="The access token expired"'
                ),
            }
        )
"""

