#!/usr/bin/env python3
"""Build a send-ready .eml for the Aithos application from letter.txt.

Open the resulting .eml in Gmail, Outlook, Apple Mail or Thunderbird and it
arrives as a complete draft with the resume already attached. Nothing is sent
by this script: it only writes the file.

    python3 build_eml.py

Re-run it any time letter.txt changes. It always rebuilds from scratch.
"""

from __future__ import annotations

import mimetypes
import os
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from email.utils import formataddr, formatdate, make_msgid

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

SUBJECT = "Application, Research Engineer, Olusanya Timothy"
FROM_NAME = "Olusanya Timothy"
FROM_ADDR = "olusanyatimothy54@gmail.com"
TO_ADDR = "hiring@aithos.org"

# Relative to the repo root. Order is the order they appear in the email.
ATTACHMENTS = [
    "RESUME/Timothy_Olusanya_Aithos_Research_Engineer.pdf",
]

OUT = os.path.join(HERE, "Aithos_application_Olusanya_Timothy.eml")


def build() -> str:
    letter_path = os.path.join(HERE, "letter.txt")
    if not os.path.exists(letter_path):
        sys.exit(f"build_eml: missing {letter_path}")
    body = open(letter_path, encoding="utf-8").read().rstrip() + "\n"

    msg = EmailMessage()
    msg["From"] = formataddr((FROM_NAME, FROM_ADDR))
    msg["To"] = TO_ADDR
    msg["Subject"] = SUBJECT
    msg["Date"] = formatdate(localtime=False)
    msg["Message-ID"] = make_msgid(domain="gmail.com")
    msg["X-Mailer"] = "build_eml.py"
    msg.set_content(body, subtype="plain", charset="utf-8")

    added = []
    for rel in ATTACHMENTS:
        path = os.path.join(REPO, rel)
        if not os.path.exists(path):
            sys.exit(f"build_eml: missing attachment {path}")
        ctype, _ = mimetypes.guess_type(path)
        maintype, subtype = (ctype or "application/octet-stream").split("/", 1)
        with open(path, "rb") as fh:
            msg.add_attachment(
                fh.read(), maintype=maintype, subtype=subtype,
                filename=os.path.basename(path),
            )
        added.append((os.path.basename(path), maintype, subtype))

    with open(OUT, "wb") as fh:
        fh.write(msg.as_bytes())

    print(f"wrote {OUT}")
    print(f"  subject    : {SUBJECT}")
    print(f"  from       : {FROM_NAME} <{FROM_ADDR}>")
    print(f"  to         : {TO_ADDR}")
    print(f"  body       : {len(body.split())} words")
    for name, mt, st in added:
        size = os.path.getsize(os.path.join(REPO, [r for r in ATTACHMENTS if os.path.basename(r) == name][0]))
        print(f"  attachment : {name} ({mt}/{st}, {size/1024:.0f} KB)")
    return OUT


if __name__ == "__main__":
    build()
