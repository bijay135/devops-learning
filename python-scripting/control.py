import sys
import subprocess

# Variables
instance_pool = [1, 2, 3]

# Functions
def start_instance(instance_number):
    subprocess.call("/Users/bijaya.shah/Applications/apache-tomcat-8.5.50/"+str(instance_number)+"/bin/startup.sh")

def stop_instance(instance_number):
    subprocess.call("/Users/bijaya.shah/Applications/apache-tomcat-8.5.50/{}/bin/shutdown.sh".format(instance_number))

def check_status():
    subprocess.run("lsof -i -n -P | grep '8001' | grep 'LISTEN'", shell=True)
    subprocess.run("lsof -i -n -P | grep '8002' | grep 'LISTEN'", shell=True)
    subprocess.run("lsof -i -n -P | grep '8003' | grep 'LISTEN'", shell=True)

# Commands with paramaters
if sys.argv[1] == "start":
    if sys.argv[2] == "all":
        for instance_number in instance_pool:
            start_instance(instance_number)
    else:
        for instance_number in sys.argv[2:]:
            start_instance(instance_number)
elif sys.argv[1] == "stop":
    if sys.argv[2] == "all":
        for instance_number in instance_pool:
            stop_instance(instance_number)
    else:
        for instance_number in sys.argv[2:]:
            stop_instance(instance_number)  
elif sys.argv[1] == "status":
    check_status()
else:
    print("Command not supported. Check and try again")