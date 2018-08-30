def normalize_snils(snils):
    snils = str(snils)
    while len(snils) < 11:
        snils = '0' + snils
    snils = f'{snils[0:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:11]}'
    return snils


def check_snils(snils):
    if len(snils) != 14:
        return False

    def snils_csum(snils):
        k = range(9, 0, -1)
        pairs = zip(k, [int(x) for x in snils.replace('-', '').replace(' ', '')[:-2]])
        return sum([k * v for k, v in pairs])

    csum = snils_csum(snils)

    while csum > 101:
        csum %= 101
    if csum in (100, 101):
        csum = 0

    return csum == int(snils[-2:])