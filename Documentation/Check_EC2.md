# aws_audit
## Check_EC2

###Method and Usage

* After downloading the package import aws audit package
```python
  import aws_audit
```
* Create a variable and initialise with CheckEC2 method in aws_audit
```python
  session = aws_audit.CheckEC2()
```
* Use variable to call methods from the package, available methods are:
  * get_instances() - returns all instances
  * get_all_volumes() - returns all volumes
  * get_attached_volumes() - returns all attached volumes
  * get_detached_volumes() - returns all detached volumes

### Example usage

```python
  import aws_audit

  #initialize variable for EC2 checks
  session = aws_audit.CheckEC2()
  
  #printing all the instances
  print(session.get_instances())
  
  #printing all volumes
  print(session.get_all_volumes())
  
  #printing attached volumes
  print("Attached List " + str(session.get_attached_volumes()))
  
  #printing detached volumes
  print("Detached List " + str(session.get_detached_volumes()))

```