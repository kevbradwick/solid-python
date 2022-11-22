"""
Single Responsibility Principle

This principle is probably the best understood principle. It states that a unit of 
function should have one purpose and responsibility. This can be applied to classes,
functions, modules and packages.

The User class below have a few issues. When you read it, what do you think it is
responsible for? Creating users? Emailing them? Both? What about the name, does it
clearly describe what it does?

This can be improved by being more specific about the name of the class and moving the 
functionality for emailing into its own function.
"""
from dataclasses import dataclass


@dataclass
class User:
    pk: int
    email: str

    def save(self):
        """
        This method will insert the user into the database
        """
        print("User inserted to DB")

    def send_registration_email(self):
        """
        This method will send a registration email to the user
        """
        print("Email sent!")


@dataclass
class UserDBModel:
    """
    The class name gives a better description about its purpose and functionality. You
    don't have to be as explicit as this, Depending on your project structure, you can use
    package names to create that intent e.g. mypackage.db.User
    """

    pk: int
    email: str

    def save(self):
        print("user saved to DB")


def send_registration_email(user: UserDBModel):
    print(f"Email sent to {user.email}!")
