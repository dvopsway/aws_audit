# aws_audit
##version : 0.1
###Updation history
* 0.1 -> Project Launch
* 0.1.1 -> Checking access_key functionality

###Introduction
This projects aims to provide a library so that you can perform auditing for an aws account
#####Current functionality:
  * Checking if mfa is enabled for users or not
  * Check if a user has access_keys enabled
  * Pulling available users and groups
  * Removing groups for user that doesn't have mfa enabled (use case)

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
* Create a variable and initialise with CheckIAM method in aws_audit
```python
  session = aws_audit.CheckIAM()
```
* Use variable to call methods from the package, available methods are:
  * get_users() - returns user list
  * get_groups() - returns group list
  * check_mfa_enabled(username) - return boolean - True if enabled or vice versa
  * check_access_keys(username) - return boolean - True if user has access key or vice versa
  * remove_all_groups(username) - remove all groups if MFA is not enable for a user 
    
### Example usage

```python
  import aws_audit

  # initializing variable
  session = aws_audit.CheckIAM()

  # getting all the groups
  users = session.get_users()

  # check if mfa is enable or not
  for u in users:
      if session.check_mfa_enabled(u):
          print("mfa is enabled for %s " % u)
          # checking access key availability
          print("has access keys : %s \n" % session.check_access_keys(u))
      else:
          print("mfa is not enabled for %s" % u)
          # checking access key availability
          print("has access keys : %s \n" % session.check_access_keys(u))

  # get all the groups
  groups = session.get_groups()
  print(groups)
```


