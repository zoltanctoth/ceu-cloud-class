import hashlib
from typing import Optional


def encrypt(s: str) -> str:
    """
    Encrypts a string using SHA256 algorithm

    @param s: string to encrypt
    @return: the SHA256 hexdigest value of `s`
    """
    return hashlib.sha256(s.encode()).hexdigest()


def init_table() -> None:
    """
    Returns empty dataframe
    @return: An empty dataframe with these columns: 'user_name' and 'password'
    """
    return {}


def get_encrypted_password_for_user(df: dict, user_name: str) -> Optional[str]:
    """
    Returns the encrypted password of a user.
    If no user with the specified `user_name` exists, return None

    @param user_name: the username
    @return: the encrypted password of the user
    """
    if user_name not in df:
        return None

    return df[user_name]


def add_or_update_user(df: dict, user_name: str, password: str) -> dict:
    """
    Adds a new record to `df` setting the `user_name` and the `password`
    If there is a record with the same username, update the password instead of
    creating a duplicate record.

    @param df: the dataframe to add the user to
    @param user_name: the username
    @param password: the password

    @return: the dataframe with the new user added or the password updated
    """
    df[user_name] = encrypt(password)
    return df


def authenticate_user(df: dict, user_name: str, password: str) -> bool:
    """
    Checks if the user with the specified `user_name` and `password` exists in `df`

    @param df: the dataframe to check
    @param user_name: the username
    @param password: the password

    @return: True if the user exists and the password matches, False otherwise
    """
    return (user_name in df) and (
        get_encrypted_password_for_user(df, user_name) == encrypt(password)
    )


if __name__ == "__main__":
    #
    # Example execution
    #
    # Create initial table
    user_df = init_table()

    # Add our first user
    user_df = add_or_update_user(user_df, "first_user", "example_password")

    # Add a second user
    user_df = add_or_update_user(user_df, "second_user", "example_password_2")

    # Update the password of our first_user
    user_df = add_or_update_user(user_df, "first_user", "new_example_password")

    # EVALUATE THE RESULTS
    # These all must return true
    assert get_encrypted_password_for_user(user_df, "nonexistent_user") is None
    assert get_encrypted_password_for_user(user_df, "first_user") == encrypt(
        "new_example_password"
    )
    assert authenticate_user(user_df, "first_user", "new_example_password")
    assert authenticate_user(user_df, "second_user", "example_password_2")
    assert not authenticate_user(user_df, "first_user", "example_password")
