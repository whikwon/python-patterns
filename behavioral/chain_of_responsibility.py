"""Google 2-step verification."""

from abc import ABC, abstractmethod


class AccountVerifier(ABC):
    successor = None

    def set_next(self, successor):
        self.successor = successor

    @abstractmethod
    def authenticate(self):
        pass


class PasswordVerifier(AccountVerifier):
    def authenticate(self):
        pwd = input("Input the password: ")
        if pwd == "0102":
            self.successor.authenticate()
        else:
            raise ValueError("Wrong password has input.")


class CellPhoneVerifier(AccountVerifier):
    def authenticate(self):
        pwd = input("Input the authorization number: ")
        if pwd == "8194":
            print("Successfully Logged in.")
        else:
            raise ValueError("Wrong password has input.")


def main():
    pwd_verifier = PasswordVerifier()
    cellphone_verifier = CellPhoneVerifier()

    pwd_verifier.set_next(cellphone_verifier)
    pwd_verifier.authenticate()


if __name__ == "__main__":
    main()
