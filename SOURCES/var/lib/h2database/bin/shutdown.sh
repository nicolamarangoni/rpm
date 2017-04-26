# Initialize variables
. /etc/h2database/variables.conf

# Shutdown a h2 instance
java -cp $H2DATABASELIB org.h2.tools.Server -tcpShutdown tcp://localhost:$H2DATABASETCPPORT
