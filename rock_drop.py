import fileinput
import sys


class Reader():
    def read(self):
        field = []
        data = fileinput.input()
        for line in data:
            field.append(line.strip('\n'))
        data.close()
        return field


class Simulator():
    def simulate(self, input_field):
        print("field at beginning of simulator", input_field)
        dimensions = input_field[0].split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        del input_field[0]
        print("input_field truncated", input_field)
        print("width, height", width, height)
        out = [['' for x in range(width)] for y in range(height)]
        for i, row in enumerate(input_field):
            for j, col in enumerate(row):
                out[i][j] = col
        print("fields before gravity", out)
        for position, obj in enumerate(out):
            print("position, obj", position, obj)
            if obj[0] == '.':
                print("match")
                print("position, +1", position, position + 1, height)
                if position + 1 < height:
                    if out[position + 1][0] == ' ':
                        print("yep, empty")
                        print("out before swap", out)
                        accepts_rocks = out[position + 1]
                        rock_to_move = out[position]
                        out[position + 1] = rock_to_move
                        out[position] = [' ']
                        print("out after swap", out)
        print("field at end of Simulator", out)
        return out

class Writer():
    def write(self, field):
        print("field coming into Writer ", field)
        height = len(field)
        rows = [[] for x in range(height)]
        print("ROWS", rows)
        for i, row in enumerate(field):
            rows[i].extend(row)
        output = ""
        print("rows after de-rowizing", rows)
        for line in rows:
            print("doing a line...")
            print("line|" + str(line) + "|")
            for char in line:
                print("doing a char...")
                output += char
            output += '\n'
        print("//")
        sys.stdout.write(output)
        print("//")
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
