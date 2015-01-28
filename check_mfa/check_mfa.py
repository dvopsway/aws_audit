import boto

class CheckMfa():
    all_users = []
    authorised_users = []
    unauthorised_users = []
    all_groups = []
    boto_ref = boto.connect_iam()

    # acquire all the users in IAM
    def get_users(self):
        users = self.boto_ref.get_all_users()
        for user in users.list_users_result.users:
            self.all_users.append(str(user['user_name']))
        return self.all_users

    # acquire all the groups in IAM
    def get_groups(self):
        groups = self.boto_ref.get_all_groups()
        for group in groups.list_groups_result.groups:
            self.all_groups.append(group['group_name'])
        return self.all_groups

    # finding if MFA is enabled or not
    def check_mfa_enabled(self,username):
        mfa_status = self.boto_ref.get_all_mfa_devices(username)
        if len(str(mfa_status.list_mfa_devices_result.mfa_devices)) > 2:
            return True
        else:
            return False

    # remove all groups for a user
    def remove_all_groups(self,username):
        self.get_groups(self)
        for group in self.all_groups:
            self.boto_ref.remove_user_from_group(group,username)