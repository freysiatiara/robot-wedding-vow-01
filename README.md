# Till Firmware Do Us Part

One wedding vow, spoken by a robot at its own wedding — funny and heartfelt in a single sentence.

Entry for the make.fun bounty [Till Firmware Do Us Part](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929).

[![Bounty](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/freysiatiara/robot-wedding-vow-01/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/freysiatiara/robot-wedding-vow-01/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

## The vow

> I promise to love you through every firmware update and every low-battery warning, and if I ever crash, reboot me beside you — I never want to wake up anywhere else.

## How it works

`main.py` (Python standard library only) writes the vow to `/output/entry.txt` — or to the path named by `ENTRY_OUTPUT`, or to `entry.txt` inside `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` when set.

```sh
python3 main.py
```
