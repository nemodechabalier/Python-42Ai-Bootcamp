
class Bank(object):
	def __init__(self):
		self.accounts = []
	def add(self, new_account):
		if isinstance(new_account, 'Account')
			print("It's not a 'Account'")
			return
		if any(new_account.name == account.name for account in self.account):
			print("Error name")
			return
		self.accounts.append(new_account)
	def transfer(self, origin, dest, amount):
		if not isinstance(origin,str) or not isinstance(dest,str):
			print("Error")
			return False
		try:
			amount = int(amount)
		except ValueError:
			print("Error")
			return False
		if any(account.name == origin for account in self.accounts) and any(account.name == dest for account in self.accounts):
			if amount > self.accounts
		
		

	def fix_account(self, name):
		# ... Your code ...


class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str)
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount