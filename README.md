

#BANKING APP USING FILE TEXT(.txt) FILES FOR STORAGE

This app interacts with the Python file system to create data stores. The data stores used on this app are:

    staff.txt - holds the staff login credentials. It is not empty.
    customer.txt - holds customers accounts created. It is empty.
    'staff'_session.txt - holds the user login session. This file is created at login and destroyed at logout.

At login, the staff username and password are required. These can be found in the staff.txt file. You can add a new staff to the file if you seek some little adventure.

At successful login, the user is presented with options to create a new customer account, check an existing account details, or log out.

Below are screen shots of the working app

##Screenshots of Working App
![snbank_landing](https://user-images.githubusercontent.com/32728256/81260610-40e90900-9032-11ea-8304-a2110387dae7.png)
App landing page

![successfull_login](https://user-images.githubusercontent.com/32728256/81260661-5a8a5080-9032-11ea-9c17-9aedaae67b68.png)
Successful staff login

![successfull_accout_creation](https://user-images.githubusercontent.com/32728256/81260695-70981100-9032-11ea-8db6-6180ecbe1553.png)
Successful customer account creation

![check_account_details](https://user-images.githubusercontent.com/32728256/81260756-8d344900-9032-11ea-9385-9d0385ee5554.png)
Check Customer Account details


![staff_logout_and_close_app](https://user-images.githubusercontent.com/32728256/81260789-a1784600-9032-11ea-9c0f-7b8fcd3557ed.png)
Logout and Close App