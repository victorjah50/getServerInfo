import configparser
import getUnixServerInfo
#import getWinServerInfo

def readServerListFile(configPathFile):
    """
    Function to read a config file section and
    with it read line by line the server list.
    """
    pathconfigfile = configparser.ConfigParser()
    pathconfigfile.read(configPathFile)

    try:
        with open(pathconfigfile.get('Globals', 'servers_pathFile'), 'r') as server:
            for lines in server:
                currentline = lines.strip().split(',')
                #print("Server {0} have opererating system: {1}".format(currentline[0], currentline[1]))
                if currentline[1] == "linux":
                    print("server {} linux on port {}".format(currentline[0],format(currentline[2])))
                    #command ="wget https://192.168.2.4/snow/deploy_snow_linux.sh && sudo sh deploy_snow_linux.sh 2>&1 > deploy.log && cat deploy.log"
                    #command ="wget https://192.168.2.4/snow/undeploy_snow_linux.sh && sudo sh undeploy_snow_linux.sh"
                    #command = "pwd"
                    command = "nohup sudo nice -n 10 /opt/snow/snowagent -w /opt/snow/ >/dev/null 2>&1 &"
                    getUnixServerInfo.executeCommand(currentline[0], pathconfigfile.get('Unix', 'user'), pathconfigfile.get('Unix', 'pass'), currentline[2],command)

                elif currentline[1] == "windows":
                    print("server {} windows".format(currentline[0]))
                elif currentline[1] == "solaris":
                    print("server {} solaris".format(currentline[0]))
                    getUnixServerInfo.executeCommand(currentline[0], pathconfigfile.get('Unix', 'user'), pathconfigfile.get('Unix', 'pass'), "22")
                else:
                    print('Error: please check server list file syntax')

    except IOError:
        print('Error reading server list file: ', pathconfigfile.get('Globals', 'servers_pathFile'))

if __name__ == '__main__':
    readServerListFile('config.ini')
