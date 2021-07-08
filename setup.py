import os, time, subprocess, re;

print('\nReseting enviorment..\n')

os.system('docker-compose up -d --force-recreate')

print('\nWait for cointainers to warm up...\n')
time.sleep(3)

print('\nInit a docker swarm\n')

r = subprocess.getoutput('docker exec manager docker swarm init')
token = re.search(r'SW\S{1,}', r)[0]
ip = re.search(r'[0-9]{3}\.\S{1,}', r)[0]

print('join token: ' + token)
print('IP manager: ' + ip)

print('\nJoin all nodes\n')

workersToJoin = ['worker1', 'worker2', 'worker3']
for worker in workersToJoin:
    command = 'docker exec %s docker swarm join --token %s %s' % (worker, token, ip)
    r = subprocess.getoutput(command)
    print('%s: %s' % (worker, r))

print('\nShow swarm status\n')
os.system('docker exec manager docker node ls')

print('\nDeploy Portainer\n')
os.system('docker exec manager docker stack deploy -c stack/portainer-agent-stack.yml portainer')