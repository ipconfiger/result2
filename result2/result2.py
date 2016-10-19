#coding=utf8

def _enum(**enums):
    return type('Enum', (), enums)

class ResultBase(object):
    def __init__(self, *data):
        self.__data = data

    def __call__(self):
        if len(self.__data)>1:
            return self.__data
        return self.__data[0]

    def __eq__(self, match_type):
        return isinstance(self, match_type)


class Success(ResultBase):

    def __init__(self, *return_data):
        super(Success, self).__init__(*return_data)

class Failure(ResultBase):

    def __init__(self, error):
        super(Failure, self).__init__(error)


Result = _enum(Ok=Success, Err=Failure)

def Ok(*return_data):
    """
    return Success wrapper
    :param return_data:normal return data
    :type : *args
    :return: Success wrapper object
    :rtype: Success
    """
    return Success(*return_data)

def Err(error):
    """
    return Failure wrapper
    :param error:error info
    :type: object
    :return: Error wrapper object
    :rtype: Failure
    """
    return Failure(error)
