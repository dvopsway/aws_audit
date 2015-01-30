# aws_audit
##version : 0.1.1
###Updation history
* 0.1 -> Project Launch
* 0.1.1 -> Checking access_keys available for users
* 0.1.2 -> Checking detached volumes

###Introduction
This projects aims to provide a library so that you can perform auditing for an aws account

#####Current functionality:
* IAM
  * Checking if mfa is enabled for users or not
  * Check if a user has access_keys enabled
  * Pulling available users and groups
  * Removing groups for user that doesn't have mfa enabled (use case)

* EC2
  * Get detached/attached/all volume lists
  * Get all the instances
  
###Prerequistes

* boto library , to install boto use the command below in terminal
```python
  pip install boto
```

###Documentation

* Check individual documentation
  * [Check_IAM](https://github.com/padmakarojha/aws_audit/blob/master/Documentation/Check_IAM.md)
  * [Check_EC2](https://github.com/padmakarojha/aws_audit/blob/master/Documentation/Check_EC2.md)
  






