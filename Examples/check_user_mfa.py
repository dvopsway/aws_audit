import aws_audit

# initializing variable
session = aws_audit.CheckIAM()

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



