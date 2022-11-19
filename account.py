class account:
    def __init__(self, name: str) -> None:
        """
        :param name: Name of the account
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        :param amount: number of money that is wanting to be deposited to the account
        :return: if the deposit works, return true, if not, return false
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        :param amount: amount of money wanting to be taken out of the account
        :return: if the withdrawal works, return true, if not, return false
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        :return: updated balance of the account
        """
        return (self.__account_balance)

    def get_name(self):
        """
        :return: name of the person of the account
        """
        return (self.__account_name)
        