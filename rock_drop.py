import fileinput
import sys
import pdb


class Reader():
    def read(self):
        field = []
        data = fileinput.input()
        for line in data:
            field.append(line.strip('\n'))
        data.close()
        return field


class Simulator():

    def undropped_exist(self, column):
        for position, obj in enumerate(column):
            if position + 1 < len(column):
                if obj == '.':
                    if column[position + 1] == ' ':
                        return True
        return False

    def simulate(self, input_field):
        dimensions = input_field[0].split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        del input_field[0]
        out = [['' for x in range(height)] for y in range(width)]
        for i, row in enumerate(input_field):
            for j, col in enumerate(row):
                out[j][i] = col
        for column in out:
            while self.undropped_exist(column):
                for position, obj in enumerate(column):
                    if column[position] == '.':
                        if position + 1 < height:
                            if column[position + 1] == ' ':
                                accepts_rocks = column[position + 1]
                                rock_to_move = column[position]
                                column[position + 1] = rock_to_move
                                column[position] = ' '
        return out

class Writer():
    def write(self, field):
        width = len(field[0])
        height = len(field)
        rows = [[[] for x in range(height)] for y in range(width)]
        for col in range(height):
            for row in range(width):
               rows[row][col] = field[col][row] 
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
