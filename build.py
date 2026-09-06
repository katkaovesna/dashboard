#!/usr/bin/env python3
"""Zašifruje measurements.json do data.json (AES-256-GCM).
Kľúč sa vygeneruje nový, ak key.txt neexistuje; inak sa použije existujúci
(aby staré uložené odkazy ostali funkčné aj po aktualizácii dát)."""
import base64
import json
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HERE = os.path.dirname(os.path.abspath(__file__))
MEAS = os.path.join(HERE, "measurements.json")
KEY_FILE = os.path.join(HERE, "key.txt")
OUT_DIR = os.path.join(HERE, "out")
OUT_FILE = os.path.join(OUT_DIR, "data.json")


def b64u(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def main():
    if os.path.exists(KEY_FILE):
        key = base64.urlsafe_b64decode(open(KEY_FILE).read().strip() + "==")
    else:
        key = AESGCM.generate_key(bit_length=256)
        open(KEY_FILE, "w").write(b64u(key))
        print("Nový kľúč vygenerovaný a uložený do key.txt")

    plaintext = open(MEAS, "rb").read()
    aesgcm = AESGCM(key)
    iv = os.urandom(12)
    ct = aesgcm.encrypt(iv, plaintext, None)  # tag je pripojený na koniec

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w") as f:
        json.dump({"iv": b64u(iv), "ct": b64u(ct)}, f)

    print("Kľúč (URL fragment):", b64u(key))
    print("Zapísané:", OUT_FILE)


if __name__ == "__main__":
    main()
