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


class Column():
    """ Can apply gravity to a single 'column' in the particle field """
    def __init__(self, height):
        self.cells = []
        self.height = height

    def apply_gravity(self):
        column = self.cells
        while self.undropped_exist():
            for position, obj in enumerate(column):
                if obj == '.':
                    if position + 1 < self.height:
                        if column[position + 1] == ' ':
                            accepts_rocks = column[position + 1]
                            rock_to_move = column[position]
                            column[position + 1] = rock_to_move
                            column[position] = accepts_rocks

    def undropped_exist(self):
        """ checks column for any rocks that haven't fully fallen """
        column = self.cells
        for position, obj in enumerate(column):
            if position + 1 < len(column):
                if obj == '.':
                    if column[position + 1] == ' ':
                        return True
        return False

class Simulator():
    """ Applies gravity to the particle field """
    def simulate(self, input_field):
        dimensions = input_field[0].split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        del input_field[0]
        columns = []
        for i in range(width):
            columns.append(Column(height))
        for i in range(width):
            for j in range(height):
               columns[i].cells.append(input_field[j][i])
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
            output += "".join(row) + '\n'
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
