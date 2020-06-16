# WPS PIN generator written in Python 3
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/wpspin.svg)](https://pypi.python.org/pypi/wpspin/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/wpspin.svg)](https://pypi.python.org/pypi/py3wifi/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/wpspin)
## Overview
WPS PIN generator uses known MAC address based algorithms commonly found in routers firmware to generate their default PINs. The PIN can be used with programs like [Reaver](https://github.com/t6x/reaver-wps-fork-t6x), [Bully](https://github.com/aanarchyy/bully)  or [OneShot](https://github.com/drygdryg/OneShot) to recover Wi-Fi password.
## Installation
```
pip install wpspin
```
Or you can install from source with:
```
git clone https://github.com/drygdryg/wpspin.git
cd wpspin/
python setup.py install
```
## Usage
### Command line tool
```
wpspin [-A] MAC
Required arguments:
    MAC              : target MAC address to generate PIN code. Example: 11:22:33:44:55:66
Optional arguments:
    -A, --get-all    : get all PIN codes in addition to the suggested ones for a single MAC
```
Example:
```
$ wpspin 54:A0:50:75:D2:40
Found 1 PIN(s)
PIN        Name
40414089   ASUS PIN

```
### Python module
Get all PINs for a single MAC
```python
>>> import wpspin
>>> generator = wpspin.WPSpin()
>>> generator.getAll('54:A0:50:75:D2:40')
[{'id': 'pin24', 'name': '24-bit PIN', 'pin': '77215369'}, {'id': 'pin28', 'name': '28-bit PIN', 'pin': '77215369'}, {'id': 'pin32', 'name': '32-bit PIN', 'pin': '98988167'}, {'id': 'pin36', 'name': '36-bit PIN', 'pin': '98988167'}, {'id': 'pin40', 'name': '40-bit PIN', 'pin': '46661760'}, {'id': 'pin44', 'name': '44-bit PIN', 'pin': '11772804'}, {'id': 'pin48', 'name': '48-bit PIN', 'pin': '13993603'}, {'id': 'pinDLink', 'name': 'D-Link PIN', 'pin': '76793011'}, {'id': 'pinDLink1', 'name': 'D-Link PIN +1', 'pin': '65690444'}, {'id': 'pinASUS', 'name': 'ASUS PIN', 'pin': '40414089'}, {'id': 'pinAirocon', 'name': 'Airocon Realtek', 'pin': '40774848'}, {'id': 'pinInvNIC', 'name': 'Inv NIC to PIN', 'pin': '90556791'}, {'id': 'pinNIC2', 'name': 'NIC * 2', 'pin': '54430723'}, {'id': 'pinNIC3', 'name': 'NIC * 3', 'pin': '31646086'}, {'id': 'pinOUIaddNIC', 'name': 'OUI + NIC', 'pin': '32676006'}, {'id': 'pinOUIsubNIC', 'name': 'OUI − NIC', 'pin': '78245280'}, {'id': 'pinOUIxorNIC', 'name': 'OUI ^ NIC', 'pin': '21918889'}, {'id': 'pinEmpty', 'name': 'Empty PIN', 'pin': ''}, {'id': 'pinCisco', 'name': 'Static PIN — Cisco', 'pin': '12345670'}, {'id': 'pinBrcm1', 'name': 'Static PIN — Broadcom 1', 'pin': '20172527'}, {'id': 'pinBrcm2', 'name': 'Static PIN — Broadcom 2', 'pin': '46264848'}, {'id': 'pinBrcm3', 'name': 'Static PIN — Broadcom 3', 'pin': '76229909'}, {'id': 'pinBrcm4', 'name': 'Static PIN — Broadcom 4', 'pin': '62327145'}, {'id': 'pinBrcm5', 'name': 'Static PIN — Broadcom 5', 'pin': '10864111'}, {'id': 'pinBrcm6', 'name': 'Static PIN — Broadcom 6', 'pin': '31957199'}, {'id': 'pinAirc1', 'name': 'Static PIN — Airocon 1', 'pin': '30432031'}, {'id': 'pinAirc2', 'name': 'Static PIN — Airocon 2', 'pin': '71412252'}, {'id': 'pinDSL2740R', 'name': 'Static PIN — DSL-2740R', 'pin': '68175542'}, {'id': 'pinRealtek1', 'name': 'Static PIN — Realtek 1', 'pin': '95661469'}, {'id': 'pinRealtek2', 'name': 'Static PIN — Realtek 2', 'pin': '95719115'}, {'id': 'pinRealtek3', 'name': 'Static PIN — Realtek 3', 'pin': '48563710'}, {'id': 'pinUpvel', 'name': 'Static PIN — Upvel', 'pin': '20854836'}, {'id': 'pinUR814AC', 'name': 'Static PIN — UR-814AC', 'pin': '43977680'}, {'id': 'pinUR825AC', 'name': 'Static PIN — UR-825AC', 'pin': '05294176'}, {'id': 'pinOnlime', 'name': 'Static PIN — Onlime', 'pin': '99956042'}, {'id': 'pinEdimax', 'name': 'Static PIN — Edimax', 'pin': '35611530'}, {'id': 'pinThomson', 'name': 'Static PIN — Thomson', 'pin': '67958146'}, {'id': 'pinHG532x', 'name': 'Static PIN — HG532x', 'pin': '34259283'}, {'id': 'pinH108L', 'name': 'Static PIN — H108L', 'pin': '94229882'}, {'id': 'pinONO', 'name': 'Static PIN — CBN ONO', 'pin': '95755212'}]
```
or without static PINs
```python
>>> generator.getAll('54:A0:50:75:D2:40', get_static=False)
[{'id': 'pin24', 'name': '24-bit PIN', 'pin': '77215369'}, {'id': 'pin28', 'name': '28-bit PIN', 'pin': '77215369'}, {'id': 'pin32', 'name': '32-bit PIN', 'pin': '98988167'}, {'id': 'pin36', 'name': '36-bit PIN', 'pin': '98988167'}, {'id': 'pin40', 'name': '40-bit PIN', 'pin': '46661760'}, {'id': 'pin44', 'name': '44-bit PIN', 'pin': '11772804'}, {'id': 'pin48', 'name': '48-bit PIN', 'pin': '13993603'}, {'id': 'pinDLink', 'name': 'D-Link PIN', 'pin': '76793011'}, {'id': 'pinDLink1', 'name': 'D-Link PIN +1', 'pin': '65690444'}, {'id': 'pinASUS', 'name': 'ASUS PIN', 'pin': '40414089'}, {'id': 'pinAirocon', 'name': 'Airocon Realtek', 'pin': '40774848'}, {'id': 'pinInvNIC', 'name': 'Inv NIC to PIN', 'pin': '90556791'}, {'id': 'pinNIC2', 'name': 'NIC * 2', 'pin': '54430723'}, {'id': 'pinNIC3', 'name': 'NIC * 3', 'pin': '31646086'}, {'id': 'pinOUIaddNIC', 'name': 'OUI + NIC', 'pin': '32676006'}, {'id': 'pinOUIsubNIC', 'name': 'OUI − NIC', 'pin': '78245280'}, {'id': 'pinOUIxorNIC', 'name': 'OUI ^ NIC', 'pin': '21918889'}, {'id': 'pinEmpty', 'name': 'Empty PIN', 'pin': ''}]
```
Get all PINs as list
```python
>>> generator.getList('54:A0:50:75:D2:40')
['77215369', '77215369', '98988167', '98988167', '46661760', '11772804', '13993603', '76793011', '65690444', '40414089', '40774848', '90556791', '54430723', '31646086', '32676006', '78245280', '21918889', '', '12345670', '20172527', '46264848', '76229909', '62327145', '10864111', '31957199', '30432031', '71412252', '68175542', '95661469', '95719115', '48563710', '20854836', '43977680', '05294176', '99956042', '35611530', '67958146', '34259283', '94229882', '95755212']
```
Get suggested PINs only
```python
>>> generator.getSuggested('54:A0:50:75:D2:40')
[{'id': 'pinASUS', 'name': 'ASUS PIN', 'pin': '40414089'}]
```
or as list
```python
>>> generator.getSuggestedList('54:A0:50:75:D2:40')
['40414089']
```
Generate specific PIN for a single MAC
```python
>>> generator.generate('pin24', '54:A0:50:75:D2:40')
'77215369'
```