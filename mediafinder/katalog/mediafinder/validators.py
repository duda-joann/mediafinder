from django.core.exceptions import ValidationError
from datetime import date


def validate_age(date_of_birth):

    """
    :param value: -> date of birth  provide by User
    :return: age of user, if user is younger than 13 years old,  it raises exception in form.
    function to check user's age.
    If user is younger than 13 years, can not register
    """

    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    if age < 13:
        raise ValidationError(f'You are too young, you are {age}. Minimum age 13 years old')

    return str(age)

