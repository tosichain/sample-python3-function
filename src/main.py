import os
import ipfshttpclient2
from io import BytesIO

def datachain():
    ipfs_api = os.getenv('IPFS_API', '/ip4/127.0.0.1/tcp/5001')

    try:
        ipfs_instance = ipfshttpclient2.connect(ipfs_api)
    except Exception as e:
        print(f"Error connecting to IPFS API: {e}")
        return

    content = "Hello World"
    directory_path = '/state'

    try:
        ipfs_instance.files.mkdir(directory_path, parents=True)

        output_path = f"{directory_path}/output.file"

        ipfs_instance.files.write(output_path, BytesIO(content.encode('utf-8')), create=True, truncate=True)

    except Exception as e:
        print(f"Error writing content to IPFS: {e}")

if __name__ == "__main__":
    datachain()
