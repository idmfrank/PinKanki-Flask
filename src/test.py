import yaml, requests, os

# Will really want to build out tests to validate config file, prob test authentication
# all responses etc.

# Load config
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Get an auth token

# Build request body
auth_body = {}
auth_body['InstanceName'] = os.environ['ARCH_INSTANCE']
auth_body['Username'] = os.environ['ARCH_USER']
auth_body['UserDomain'] = str(os.environ.get('ARCH_DOMAIN') or '') # UserDomain should be empty string not 'None'
auth_body['Password'] = os.environ['ARCH_PWD']

login_url = os.environ['ARCH_HOST'] + config['Resources']['Login']

r = requests.post(login_url, json=auth_body)

# print(r.status_code)
# print(r.json())

SessionToken = r.json()['RequestedObject']['SessionToken']
print("ding ding! " + SessionToken)

# Get users
user_url = os.environ['ARCH_HOST'] + config['Resources']['User']
u = requests.get(user_url, headers={"Authorization": "Archer session-id=" + SessionToken})
print(user_url)

#print(u.json())

# Get groups
group_url = os.environ['ARCH_HOST'] + config['Resources']['Group']
g = requests.get(group_url, headers={"Authorization": "Archer session-id=" + SessionToken})
#print(group_url)

#print(g.json())

# Get roles
role_url = os.environ['ARCH_HOST'] + config['Resources']['Role']
r = requests.get(role_url, headers={"Authorization": "Archer session-id=" + SessionToken})
print(role_url)

print(r.json())

# Also /system/groupmembership and /system/rolemembership


# Logout

logout_url = os.environ['ARCH_HOST'] + config['Resources']['Logout']
r = requests.post(logout_url, json={'Value': SessionToken}, headers={'Authorization': 'Archer session-id=' + SessionToken})
print("Logout request returned: " + str(r.status_code))
print("IsSuccessful: " + str(r.json()['IsSuccessful']))
