import aws_audit

# initializing variable
session = aws_audit.CheckEC2()

# print all volumes
print(session.get_all_volumes())

# print all instances
print(session.get_instances())

# print all attached volumes
print("Attached List " + str(session.get_attached_volumes()))

# print all detached volumes
print("Detached List " + str(session.get_detached_volumes()))