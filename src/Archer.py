import yaml, requests, os

class Archer:
    def __init__(self):
        # Load config
        with open('config.yml', 'r') as file:
            self.config = yaml.safe_load(file)

        # Build auth request body
        self.auth_body = {}
        self.auth_body['InstanceName'] = os.environ['ARCH_INSTANCE']
        self.auth_body['Username'] = os.environ['ARCH_USER']
        self.auth_body['UserDomain'] = str(os.environ.get('ARCH_DOMAIN') or '') # UserDomain should be empty string not 'None'
        self.auth_body['Password'] = os.environ['ARCH_PWD']          

        self.session_token = None

    def __str__(self):
        return f'ArcherAuth({self.session_token})'

    def login(self):
        """Attempt to login."""
        r = requests.post(os.environ['ARCH_HOST'] + self.config['Resources']['Login'],
            json=self.auth_body)
        session_token = r.json()['RequestedObject']['SessionToken']
        self.session_token = session_token
        return session_token

    def logout(self):
        """Attempt to logout."""
        if self.session_token != None: 
            data = {'Value': self.session_token}
            r = requests.post(os.environ['ARCH_HOST'] + self.config['Resources']['Logout'],
                headers={"Authorization": "Archer session-id=" + self.session_token}, 
                json=data)
            self.session_token = None
            return r

    def getUsers(self):
        r = requests.get(os.environ['ARCH_HOST'] + self.config['Resources']['User'],
            headers={"Authorization": "Archer session-id=" + self.session_token})
        return r.json()

    def getGroups(self):
        group_url = os.environ['ARCH_HOST'] + self.config['Resources']['Group']
        r = requests.get(group_url, headers={"Authorization": "Archer session-id=" + self.session_token})
        return r.json()

    def getRoles(self):
        role_url = os.environ['ARCH_HOST'] + self.config['Resources']['Role']
        r = requests.get(role_url, headers={"Authorization": "Archer session-id=" + self.session_token})
        return r.json()

