# %% First: Import and understand hashing
import hashlib

# Let's see how hashing works
password = "hello123"
hashed = hashlib.sha256(password.encode()).hexdigest()
print(f"Original password: {password}")
print(f"Hashed password: {hashed}")


# %% Exercise 1: Create the encrypt function
def encrypt(password: str) -> str:
    """
    Encrypts a password using SHA256
    """
    # TODO: Use hashlib.sha256() to hash the password
    # Remember to:
    # 1. Encode the password string
    # 2. Use hexdigest() to get the hash
    pass


# Test your encrypt function
def test_encrypt():
    test_password = "test123"
    expected_hash = "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae"
    try:
        result = encrypt(test_password)
        assert result == expected_hash, f"Expected {expected_hash}, but got {result}"
        print("🎉 Great job! Your encryption function works perfectly!")
        return True
    except Exception as e:
        print("❌ Not quite right. Make sure you're using SHA256 and hexdigest()")
        print(f"Error: {str(e)}")
        return False


test_encrypt()

# %% Exercise 2: Store users in a dictionary
# Let's create a function to add users to our database
# The database will look like this:
# users = {
#     "alice": "hashed_password_here",
#     "bob": "different_hashed_password_here"
# }


def add_update_user(users: dict, username: str, password: str) -> None:
    """
    Adds a new user or updates existing user's password

    TODO:
    1. Hash the password using encrypt()
    2. Store username:hashed_password in the users dictionary
       (this will automatically update if user exists)
    3. Return the updated users dictionary

    Example:
    users = {"alice": "old_hash"}
    add_user(users, "alice", "newpass123")
    returns {"alice": "new_hash"} where new_hash is encrypt("newpass123")
    """
    pass


def test_add_update_user():
    users = {}
    try:
        # Test adding new user
        add_update_user(users, "alice", "password123")
        assert users["alice"] == encrypt("password123")

        # Test updating existing user
        old_hash = users["alice"]
        add_update_user(users, "alice", "newpassword123")
        assert users["alice"] == encrypt("newpassword123")
        assert users["alice"] != old_hash

        print("🌟 Excellent! Your function can both add new users and update existing ones!")
        return True
    except Exception as e:
        print("❌ The add_user function needs some work")
        print(f"Error: {str(e)}")
        return False


test_add_update_user()


# %% Exercise 3: Check if password is correct
def check_password(users: dict, username: str, password: str) -> bool:
    """
    Returns True if username exists and password is correct
    """
    # TODO: Check if:
    # 1. The username exists in the database
    # 2. The hashed password matches what's stored
    # Hint: Use the encrypt() function on the password before comparing!
    pass


# Test your check_password function
def test_check_password():
    users = {"alice": encrypt("password123")}
    try:
        # Should work with correct password
        assert check_password(users, "alice", "password123")
        # Should fail with wrong password
        assert not check_password(users, "alice", "wrong")
        # Should fail with non-existent user
        assert not check_password(users, "bob", "any")
        print("🏆 Perfect! Your password checking system is secure!")
        return True
    except Exception as e:
        print("❌ The check_password function needs some work")
        print(f"Error: {str(e)}")
        return False


test_check_password()


# %% Bonus Exercise 1: Add password requirements
def add_user_with_requirements(users: dict, username: str, password: str) -> bool:
    """
    Add user only if password meets requirements:
    - At least 8 characters
    - Contains at least one number
    - Contains at least one uppercase letter
    Returns False if requirements aren't met
    """
    pass


# Test your password requirements
def test_requirements():
    users = {}
    try:
        assert add_user_with_requirements(users, "user1", "TestPass123")
        assert not add_user_with_requirements(users, "user2", "short1")
        assert not add_user_with_requirements(users, "user3", "nodigits")
        assert not add_user_with_requirements(users, "user4", "nocaps123")
        print("🎯 Excellent! Your password requirements are working!")
        return True
    except Exception as e:
        print("❌ Password requirements need adjustment")
        print(f"Error: {str(e)}")
        return False


test_requirements()

# %% Bonus Exercise 2: Add Global Salt
# For extra security, we'll add a global salt to all passwords.
# In a real application, this would be stored in a secure configuration file.

# Global salt - in practice, this would be in a secure config file
GLOBAL_SALT = "fj29sk3n4890cmx"  # Example salt, could be any string


def add_user_with_salt(users: dict, username: str, password: str) -> None:
    """
    Add user with password hashed with global salt

    TODO:
    1. Combine the password with GLOBAL_SALT (e.g., password + GLOBAL_SALT)
    2. Hash the combined string using encrypt()
    3. Store the hash in users dictionary
    4. Return the updated users dictionary

    Example:
    add_user_with_salt({}, "alice", "pass123")
    returns {"alice": hash_of_pass123_plus_global_salt}
    """
    pass


def test_salt():
    users = {}
    try:
        # Add two users with same password
        add_user_with_salt(users, "user1", "same_password")
        add_user_with_salt(users, "user2", "same_password")

        # Verify basic structure
        assert isinstance(users, dict)
        assert "user1" in users
        assert "user2" in users

        # Same password should produce same hash with global salt
        assert users["user1"] == users["user2"]

        # Verify hash is different from unsalted version
        assert users["user1"] != encrypt("same_password")

        print("🌟 Fantastic! Your global salt system is working!")
        return True
    except Exception as e:
        print("❌ Global salt implementation needs some work")
        print(f"Error: {str(e)}")
        return False


test_salt()
# %%
