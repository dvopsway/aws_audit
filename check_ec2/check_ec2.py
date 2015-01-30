import boto


class CheckEC2(object):
    volumes = None
    instances = None
    boto_ref = None
    all_volumes = []
    all_instances = []
    detached_volumes = []
    attached_volumes = []
    
    def __init__(self):
        self.boto_ref = boto.connect_ec2()
        
    def get_instances(self):
        self.all_instances = []
        self.instances = self.boto_ref.get_all_instances()
        for i in self.instances:
            self.all_instances.append(str(i))
        return self.all_instances
    
    # acquire all the volumes
    def get_all_volumes(self):
        self.all_volumes = []
        self.volumes = self.boto_ref.get_all_volumes()
        for v in self.volumes:
            self.all_volumes.append(str(v))
        return self.all_volumes
    
    # acquire all the attached volumes
    def get_attached_volumes(self):
        self.attached_volumes = []
        self.get_all_volumes()
        for v in self.volumes:
            if v.attachment_state() == 'attached':
                self.attached_volumes.append(str(v)[7:])
        return self.attached_volumes

    def get_detached_volumes(self):
        self.detached_volumes = []
        self.get_all_volumes()
        for v in self.volumes:
            if v.attachment_state() != 'attached':
                self.detached_volumes.append(str(v)[7:])
        return self.detached_volumes