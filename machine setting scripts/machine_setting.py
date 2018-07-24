#!/usr/bin/env python

import paramiko


server_list = {'IMAGENET 1':'ec2-52-10-180-106.us-west-2.compute.amazonaws.com','IMAGENET 2':'ec2-34-220-41-19.us-west-2.compute.amazonaws.com','IMAGENET 3':'ec2-35-161-100-216.us-west-2.compute.amazonaws.com','IMAGENET 4':'ec2-54-188-152-212.us-west-2.compute.amazonaws.com\
','IMAGENET 5':'ec2-34-214-148-210.us-west-2.compute.amazonaws.com','IMAGENET 6':'ec2-54-200-141-4.us-west-2.compute.amazonaws.com'}

def start_sever():
    for sever in server_list:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_list[sever], 22, 'ubuntu',
        key_filename='/Users/jonah/.ssh/megadata-OR.pem')

        ssh.exec_command('')


def look_up_status():
    for sever in server_list:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_list[sever], 22, 'ubuntu',
        key_filename='/Users/jonah/.ssh/megadata-OR.pem')
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp = ssh.open_sftp()


if __name__ == "__main__":
    start_sever()
        



