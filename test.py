import unittest
from workshop4 import User, BankUser


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User('Bob', 1234, 'password')
        self.bank_user = BankUser("Alice", 9999, 'puppies')
        self.bank_user2 = BankUser('Charles', 2022, 'bears')

    def test_name(self):
        # test to see if first argument and second argument are equal
        self.assertEqual(self.user.name, 'Bob')

    def test_pin(self):
        self.assertEqual(self.user.pin, 1234)

    def test_password(self):
        self.assertEqual(self.user.password, 'password')

    def test_change_name(self):
        self.user.change_name('Robert')
        self.assertEqual(self.user.name, 'Robert')

    def test_change_pin(self):
        self.user.change_pin(5678)
        self.assertEqual(self.user.pin, 5678)

    def test_change_password(self):
        self.user.change_password('kitty123')
        self.assertEqual(self.user.password, 'kitty123')

    # tests if bank_user class inheritied correctly from User class
    def test_bank_user_class(self):
        self.assertIsInstance(self.bank_user, User)

    def test_bank_name(self):
        self.assertEqual(self.bank_user.name, 'Alice')

    def test_bank_pin(self):
        self.assertEqual(self.bank_user.pin, 9999)

    def test_bank_password(self):
        self.assertEqual(self.bank_user.password, 'puppies')

    # tests if change name method in bank user class works
    def test_bank_change_name(self):
        self.bank_user.change_name('Robert')
        self.assertEqual(self.bank_user.name, 'Robert')

    def test_bank_change_pin(self):
        self.bank_user.change_pin(5678)
        self.assertEqual(self.bank_user.pin, 5678)

    def test_bank_change_password(self):
        self.bank_user.change_password('kitty123')
        self.assertEqual(self.bank_user.password, 'kitty123')

    def test_bank_change_name2(self):
        self.bank_user2.change_name('Charles')
        self.assertEqual(self.bank_user2.name, 'Charles')

    def test_bank_change_pin2(self):
        self.bank_user2.change_pin(2022)
        self.assertEqual(self.bank_user2.pin, 2022)

    def test_bank_change_password2(self):
        self.bank_user2.change_password('bears')
        self.assertEqual(self.bank_user2.password, 'bears')

    # tests if bank_user balance was initilized to 0
    def test_bank_balance(self):
        self.assertEqual(self.bank_user.balance, 0)

    def test_bank_show_balance(self):
        self.assertEqual(self.bank_user.show_balance(), 0)

    def test_bank_deposit(self):
        self.bank_user.deposit(100)
        self.assertEqual(self.bank_user.balance, 100)

    def test_bank_withdraw(self):
        self.bank_user.withdraw(100)
        self.assertEqual(self.bank_user.balance, -100)

    def test_bank_transaction(self):
        alice = BankUser('Alice', 1234, 'password')
        alice.deposit(5)
        alice.withdraw(5)
        self.assertEqual(alice.balance, 0)

    def test_bank_transfer_money_false_pin(self):
        alice = BankUser('Alice', 9999, 'puppies')
        bob = BankUser('Bob', 6666, 'yay')
        # checks if transfer money will fail with incorrect pin
        self.assertEqual(alice.transfer_money(1234, 100, bob), False)

    def test_bank_transfer_money_correct_pin(self):
        bob = BankUser('Bob', 6666, 'yay')
        alice = BankUser('Alice', 9999, 'puppies')
        alice.transfer_money(9999, 100, bob)
        # if money transferred correctly bob should have 100 balance
        self.assertEqual(bob.balance, 100)
