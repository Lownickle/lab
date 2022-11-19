import account

class Test:


    account = account.account('John')


    def test_init(self):
        assert self.account.get_name() == 'John'
        assert self.account.get_balance() == 0

    def test_deposit(self):
        assert self.account.deposit(20) is True
        assert self.account.get_balance() == 20

        assert self.account.deposit(-10) is False
        assert self.account.get_balance() == 20

        assert self.account.deposit(0) is False
        assert self.account.get_balance() == 20

    def test_withdraw(self):
        assert self.account.withdraw(10) is True
        assert self.account.get_balance() == 10

        assert self.account.withdraw(-10) is False
        assert self.account.get_balance() == 10

        assert self.account.withdraw(0) is False
        assert self.account.get_balance() == 10

        assert self.account.withdraw(21) is False
        assert self.account.get_balance() == 10

