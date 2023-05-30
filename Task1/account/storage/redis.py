from typing import Optional, List

from account.model import Account
from account.storage.protocol import AccountsStorageProtocol


class AccountsRedisStorage(AccountsStorageProtocol):
    def __init__(self):
        self.redis_client = redis.Redis()

    def get_all_accounts(self) -> List[Account]:
        account_keys = self.redis_client.keys("*")
        accounts = []
        for key in account_keys:
            account_data = self.redis_client.hgetall(key)
            username = key.decode()
            password = account_data[b"password"].decode()
            email = account_data[b"email"].decode()
            account = Account(username=username, password=password, email=email)
            accounts.append(account)
        return accounts
    
    def get_account_by_id(self, account_id: int) -> Optional[Account]:
        account_keys = self.redis_client.keys("*")
        for key in account_keys:
            account_data = self.redis_client.hgetall(key)
            username = key.decode()
            password = account_data[b"password"].decode()
            email = account_data[b"email"].decode()
            account = Account(username=username, password=password, email=email)
            if account.id == account_id:
                return account
        return None

    def mark_account_as_blocked(self, account_id: int):
        account_keys = self.redis_client.keys("*")
        for key in account_keys:
            account_data = self.redis_client.hgetall(key)
            username = key.decode()
            password = account_data[b"password"].decode()
            email = account_data[b"email"].decode()
            account = Account(username=username, password=password, email=email)
            if account.id == account_id:
                account.blocked = True
                self.update_account(account)
                return

    def add_account(self) -> int:
        username = "new_account"
        password = "password123"
        email = "new_account@example.com"
        account = Account(username=username, password=password, email=email)
        self.create_account(account)
        return account.id

    def set_account_processing(self, account_id: int) -> Optional[Account]:
        account_keys = self.redis_client.keys("*")
        for key in account_keys:
            account_data = self.redis_client.hgetall(key)
            username = key.decode()
            password = account_data[b"password"].decode()
            email = account_data[b"email"].decode()
            account = Account(username=username, password=password, email=email)
            if account.id == account_id:
                account.status = "processing"
                self.update_account(account)
                return account
        return None

    def set_account_pending(self, account_id: int) -> Optional[Account]:
        account_keys = self.redis_client.keys("*")
        for key in account_keys:
            account_data = self.redis_client.hgetall(key)
            username = key.decode()
            password = account_data[b"password"].decode()
            email = account_data[b"email"].decode()
            account = Account(username=username, password=password, email=email)
            if account.id == account_id:
                account.status = "pending"
                self.update_account(account)
                return account
        return None
