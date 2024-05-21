#!/usr/bin/env python3
"""BaseicAuth class module"""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth class"""
    def __init__(self) -> None:
        """contructor method"""
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header method"""

        if not authorization_header or \
                not isinstance(authorization_header, str):
            return None

        if authorization_header[:6] != 'Basic ':
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """def decode_base64_authorization_header method"""
        if not base64_authorization_header or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            decoded_str = decoded.decode('utf-8')
            return decoded_str

        except (base64.binascii.Error, UnicodeDecodeError):
            return None
