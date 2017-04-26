# Initialize variables
. /etc/h2database/variables.conf

# Start a h2 instance
java -cp $H2DATABASELIB org.h2.tools.Server -tcpAllowOthers -webAllowOthers -tcpPort $H2DATABASETCPPORT -webPort $H2DATABASEWEBPORT -baseDir $H2DATABASEDATADIR
