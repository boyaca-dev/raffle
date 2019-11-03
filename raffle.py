from random import shuffle, choice

from tabulate import tabulate

prizes = [
    'Licencia JetBrains #1',
    'Licencia JetBrains #2',
    'Entrada ScaleConf #1',
    'Entrada ScaleConf #2',
    'Entrada Pycon',
    'Cursos Net University #1',
    'Cursos Net University #2',
    'Cursos Net University #3',
    'Cursos Net University #4',
    'Cursos Net University #5',
    'Paquete JSConf #1',
    'Paquete JSConf #2',
    'Paquete JSConf #3',
    'Paquete JSConf #4',
    'Paquete JSConf #5',
    'Paquete JSConf #6',
    'Pin ScaleConf #1',
    'Pin ScaleConf #2',
    'Pin ScaleConf #3'
]


# noinspection PyBroadException
def get_attendees():
    attendees = []
    try:
        f = open('./attendees.txt', 'r')
    except Exception:
        return []
    lines = f.readlines()
    if len(lines) > 1:
        lines.pop(0)
    for line in lines:
        full_name = ''
        is_here = False
        try:
            portions = line.split(',')
            full_name = portions[4]
            is_here = str(portions[32]) == '1'
        except Exception:
            pass
        if len(full_name) > 0 and is_here:
            attendees.append(full_name)
    return attendees


def main():
    attendees = get_attendees()
    if len(attendees) <= 0:
        print("No hay asistentes registrados")
        return 1
    shuffle(attendees)
    indices = range(len(attendees))
    winners_indices = []
    while len(winners_indices) < len(prizes):
        winners_indices.append(choice(indices))
        winners_indices = list(set(winners_indices))
    winners = [attendees[i] for i in winners_indices]
    shuffle(winners)
    assigned_prizes = [[i + 1, prizes[i], attendees[i]] for i in range(len(prizes))]
    print(tabulate(assigned_prizes, headers=['No.', 'Prize', 'Winner'], tablefmt='orgtbl'))
    return 0


if __name__ == '__main__':
    main()
