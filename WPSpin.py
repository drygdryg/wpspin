# -*- coding: utf-8 -*-
class WPSException(Exception):
    pass


class WPSpin(object):
    '''WPS pin generator'''
    def __init__(self):
        self.ALGO_MAC = 0
        self.ALGO_EMPTY = 1
        self.ALGO_STATIC = 2

        self.algos = {}
        self.algos['pin24'] = {'name': '24-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin24}
        self.algos['pin28'] = {'name': '28-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin28}
        self.algos['pin32'] = {'name': '32-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin32}
        self.algos['pin36'] = {'name': '36-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin36}
        self.algos['pin40'] = {'name': '40-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin40}
        self.algos['pin44'] = {'name': '44-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin44}
        self.algos['pin48'] = {'name': '48-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.pin48}
        self.algos['pinDLink'] = {'name': 'D-Link PIN', 'mode': self.ALGO_MAC, 'gen': self.pinDLink}
        self.algos['pinDLink1'] = {'name': 'D-Link PIN +1', 'mode': self.ALGO_MAC, 'gen': self.pinDLink1}
        self.algos['pinASUS'] = {'name': 'ASUS PIN', 'mode': self.ALGO_MAC, 'gen': self.pinASUS}
        self.algos['pinAirocon'] = {'name': 'Airocon Realtek', 'mode': self.ALGO_MAC, 'gen': self.pinAirocon}
        self.algos['pinInvNIC'] = {'name': 'Inv NIC to PIN', 'mode': self.ALGO_MAC, 'gen': self.pinInvNIC}
        self.algos['pinNIC2'] = {'name': 'NIC * 2', 'mode': self.ALGO_MAC, 'gen': self.pinNIC2}
        self.algos['pinNIC3'] = {'name': 'NIC * 3', 'mode': self.ALGO_MAC, 'gen': self.pinNIC3}
        self.algos['pinOUIaddNIC'] = {'name': 'OUI + NIC', 'mode': self.ALGO_MAC, 'gen': self.pinOUIaddNIC}
        self.algos['pinOUIsubNIC'] = {'name': 'OUI − NIC', 'mode': self.ALGO_MAC, 'gen': self.pinOUIsubNIC}
        self.algos['pinOUIxorNIC'] = {'name': 'OUI ^ NIC', 'mode': self.ALGO_MAC, 'gen': self.pinOUIxorNIC}
        # Static pin algos
        self.algos['pinEmpty'] = {'name': 'Empty PIN', 'mode': self.ALGO_EMPTY, 'gen': lambda mac: ''}
        self.algos['pinCisco'] = {'name': 'Cisco', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 1234567}
        self.algos['pinBrcm1'] = {'name': 'Broadcom 1', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 2017252}
        self.algos['pinBrcm2'] = {'name': 'Broadcom 2', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4626484}
        self.algos['pinBrcm3'] = {'name': 'Broadcom 3', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 7622990}
        self.algos['pinBrcm4'] = {'name': 'Broadcom 4', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6232714}
        self.algos['pinBrcm5'] = {'name': 'Broadcom 5', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 1086411}
        self.algos['pinBrcm6'] = {'name': 'Broadcom 6', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3195719}
        self.algos['pinAirc1'] = {'name': 'Airocon 1', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3043203}
        self.algos['pinAirc2'] = {'name': 'Airocon 2', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 7141225}
        self.algos['pinDSL2740R'] = {'name': 'DSL-2740R', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6817554}
        self.algos['pinRealtek1'] = {'name': 'Realtek 1', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9566146}
        self.algos['pinRealtek2'] = {'name': 'Realtek 2', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9571911}
        self.algos['pinUpvel'] = {'name': 'Upvel', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 2085483}
        self.algos['pinUR814AC'] = {'name': 'UR-814AC', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4397768}
        self.algos['pinUR825AC'] = {'name': 'UR-825AC', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 529417}
        self.algos['pinOnlime'] = {'name': 'Onlime', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9995604}
        self.algos['pinEdimax'] = {'name': 'Edimax', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3561153}
        self.algos['pinThomson'] = {'name': 'Thomson', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6795814}
        self.algos['pinHG532x'] = {'name': 'HG532x', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3425928}
        self.algos['pinH108L'] = {'name': 'H108L', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9422988}
        self.algos['pinONO'] = {'name': 'CBN ONO', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9575521}

    def _parseMac(self, mac):
        mac = mac.replace(':', '').replace('-', '').replace('.', '')
        mac = int(mac, 16)
        return mac

    def checksum(self, pin):
        '''
        Standard WPS checksum algorithm.
        @pin — A 7 digit pin to calculate the checksum for.
        Returns the checksum value.
        '''
        accum = 0
        while pin:
            accum += (3 * (pin % 10))
            pin = int(pin / 10)
            accum += (pin % 10)
            pin = int(pin / 10)
        return ((10 - accum % 10) % 10)

    def generate(self, algo, mac):
        '''
        WPS pin generator
        @algo — the WPS pin algorithm ID
        Returns the WPS pin string value
        '''
        mac = self._parseMac(mac)
        if algo not in self.algos:
            raise WPSException('Invalid WPS pin algorithm')
        pin = self.algos[algo]['gen'](mac)
        if algo == 'pinEmpty':
            return pin
        pin = pin % 10000000
        pin = str(pin) + str(self.checksum(pin))
        return pin.zfill(8)

    def getAll(self, mac, get_static=True):
        '''
        Get all WPS pin's for single MAC
        '''
        res = []
        for ID, algo in self.algos.items():
            if algo['mode'] == self.ALGO_STATIC and not get_static:
                continue
            item = {}
            item['id'] = ID
            if algo['mode'] == self.ALGO_STATIC:
                item['name'] = 'Static PIN — ' + algo['name']
            else:
                item['name'] = algo['name']
            item['pin'] = self.generate(ID, mac)
            res.append(item)
        return res

    def getList(self, mac, get_static=True):
        res = []
        for ID, algo in self.algos.items():
            if algo['mode'] == self.ALGO_STATIC and not get_static:
                continue
            res.append(self.generate(ID, mac))
        return res

    def pin24(self, mac):
        return (mac & 0xFFFFFF)

    def pin28(self, mac):
        return (mac & 0xFFFFFFF)

    def pin32(self, mac):
        return (mac % 0x100000000)

    def pin36(self, mac):
        return (mac % 0x1000000000)

    def pin40(self, mac):
        return (mac % 0x10000000000)

    def pin44(self, mac):
        return (mac % 0x100000000000)

    def pin48(self, mac):
        return mac

    def pinDLink(self, mac):
        # Get the NIC part
        nic = mac & 0xFFFFFF
        # Calculating pin
        pin = nic ^ 0x55AA55
        pin ^= (((pin & 0xF) << 4) +
                ((pin & 0xF) << 8) +
                ((pin & 0xF) << 12) +
                ((pin & 0xF) << 16) +
                ((pin & 0xF) << 20))
        pin %= int(10e6)
        if pin < int(10e5):
            pin += ((pin % 9) * int(10e5)) + int(10e5)
        return pin

    def pinDLink1(self, mac):
        return self.pinDLink(mac + 1)

    def pinASUS(self, mac):
        mac = hex(mac).split('x')[-1].upper().zfill(12)
        b = []
        for i in range(0, 12, 2):
            b.append(int(mac[i:i+2], 16))
        pin = ''
        for i in range(7):
            pin += str((b[i % 6] + b[5]) % (10 - (i + b[1] + b[2] + b[3] + b[4] + b[5]) % 7))
        return int(pin)

    def pinAirocon(self, mac):
        mac = hex(mac).split('x')[-1].upper().zfill(12)
        b = []
        for i in range(0, 12, 2):
            b.append(int(mac[i:i+2], 16))
        pin = ((b[0] + b[1]) % 10)\
        + (((b[5] + b[0]) % 10) * 10)\
        + (((b[4] + b[5]) % 10) * 100)\
        + (((b[3] + b[4]) % 10) * 1000)\
        + (((b[2] + b[3]) % 10) * 10000)\
        + (((b[1] + b[2]) % 10) * 100000)\
        + (((b[0] + b[1]) % 10) * 1000000)
        return pin

    def pinInvNIC(self, mac):
        nic = mac & 0xFFFFFF
        pin = ~nic & 0xFFFFFF
        return pin

    def pinNIC2(self, mac):
        nic = mac & 0xFFFFFF
        pin = nic * 2
        return pin

    def pinNIC3(self, mac):
        nic = mac & 0xFFFFFF
        pin = nic * 3
        return pin

    def pinOUIaddNIC(self, mac):
        mac = hex(mac).split('x')[-1].upper().zfill(12)
        oui = int(mac[:6], 16)
        nic = int(mac[6:], 16)
        pin = (oui + nic) % int(10e6)
        return pin

    def pinOUIsubNIC(self, mac):
        mac = hex(mac).split('x')[-1].upper().zfill(12)
        oui = int(mac[:6], 16)
        nic = int(mac[6:], 16)
        pin = oui - nic if nic < oui else (oui + int(10e6) - nic) & 0xFFFFFF
        return pin

    def pinOUIxorNIC(self, mac):
        mac = hex(mac).split('x')[-1].upper().zfill(12)
        oui = int(mac[:6], 16)
        nic = int(mac[6:], 16)
        pin = oui ^ nic
        return pin
