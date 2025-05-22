from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepository(ABC):
    @abstractmethod
    def create(self, user_data: dict) -> dict:
        """Create a new user"""
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[dict]:
        """Find a user by email"""
        pass

    @abstractmethod
    def find_by_cpf(self, cpf: str) -> Optional[dict]:
        """Find a user by CPF"""
        pass

    @abstractmethod
    def update(self, user_id: str, user_data: dict) -> dict:
        """Update user data"""
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        """Delete a user"""
        pass

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def create(self, user_data: dict) -> dict:
        self.users.append(user_data)
        return user_data

    def find_by_email(self, email: str) -> Optional[dict]:
        return next((user for user in self.users if user['email'] == email), None)

    def find_by_cpf(self, cpf: str) -> Optional[dict]:
        return next((user for user in self.users if user['cpf'] == cpf), None)

    def update(self, user_id: str, user_data: dict) -> dict:
        for i, user in enumerate(self.users):
            if user.get('id') == user_id:
                self.users[i].update(user_data)
                return self.users[i]
        raise ValueError(f"User with id {user_id} not found")

    def delete(self, user_id: str) -> bool:
        initial_length = len(self.users)
        self.users = [user for user in self.users if user.get('id') != user_id]
        return len(self.users) < initial_length 