### **Don't-Cry Ransomware**

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python\&logoColor=white)
![Cython](https://img.shields.io/badge/Requires-Cython-yellow?logo=python\&logoColor=white)
![License](https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat\&logo=open-source-initiative\&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Status](https://img.shields.io/badge/Status-Temporarily--Inactive-orange)

![DCry](./DCRY.png)

Ransomware using Python 💀💀💀

## Usage

* Open the [`DCry.py`](./src/DCRY.py) file, change the `YOUR_URL` variable to your Tor server URL, and set the `dev_mode` variable to `False`.
* Install the required packages with the following command:

  ```bash
  pip install -r requirements.txt
  ```
* Build the Cython code with the following command:

  ```bash
  python src/setup.py build_ext --inplace
  ```
* Run the server with the following command:

  ```bash
  python src/server.py
  ```
* Run the ransomware with the following command:

  ```bash
  python src/DCRY.py
  ```
* Run the decryptor with the following command:

  ```bash
  python src/decryptor.py
  ```

## Warning

> \[!WARNING]
> This project is a ransomware simulation for educational purposes only.

## License

* This project is licensed under the terms of the [Apache License 2.0](./LICENSE).
