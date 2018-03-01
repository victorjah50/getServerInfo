import paramiko

def executeCommand(host,user,passwd,pt,command):
    try:
        t = paramiko.SSHClient()
        t.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        t.connect(hostname=host, port=pt, username=user, password=passwd)
        stdin, stdout, stderr = t.exec_command(command)

        output = stdout.readlines()

        for i in output:
            print(i.rstrip('\n'))

    finally:
        t.close()

