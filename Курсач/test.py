class Magazine:
    def __init__(self, capacity, diameter_range):
        self.capacity = capacity
        self.diameter_range = diameter_range
        self.contents = []

    def is_patron_fit(self, diameter):
        return self.diameter_range[0] <= diameter <= self.diameter_range[1]

    def insert_patron(self, patron):
        if len(self.contents) < self.capacity and self.is_patron_fit(patron.diameter):
            self.contents.append(patron)
            return True
        return False

class Patron:
    def __init__(self, id, diameter):
        self.id = id
        self.diameter = diameter

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

def main():
    # Чтение данных из файлов
    box1_data = read_file('box1.txt')[1:]
    magazine_data = read_file('magazine.txt')[1:]
    gilza_data = read_file('gilza.txt')[1:]
    box2_data = read_file('box2.txt')[1:]
    vibor_data = read_file('vibor.txt')

    # Инициализация магазина
    magazine = Magazine(int(magazine_data[0]), [float(d) for d in magazine_data[1].split(',')])

    # Инициализация списков для остатков и отстрелянных патронов
    box1_remaining = []
    box2_remaining = []
    gilza_shot = []

    # Инициализация списка подходящих патронов
    suitable_patrons = []

    # Заполнение коробочек и магазина
    for line in box1_data:
        id, diameter = [float(item) for item in line.split(',')]
        patron = Patron(id, diameter)

        if not magazine.insert_patron(patron):
            box1_remaining.append(line)
        else:
            suitable_patrons.append(diameter)

    for line in box2_data:
        id, diameter = [float(item) for item in line.split(',')]
        patron = Patron(id, diameter)

        if not magazine.insert_patron(patron):
            box2_remaining.append(line)
        else:
            suitable_patrons.append(diameter)

    # Запись результатов в файлы
    write_file('box1_remaining.txt', box1_remaining)
    write_file('box2_remaining.txt', box2_remaining)
    write_file('gilza_shot.txt', gilza_shot)
    write_file('suitable_patrons.txt', suitable_patrons)

if __name__ == "__main__":
    main()
