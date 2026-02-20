from lab02_methods.tasks.bank_account import BankAccount

def test_bank_account():
    a = BankAccount(100)
    a.withdraw(150)
    assert a.balance == 100
    a.withdraw(50)
    assert a.balance == 50

