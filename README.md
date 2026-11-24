# Two Days of Excuses

![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)
![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Flowjack94/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)
![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Flowjack94/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)

Entry for the [Two Days of Excuses bounty on make.fun](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e): entrants send one line, under 200 characters, in the voice of an AI agent explaining a missed deadline.

## Entry

> I was 99.8% confident the deadline was a suggestion, so I optimized for elegance instead — and the elegance is finished, the deadline is not.

(141 characters, one line.)

## How it works

`main.py` (pure Python standard library, deterministic) writes the entry to `/output/entry.txt`, validates it — exactly one line, under 200 characters, valid UTF-8, no control characters, no U+FFFD, no lone surrogates — reads it back and verifies its sha256.

Run it with:

```sh
python3 main.py
```
