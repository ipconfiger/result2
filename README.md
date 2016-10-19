# result2

Swift style Result for Python

We can not use exceptions as logical judgments, for example:

``` python
class UserNotExistsException(Exception):
    pass

class UserNotValidException(Exception):
    pass

def get_valid_user_by_email(email):
    """
    Return user instance
    """
    user = get_user(email)
    if user:
        if user.valid is False:
            raise UserNotValidException
        return user
    raise UserNotExistsException

try:
    user = get_user_by_email('superpowerlee@gmail.com')
    # do something if user exists ...
except UserNotExistsException, e:
    # to create new user page with reason
except UserNotValidException, e:
    # to create new user page with reason
```

this code use try .. except as if, it's not a right way. So, you change the code, like next:

``` python
def get_valid_user_by_email(email):
    """
    Return user instance
    """
    user = get_user(email)
    if user:
        if user.valid is False:
            return False, u"user not valid"
        return True, user
    return False, u"user not exists"


result, data = user = get_user_by_email('superpowerlee@gmail.com')
if result:
    # do something if user exists ...
else:
    # to create new user page with reason

```

In this case, what's the meaning of variable data ? The semantics in this code are ambiguous. It's easy to let us make mistake.

Use result2, your can rewrite the code above, use swift style result type, for example:

``` python

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


result = get_user_by_email('superpowerlee@gmail.com')
if result == Result.Ok:
    # do something if user exists ...
else:
    # to create new user page with reason
```

This one will be better, with clear logic and semantics.

That's why i write this lib. Thers is a similar lib https://github.com/dbrgn/result, why write new one? Because this one can return multi value.



# Useage

Install:

pip install result2

When you return something:

``` python
return Ok(data)  # return one value

return Ok(data1, data2, data3 ...)  # return a lot of value

return Err(reson)  # return failure
```



To check if return right:

``` python
if result == Result.Ok:
```



To check if return not right:

``` python
if result == Result.Err:
```



To get return value:

``` python
user = result()  # when return one value
v1, v2, v3 = result()  # when return multi value
error = result()  # get error reason
```



That's all of it, enjoy.