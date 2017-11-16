### implement class Password here ###
class Password(object):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "*" * len(self._password)

    def resolve_password(self):
        return self._password

    def change_password(self, new_password):
        self._password = new_password

    def check_validity(self, *args):
        for arg in args:
            if not arg(self._password):
                return False
        return True


################################################################################

### validity check functions ###

def no_shorter_than_8(string):
    "checks that a given string is not shorter than 8 characters"

    return len(string) >= 8


def contains_special_chars(string):
    "checks that a given string does contain special characters"

    return not string.isalnum()


def starts_upper_case(string):
    "checks that a given string begins with an upper case letter"

    if string[0].isupper():
        return True
    return False


################################################################################

### some test cases ###

pw1 = Password("Password_1234")
print(pw1)  # should print: *************
print(pw1.resolve_password())  # should print: Password_1234
print(pw1.check_validity(no_shorter_than_8, contains_special_chars, starts_upper_case))  # should print: True
pw1.change_password("password_1234")
print(pw1.check_validity(starts_upper_case))  # should print: False
