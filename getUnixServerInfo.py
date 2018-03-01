import paramiko

def executeCommand(host,user,passwd,pt,command):
    """
    host = "10.233.128.19"
    passwd = "Feb02**2018&&"
    user = "vvargas"
    pt = 22
    """

    try:
        t = paramiko.SSHClient()
        t.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        t.connect(hostname=host, port=pt, username=user, password=passwd)
        stdin, stdout, stderr = t.exec_command(command)

        output = stdout.readlines()
        #print("\n".join(output))
        for i in output:
            print(i.rstrip('\n'))

    finally:
        t.close()

