import unittest
import rock_drop


class Case(unittest.TestCase):
    def setUp(self):
        self.reader = rock_drop.Reader()
        self.writer = rock_drop.Writer()
        self.simulator = rock_drop.Simulator()

    def read_test_input(self, filename):
        output = []
        with open('data/' + filename + '.txt', 'r') as filedata:
            for line in filedata:
                output.append(line.strip('\n'))
        return output

    def read_test_output(self, filename):
        output = ""
        with open('data/' + filename + '.txt', 'r') as filedata:
            for line in filedata:
                output += line
        return output

    def test_1x2_singlerock(self):
        test_input = self.read_test_input('1x2_singlerock_in')
        test_output = self.read_test_output('1x2_singlerock_out')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    def test_1x8_severalsingles(self):
        test_input = self.read_test_input('1x8_severalsingles_in')
        test_output = self.read_test_output('1x8_severalsingles_out')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    def test_2x2_twotypes(self):
        test_input = self.read_test_input('2x2_twotypes_in')
        test_output = self.read_test_output('2x2_twotypes_out')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)

    def test_2x3_singles(self):
        test_input = self.read_test_input('2x3_singles_in')
        test_output = self.read_test_output('2x3_singles_out')
        simulated = self.simulator.simulate(test_input)
        self.assertEqual(self.writer.write(simulated), test_output)
