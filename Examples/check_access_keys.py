import aws_audit

# initializing variable
session = aws_audit.CheckIAM()

# getting all the groups
users = session.get_users()

# check if access key is available
for u in users:
    if session.check_access_keys(u):
        print("%s has access keys" % u )
    else:
        print("%s doesn't have access keys" % u )