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
        self.validate(field)
        return field

    @staticmethod
    def validate(input_field):
        """ validates raw user input against problem domain requirements """
        field = input_field[:]  # make a copy
        header = field[0]
        if len(header) is not 3 or not any(char.isdigit() for char in header):
            raise BadInputFile("Bad field header; format is <w><space><h>")
        width, height = (int(x) for x in field[0].split(' '))
        del field[0]
        for line in field:
            if len(line) != width:
                raise BadInputFile("Bad field body; a line length was wrong")
        if len(field) != height:
            raise BadInputFile("Bad field body; field height was wrong")


class BadInputFile(Exception):
    pass


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


class Table():
    def __init__(self):
        self.can_fall = False
        self.accepts_rocks = False

    def __str__(self):
        return 'T'


class DoubleRock():
    def __init__(self):
        self.can_fall = True
        self.accepts_rocks = False

    def __str__(self):
        return ':'


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
                    below = position + 1
                    if below < self.height and column[below].accepts_rocks:
                        to_space = column[below]
                        from_space = column[position]
                        if isinstance(to_space, EmptySpace):
                            column[below] = from_space
                            column[position] = EmptySpace()
                        elif isinstance(to_space, SingleRock):
                            if isinstance(from_space, DoubleRock):
                                column[below] = DoubleRock()
                                column[position] = SingleRock()
                            elif isinstance(from_space, SingleRock):
                                column[below] = DoubleRock()
                                column[position] = EmptySpace()
                        else:
                            raise("Unexpected particle type below object")


    def undropped_exist(self):
        """ checks column for any rocks that haven't fully fallen """
        column = self.cells
        for position, obj in enumerate(column):
            below = position + 1
            if below < self.height:
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
            elif raw_object == 'T':
                return Table()
            elif raw_object == ':':
                return DoubleRock()
            else:
                raise BadInputFile("Unexpected particle character in input")

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
