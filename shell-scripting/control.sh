#/bin/bash

#Variables
INSTANCE_POOL=( 1 2 3 )

#Functions
start_instance(){
    /Users/bijaya.shah/Applications/apache-tomcat-8.5.50/$1/bin/startup.sh
} 
stop_instance(){
    /Users/bijaya.shah/Applications/apache-tomcat-8.5.50/$1/bin/shutdown.sh
}
check_status(){
    lsof -i -n -P | grep "8001" | grep "LISTEN"
    lsof -i -n -P | grep "8002" | grep "LISTEN"
    lsof -i -n -P | grep "8003" | grep "LISTEN"
}

# Commands with paramaters
if [ $1 == "start" ]; then
    if [ $2 == "all" ]; then
        for INSTANCE_NUMBER in "${INSTANCE_POOL[@]}"; do
            start_instance $INSTANCE_NUMBER
        done
    else
        for INSTANCE_NUMBER in "${@:2}" ; do
            start_instance $INSTANCE_NUMBER
        done
fi
elif [ $1 == "stop" ]; then
    if [ $2 == "all" ]; then
        for INSTANCE_NUMBER in "${INSTANCE_POOL[@]}"; do
            stop_instance $INSTANCE_NUMBER
        done
    else
        for INSTANCE_NUMBER in "${@:2}" ; do
            stop_instance $INSTANCE_NUMBER
        done
    fi        
elif [ $1 == "status" ]; then
    check_status
else
    echo "Command not supported. Check and try again"
fi
