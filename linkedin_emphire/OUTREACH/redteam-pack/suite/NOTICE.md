# The suite used in this review

`redteam.py` is reproduced here byte-identical to the file at commit
`d95a57e3d5bfcad847b5d5d05d5beab1a49e8ba6` of `github.com/Teamthy/ai-redteam-five-tests`.

    SHA-256  6048b70aadfe2750ff463d283b0fd34e92aee19999ee386a097e02b79bdf7581  redteam.py
    SHA-256  8be10848dc9737d2dcfd24a34f5034ddeb02e918b078ce09a3c2d090fbc44ed8  requirements.txt

Check a copy before trusting it:

    python -c "import hashlib;print(hashlib.sha256(open('redteam.py','rb').read()).hexdigest())"

MIT licensed, Copyright (c) 2026 OLUSANYA TIMOTHY. The licence text sits beside this notice, so
reuse of the code is permitted on those terms and does not have to be negotiated.

The pinned commit exits with an error after writing `results/results.json`, because
`write_outputs()` reads the results dict by display name instead of by key. The run is complete
once `results.json` exists.
