

class BankDeposit:

    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance // 100 * self.rate

    def get_balance_with_profit(self):
        return self.__calculate_profit() + self.balance
