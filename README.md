# MFcoin rate in polybar

Shows the creep currency in Polybar

## Installation

go to the directory .config 

```bash
cd ~/.config/polybar/
git clone https://github.com/0RootLoL0/MFcoin_rate_in_polybar.git
```

## include

```
modules-right = mfcrate ;add module


...


[module/mfcrate]
type = custom/script
exec = python3 $HOME/.config/polybar/castom/mfc_polybar.py
interval=15
click-left = firefox --new-window "https://mfcoin.net"
click-right = firefox --new-window "https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/mfcoin"
```
## test
test bolybar
```
polybar -c ~/.config/polybar/setevoy-polybar1.conf top
```