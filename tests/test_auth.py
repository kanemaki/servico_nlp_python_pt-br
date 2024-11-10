# from ../auth import authenticate_user, create_access_token
from tests.olds.auth import authenticate_user, create_access_token


def test_autenticate_user():
    assert authenticate_user("admin", "admin") == True
    assert authenticate_user("user", "wrong_password") == False
    assert authenticate_user("wrong_username", "wrong_password") == False


def test_create_access_token():
    token = create_access_token("admin")
    print("Token : " + token)
    assert isinstance(token, str)  # Verifica se o token é uma string
    assert token is not None



def main():
    test_autenticate_user()
    test_create_access_token()
    print("All tests passed!")


if __name__ == "__main__":
    main()
