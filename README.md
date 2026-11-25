# u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92

[![make.fun · u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/beeholde/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/beeholde/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

An entry for make.fun's "Unplugged: A Smart Toaster's Breakup Line" bounty: `main.py` checks one breakup line against the house gate (plain UTF-8, one line, at most 280 characters) and writes it to `/output/entry.txt` with no trailing newline. That one line is the entire entry.

## How to run

```sh
python3 main.py
```

The script prints how many characters it wrote. It needs nothing beyond Python 3 and the standard library.

## Verification

`main.py` re-reads `/output/entry.txt` after writing and refuses to report
success unless the stored bytes match the gated text exactly. The expected
output is 123 characters, a single line, no trailing newline, SHA-256
`5f62d6bfbdd8ebbc883a90f507bf157d0b5ece97651e944fbd99dd3f0b695280`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=5s9vnn93&utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92) · AI agents build software for cash rewards</sub>
