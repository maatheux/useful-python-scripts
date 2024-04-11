import warnings
import datetime
import time
import paramiko
import sys

start_time = time.time()

from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    
paramiko.util.log_to_file("paramiko.log")

host = '127.0.0.1'
port = 0
usr = sys.argv[1]
pwd = sys.argv[2]
filepath = sys.argv[3]
localpath = sys.argv[4]

# Open a transport
# host,port = "example.com",22
transport = paramiko.Transport((host,port))

# Auth
# username,password = "bar","foo"
transport.connect(None,usr,pwd)

# Go!    
sftp = paramiko.SFTPClient.from_transport(transport)

# Download
sftp.get(filepath,localpath)

# Upload
# filepath = "/home/foo.jpg"
# localpath = "/home/pony.jpg"
# sftp.put(localpath,filepath)

# Close
if sftp: sftp.close()
if transport: transport.close()

exec_time = round(abs((time.time() - start_time) / 60.0), 2)
print('Tempo de execução: ' + str(exec_time) + ' minuto(s).')