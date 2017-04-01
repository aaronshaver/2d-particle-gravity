import unittest
import rock_drop


class Case(unittest.TestCase):
    def setUp(self):
        self.reader = rock_drop.Reader()
        self.writer = rock_drop.Writer()
        self.simulator = rock_drop.Simulator()
        self.infix = '_in.txt'
        self.outfix = '_out.txt'

    def read_test_input(self, filename):
        output = []
        with open('data/' + filename + self.infix, 'r') as filedata:
            for line in filedata:
                output.append(line.strip('\n'))
        return output

    def read_test_output(self, filename):
        output = ""
        with open('data/' + filename + self.outfix, 'r') as filedata:
            for line in filedata:
                output += line
        return output

    def test_bad_height(self):
        test_input = self.read_test_input('bad_height')
        self.assertRaises(rock_drop.BadInputFile, self.reader.validate, test_input)

    def test_bad_width(self):
        test_input = self.read_test_input('bad_width')
        self.assertRaises(rock_drop.BadInputFile, self.reader.validate, test_input)

    def test_bad_header(self):
        test_input = self.read_test_input('bad_header')
        self.assertRaises(rock_drop.BadInputFile, self.reader.validate, test_input)

    def test_bad_particle_chars(self):
        test_input = self.read_test_input('bad_particle_chars')
        self.assertRaises(rock_drop.BadInputFile, self.simulator.simulate, test_input)

    def test_1x2_singlerock(self):
        test_input = self.read_test_input('1x2_singlerock')
        test_output = self.read_test_output('1x2_singlerock')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    @unittest.skip("haven't implemented double rock stacking yet")
    def test_1x8_severalsingles(self):
        test_input = self.read_test_input('1x8_severalsingles')
        test_output = self.read_test_output('1x8_severalsingles')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    @unittest.skip("haven't implmented double rocks yet")
    def test_2x2_twotypes(self):
        test_input = self.read_test_input('2x2_twotypes')
        test_output = self.read_test_output('2x2_twotypes')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    def test_2x3_singles(self):
        test_input = self.read_test_input('2x3_singles')
        test_output = self.read_test_output('2x3_singles')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    def test_4x3_singles(self):
        test_input = self.read_test_input('4x3_singles')
        test_output = self.read_test_output('4x3_singles')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)
