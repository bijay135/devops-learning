import argparse 
import subprocess

# Definatons
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", dest = "mode", help="Control mode start, stop, status")
args = parser.parse_args()
if args.mode != "status":
    instance = input("Enter instance number(space seperated for multiple), all:  ")

# Variables
instance_pool = [1, 2, 3]

# Functions
def start_instance(instance_number):
    subprocess.call("/Users/bijaya.shah/Applications/apache-tomcat-8.5.50/"+str(instance_number)+"/bin/startup.sh")

def stop_instance(instance_number):
    subprocess.call("/Users/bijaya.shah/Applications/apache-tomcat-8.5.50/"+str(instance_number)+"/bin/shutdown.sh")

def check_status():
    subprocess.run("lsof -i -n -P | grep '8001' | grep 'LISTEN'", shell=True)
    subprocess.run("lsof -i -n -P | grep '8002' | grep 'LISTEN'", shell=True)
    subprocess.run("lsof -i -n -P | grep '8003' | grep 'LISTEN'", shell=True)

# Commands
if args.mode == "start":
    if instance == "all":
        for instance_number in instance_pool:
            start_instance(instance_number)
    else:
        for instance_number in instance.split():
            start_instance(instance_number)
elif args.mode == "stop":
    if instance == "all":
        for instance_number in instance_pool:
            stop_instance(instance_number)
    else:
        for instance_number in instance.split():
            stop_instance(instance_number)  
elif args.mode == "status":
    check_status()
else:
    print("Command not supported. Check and try again")