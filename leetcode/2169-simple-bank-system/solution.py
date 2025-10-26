class Bank(object):

    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)
    

        """
        :type balance: List[int]
        """
        

    def transfer(self, account1, account2, money):
        if 1<= account1 <= self.n and 1<= account2 <= self.n:
            if self.balance[account1 - 1]>=money:
                self.balance[account1-1]-=money
                self.balance[account2-1]+=money
                return True
        return False
    
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        

    def deposit(self, account, money):
        if 1<= account <=self.n :
            self.balance[account-1]+=money

            return True
        return False
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        

    def withdraw(self, account, money):
        if 1<= account<=self.n:
            if self.balance[account-1] >=money:

                self.balance[account-1]-=money
                return True
        return False

        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
