#coding=utf8

from result2 import Result, Ok, Err


def get_valid_user_by_email(email):
    """
    Return user instance
    """
    user = get_user(email)
    if user:
        if user.valid is False:
            return Err("user not valid")
        return Ok(user)
    return Err("user not exists")


result = user = get_user_by_email('superpowerlee@gmail.com')
if result == Result.Ok:
    # do something if user exists ...
else:
    # to create new user page with reason
