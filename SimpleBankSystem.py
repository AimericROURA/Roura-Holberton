class Bank:
    balance: List[int]  #List of account balances

    #Create a new Bank object from a list of accounts
    def __init__(self, balance: List[int]):
        self.balance = balance

    #Transfer "money" from account1 to account2
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        validTransaction = self.transactionIsValid(account1, money) and self.transactionIsValid(account2)
        if validTransaction:
            #The transaction is valid, we can proceed
            self.balance[account1-1] = self.balance[account1-1] - money
            self.balance[account2-1] = self.balance[account2-1] + money

        return validTransaction

    #Add "money" to the account
    def deposit(self, account: int, money: int) -> bool:
        validTransaction = self.transactionIsValid(account)
        if validTransaction:
            #The transaction is valid, we can proceed
            self.balance[account-1] = self.balance[account-1] + money

        return validTransaction

    #Remove "money" from the account
    def withdraw(self, account: int, money: int) -> bool:
        validTransaction = self.transactionIsValid(account, money)
        if validTransaction:
            #The transaction is valid, we can proceed
            self.balance[account - 1] = self.balance[account - 1] - money

        return validTransaction

    #Check the validity of any transaction
    def transactionIsValid(self, account: int, money: Optional[int] = None) -> bool:
        validity = (len(self.balance) >= account)  #Check if the account exists
        if ((money != None) and validity):  #In the case of a withdrawal, we check if the account has enough money
            validity = validity and (self.balance[account - 1] >= money)
        return validity


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)