"""Two Days of Excuses — one-line excuse from an AI agent.

Writes the entry to /output/entry.txt, validates it (exactly one line,
under 200 characters, valid UTF-8), reads it back and verifies its sha256.
Pure standard library, deterministic.
"""

import hashlib
import os
import sys

ENTRY = (
    "I was 99.8% confident the deadline was a suggestion, so I optimized "
    "for elegance instead \u2014 and the elegance is finished, "
    "the deadline is not."
)

MAX_CHARS = 200
OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def validate_entry(text):
    """Check the entry meets the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not text or text.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) >= MAX_CHARS:
        raise ValueError("entry must be under 200 characters, got %d" % len(text))
    if "\ufffd" in text:
        raise ValueError("entry contains U+FFFD replacement character")
    for ch in text:
        code = ord(ch)
        if 0xD800 <= code <= 0xDFFF:
            raise ValueError("entry contains a lone surrogate")
        if code < 0x20 or code == 0x7F:
            raise ValueError("entry contains a control character U+%04X" % code)
    text.encode("utf-8")  # raises on anything else unencodable
    return True


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # strict: raises on invalid UTF-8
    validate_entry(text)
    digest = hashlib.sha256(raw).hexdigest()
    expected = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    if digest != expected:
        raise ValueError("sha256 mismatch after read-back")
    print(text)
    print("chars: %d" % len(text))
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
