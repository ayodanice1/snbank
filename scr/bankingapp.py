
class DataFileScraper(object):
	def __init__(self, dataFile):
		self.dataFile = dataFile

	def retrieveCredentials(self, data_type):
		"""
		This method takes a data file, extract its contents. From the extracted content,
		it then builds the individual credentials into a dictionary.
		"""
		with open(self.dataFile, 'r') as f:
			data = f.read()
		item_objects = {}
		data_objects = self.retrieveObjects( data )

		for data_object in data_objects:
			item_object = self.buildCredential(data_object)
			if data_type == 'staff':
				head = item_object['username']
				del item_object['username']
				item_objects[head] = item_object
			elif data_type == 'customer':
				head = item_object['accountnumber']
				del item_object['accountnumber']
				item_objects[head] = item_object
		
		return item_objects

	def retrieveObjects(self, data_string) :
		"""
		This method takes a string of data 'data_string', breaks it into 'tokens'
		and builds individual data objects 'data_object' from the tokens, which are then
		returned to the method caller as a compiled list 'data_objects'.
		"""
		tokens = data_string.split()
		data_objects = []

		for token in tokens:
			if token == '{': data_object = []
			elif token == '}': data_objects.append(data_object)
			elif token == ':': continue
			else: data_object.append(token)
		return data_objects

	def buildCredential(self, object_tokens):
		keywords = ('username', 'password', 'firstname', 'lastname', 'email',
			'openingbalance', 'accountname', 'accounttype', 'accountnumber')
		data_object = []
		credential = {}

		for token in object_tokens:
			if token != ',':
				if token in keywords: key = token
				else: value = token
			else: credential[key] = value
		return credential

class BankingApp(object):
	def __init__(self, username, password):
		self.customers_data_file = '../datastore/customer.txt'
		self.staffs_data_file = '../datastore/staff.txt'
		self.staffData = DataFileScraper(self.staffs_data_file)
		self.customerData = DataFileScraper(self.customers_data_file)
		self.staff_credentials = self.staffData.retrieveCredentials('staff')
		self.username = username
		self.password = password

	def useApp(self):
		print("""
			Below are the options available to you.

			1 - Create New Customer Account
			2 - Check Account Details
			3 - Logout
		""")
		try:
			user_option = int(input("Enter option: "))
		except:
			print("\nWrong option input!")
		else:
			if user_option == 1:
				self.createCustomerAccount()
			elif user_option == 2:
				accountnumber = input("Enter the accountnumber: ")
				account = self.getACustomerInfo(accountnumber)
				for field in account:
					print(f'{field}: {account[field]}')
				self.useApp()
			elif user_option == 3:
				import os
				os.remove(f'../datastore/{self.username}_session.txt')
				print("\nStaff log out successful.")

	def verifyLogin(self):
		staff = self.staff_credentials[self.username]
		if staff['password'] == self.password:
			return True
		else: return False

	def getStaffsCredentials(self):
		return self.staff_credentials

	def getCustomersInfo(self):
		customer_accounts = self.customerData.retrieveCredentials('customer')
		return customer_accounts

	def getACustomerInfo(self, accountnumber):
		customer_accounts = self.customerData.retrieveCredentials('customer')
		try:
			customer_accounts[accountnumber]
		except:
			print("\nERROR! ERROR!! ERROR!!!")
			print("Account does not exist!")
			self.useApp()
		else:
			return customer_accounts[accountnumber] 

	def createCustomerAccount(self):
		firstname = input("Enter first name: ")
		lastname = input("Enter last name: ")
		openingbalance = float(input("Enter opening balance: "))
		accounttype = input("Enter account type: ")
		email = input("Enter email: ")
		accountnumber = self.generateAccountNumber()
		with open(self.customers_data_file, 'a+') as f:
			f.write('\n')
			f.write('{ \n')
			f.write(f'accountnumber : {accountnumber} ,\n')
			f.write(f'firstname : {firstname} ,\n')
			f.write(f'lastname : {lastname} ,\n')
			f.write(f'accounttype : {accounttype} ,\n')
			f.write(f'email : {email} ,\n')
			f.write(f'openingbalance : {openingbalance} ,\n')
			f.write('} ,')
			f.close()
		print(f"New customer account number is '{accountnumber}'.")
		self.useApp()

	def updateCustomerAccount(self):
		pass

	def deleteCustomerAccount(self):
		pass

	def generateAccountNumber(self):
		import random
		number_string = ''
		for i in range(10):
			number_string += str(random.randrange(10))
		try:
			self.customer_accounts[number_string]
		except:
			return number_string



def main():
	print("""
		*****BANKING SYSTEM APPLICATION*****


		Below are the options available to you.

		1 - Staff LogIn
		2 - Close App
	""")

	try:
		user_option = int(input("Enter option: "))
	except:
		print("\nWrong option input!\nTry again")
		main()
	else:
		if user_option == 1:
			username = input("Enter username: ")
			password = input("Enter password: ")
			bankingApp = BankingApp(username, password)
			if (bankingApp.verifyLogin()):
				from datetime import datetime
				f = open(f'../datastore/{username}_session.txt', 'w+')
				f.write(f'@ {datetime.now()}: {username} logged in.')
				f.close()
				bankingApp.useApp()
				main()
			else:
				print("Invalid credentials! Try again")
				main()
		elif user_option == 2: print("Application stopped and closing down...")


main()
