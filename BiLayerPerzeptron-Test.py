from BiLayerPerzeptron import BiLayerPerzeptron
import random as rand

## Example 1
print('Weights for AND: ')
AND = BiLayerPerzeptron(2, 1, [], [([0, 0], [0]), ([1, 0], [0]), ([0, 1], [0]), ([1, 1], [1])], 0.1, 3.14, 500, 0.0001)
print('AND([0, 0]): ' + str(AND([0, 0])))
print('AND([0, 1]): ' + str(AND([0, 1])))
print('AND([1, 0]): ' + str(AND([1, 0])))
print('AND([1, 1]): ' + str(AND([1, 1])))

## Example 2
print('Weights for OR: ')
OR = BiLayerPerzeptron(2, 1, [], [([0, 0], [0]), ([1, 0], [1]), ([0, 1], [1]), ([1, 1], [1])], 0.1, 3.14, 500, 0.0001)
print('OR([0, 0]): ' + str(OR([0, 0])))
print('OR([0, 1]): ' + str(OR([0, 1])))
print('OR([1, 0]): ' + str(OR([1, 0])))
print('OR([1, 1]): ' + str(OR([1, 1])))

## Example 3
print('Weights for XOR: ')
XOR = BiLayerPerzeptron(2, 1, [], [([0, 0], [0]), ([1, 0], [1]), ([0, 1], [1]), ([1, 1], [0])], 0.1, 3.14, 10000, 0.0001)
print('XOR([0, 0]): ' + str(XOR([0, 0])))
print('XOR([0, 1]): ' + str(XOR([0, 1])))
print('XOR([1, 0]): ' + str(XOR([1, 0])))
print('XOR([1, 1]): ' + str(XOR([1, 1])))
print('Sorry, it doesnt work well for XOR !!!')