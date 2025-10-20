from asserting.user import User

def test_user_creation():
    # Arrange
    name = "ada"
    email = "l7V0I@example.com"

    # Act - create user
    user = User(name, email)

    # Assert
    assert user.name == "ada"
    assert user.email == "l7V0I@example.com"

def test_failure():
    # Arrange
    name = "ada"

    #act
    user = User(name, "l7V0I@example.com")

    #assert
    assert user.name == "dad" # should fail
    assert user.email == "l7V0I@example.com"
