import reflex as rx
from sqlmodel import select
from typing import Optional
from .db_model import User

class State2(rx.State):
    """The base state for the app."""

    user: Optional[User] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None

class AuthState(State2):
    """The authentication state for sign up and login page."""

    username: str
    password: str
    confirm_password: str
    email: str

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("Username already exists.")
            self.user = User(username=self.username, password=self.password, email=self.email)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/home")
            else:
                return rx.window_alert("Invalid username or password.")