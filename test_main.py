from main import create_token
from main import verify_signature

class TestChallenge4:
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'

    data = {'language': 'Python'}

    def test_create_token(self):
        assert create_token({"language": "Python"}, "acelera") == self.token

    def test_verify_signature(self):
        assert verify_signature(self.token) == self.data