import paramiko
from dotenv import load_dotenv
import os

load_dotenv()

hostname = os.getenv('HOSTNAME')
username = os.getenv('USERNAME')
private_key_path = os.getenv('PRIVATE_KEY_PATH')

def main():

    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Create SFTP client
        sftp = ssh.open_sftp()
    except:
        print("Unable to establish SSh connection")
        return
    # Load private key for authentication
    try:
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        transfer(ssh, sftp, private_key)
    except:
        print("Unable to load private key")
        end_connection(ssh, sftp)


def transfer(ssh: paramiko.SSHClient(), sftp, private_key: paramiko.RSAKey):
    try:
        ssh.connect(hostname, username=username, pkey=private_key)
    except:
        print("Unable to create a conection, please check your credentials.")
        end_connection(ssh)

    try:
        # Upload file to remote server
        local_file_path = input("Enter local file path: ")
        remote_file_path = input("Enter remote file path: ")
        sftp.put(local_file_path, remote_file_path)
    except:
        print("Unable to upload files to remote server.")
        end_connection(ssh, sftp)
        
    try:
        # Download file from remote server
        sftp.get(remote_file_path, local_file_path)
    except:
        print("Unable to download files to remote server.")
        end_connection(ssh, sftp)


def end_connection(ssh: paramiko.SSHClient(), sftp):
    # Close SFTP session and disconnect
    sftp.close()
    ssh.close()


if __name__ == '__main__':
    main()
