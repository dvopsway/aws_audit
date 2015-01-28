# aws_audit
##version : 0.1

###Introduction
This projects aims to provide a library so that you can perform auditing for an aws account
#####Current functionalities:
  * checking if mfa is enabled for users
  * Pulling available users and groups
  * removing groups for user that doesn't have mfa enabled (use case)

###Prerequistes

* boto library , to install boto use the command below in terminal
```python
  pip install boto
```

###Method and Usage

* After downloading the package import aws audit package
```python
  import aws_audit
```
* Create a variable and intilise with CheckMfa method in aws_adit
```python
  session = aws_audit.CheckMfa()
```
* Use variable to call methods from the package, available methods are:
  * get_users() - returns user list
  * get_groups() - returns group list
  * check_mfa_enabled(username) - return boolean - True if enabled or vice versa
  * remove_all_groups(username) - remove all groups if MFA is not enable for a user 
    
### Example usage

```python
  import aws_audit
  
  # initializing variable
  session = aws_audit.CheckMfa()
  
  # getting all the groups
  users = session.get_users()
  
  # check if mfa is enable or not
  for u in users:
      if session.check_mfa_enabled(u):
          print("mfa is enabled for %s " % u)
      else:
          print("mfa is not enabled for %s" % u)
          
  # get all the groups
  groups = session.get_groups()
  print(groups)
```


