
class FlywaySchemaHistory:
    def __init__(self, installed_rank=0, version='', description='', type='', script='', checksum=0, installed_by='', installed_on=None, execution_time=0, success=False):
        self.installed_rank = installed_rank
        self.version = version
        self.description = description
        self.type = type
        self.script = script
        self.checksum = checksum
        self.installed_by = installed_by
        self.installed_on = installed_on
        self.execution_time = execution_time
        self.success = success
    
    def to_json(self):
        return {
            'installed_rank' : self.installed_rank,
            'version' : self.version,
            'description' : self.description,
            'type' : self.type,
            'script' : self.script,
            'checksum' : self.checksum,
            'installed_by' : self.installed_by,
            'installed_on' : str(self.installed_on),
            'execution_time' : self.execution_time,
            'success' : self.success
        }
        
    def to_response(self):
        return {
            'installed_rank' : self.installed_rank,
            'version' : self.version,
            'description' : self.description,
            'type' : self.type,
            'script' : self.script,
            'checksum' : self.checksum,
            'installed_by' : self.installed_by,
            'installed_on' : str(self.installed_on),
            'execution_time' : self.execution_time,
            'success' : self.success
        }