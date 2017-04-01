""" rock_drop: simulates gravity for falling rocks in a particle field """
import fileinput
import sys
import pdb


class Reader():
    """ Validates, converts to internal repr raw particle field from STDIN """
    def read(self):
        """ reads in raw STDIN input """
        field = []
        data = fileinput.input()
        for line in data:
            field.append(line.strip('\n'))
        data.close()
        return field


class SingleRock():
    def __init__(self):
        self.can_fall = True
        self.accepts_rocks = True

    def __str__(self):
        return '.'

class EmptySpace():
    def __init__(self):
        self.can_fall = False
        self.accepts_rocks = True

    def __str__(self):
        return ' '


class NoSuchParticle(Exception):
    pass

class Column():
    """ Can apply gravity to a single 'column' in the particle field """
    def __init__(self, height):
        self.cells = []
        self.height = height

    def apply_gravity(self):
        column = self.cells
        while self.undropped_exist():
            for position, obj in enumerate(column):
                if obj.can_fall:
                    if position + 1 < self.height:
                        if column[position + 1].accepts_rocks:
                            accepts_rocks = column[position + 1]
                            rock_to_move = column[position]
                            column[position + 1] = rock_to_move
                            column[position] = accepts_rocks

    def undropped_exist(self):
        """ checks column for any rocks that haven't fully fallen """
        column = self.cells
        for position, obj in enumerate(column):
            below = position + 1
            if below < len(column):
                if obj.can_fall:
                    if column[below].accepts_rocks:
                        return True
        return False




class Simulator():
    """ Applies gravity to the particle field """
    def simulate(self, input_field):
        def _initialize_columns():
            columns = []
            for _ in range(width):
                columns.append(Column(height))
            return columns

        def _convert_to_object(raw_object):
            if raw_object == '.':
                return SingleRock()
            elif raw_object == ' ':
                return EmptySpace()
            else:
                raise NoSuchParticle("Unexpected particle character in input")

        dimensions = input_field[0].split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        del input_field[0]

        columns = _initialize_columns()
        for i in range(width):
            for j in range(height):
                raw_obj = input_field[j][i]
                obj = _convert_to_object(raw_obj)
                columns[i].cells.append(obj)
        for column in columns:
            column.apply_gravity()
        return columns

class Writer():
    """ Writes fully simulated (gravity applied) field as strings to STDOUT """
    def write(self, field):
        width = len(field[0].cells)
        height = len(field)
        rows = [[[] for x in range(height)] for y in range(width)]
        for col in range(height):
            for row in range(width):
                rows[row][col] = field[col].cells[row]
        output = ""
        for row in rows:
            for obj in row:
                output += str(obj)
            output += '\n'
        sys.stdout.write(output)
        return output

def main():
    reader = Reader()
    unsimulated_field = reader.read()

    simulator = Simulator()
    simulated_field = simulator.simulate(unsimulated_field)

    writer = Writer()
    writer.write(simulated_field)

if __name__ == "__main__":
    main()
