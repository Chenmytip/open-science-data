#!/usr/bin/env python3
"""Reconstruct ReadThrough_alg.zip from its numbered upload parts."""

from hashlib import sha256
from pathlib import Path
from shutil import copyfileobj


output = Path("ReadThrough_alg.zip")
parts = sorted(Path(".").glob("ReadThrough_alg.zip.part[0-9][0-9][0-9]"))
if not parts:
    raise SystemExit("No archive parts found")

with output.open("wb") as destination:
    for part in parts:
        with part.open("rb") as source:
            copyfileobj(source, destination)

digest = sha256(output.read_bytes()).hexdigest().upper()
expected = "DFC5F310D90CEC4E16B7A52CAEFE247C34A6EFB56DAC83A66D60BF856D789EE2"
print(f"Reconstructed {output} from {len(parts)} parts")
print(f"SHA-256: {digest}")
if digest != expected:
    raise SystemExit("SHA-256 verification failed")
print("SHA-256 verification passed")
