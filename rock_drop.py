""" simulates gravity for falling rocks in a particle field """
import fileinput
import sys
from field_objects import SingleRock, DoubleRock, EmptySpace, Table


class Reader():
    """ validates, converts to internal repr raw particle field from STDIN """
    def read(self):
        """ reads in particle field via raw STDIN input """
        field = []
        data = fileinput.input()
        for line in data:
            field.append(line.strip('\n'))
        data.close()
        self.validate(field)
        return field

    @staticmethod
    def validate(field):
        """ validates raw user input against problem domain requirements """
        header = field[0]
        if len(header) < 3 or not any(char.isdigit() for char in header):
            raise BadInputFile("Bad field header; format is <w><space><h>")

        width, height = (int(x) for x in field[0].split(' '))
        for line in field[-1:]:
            if len(line) != width:
                raise BadInputFile("Bad field body; a line length was wrong")

        if len(field) - 1 != height:  # -1 because we ignore header
            raise BadInputFile("Bad field body; field height was wrong")


class BadInputFile(Exception):
    """ custom error for when user's input didn't follow the spec """
    pass


class Column():
    """ a single vertical slice of the particle field; can apply gravity to the
    slice """
    def __init__(self, height):
        self.cells = []
        self.height = height

    def apply_gravity(self):
        """ the 'core' of the program: applies the physics rules to a vertical
        column of a mix of empty space, fixed objects, and falling objects """
        column = self.cells
        while self._undropped_exist():
            for position, obj in enumerate(column):
                below = position + 1
                if obj.can_fall and below < self.height and column[below].accepts_rocks:
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
                        raise "Unexpected particle type below object"


    def _undropped_exist(self):
        """ Checks column for any objects that haven't fully dropped """
        column = self.cells
        for position, obj in enumerate(column):
            below = position + 1
            if below < self.height and obj.can_fall:
                if column[below].accepts_rocks:
                    return True
        return False


class Simulator():
    """ Applies gravity to the particle field """
    @staticmethod
    def simulate(input_field):
        """ processes the raw input particle field into a fully simulated field
        (i.e. all rocks have fallen) """
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
        del input_field[0]  # strip header, leaving only particle field

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
    """ writes fully simulated (gravity applied) field as strings to STDOUT """
    @staticmethod
    def write(field):
        """ prints the fully simulated particle field to STDOUT """
        width = len(field[0].cells)
        height = len(field)

        # transpose from columns to rows, and populate for writing
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
    """ end-to-end program: reads, simulates, and writes a particle field """
    reader = Reader()
    unsimulated_field = reader.read()

    simulator = Simulator()
    simulated_field = simulator.simulate(unsimulated_field)

    writer = Writer()
    writer.write(simulated_field)

if __name__ == "__main__":
    main()
