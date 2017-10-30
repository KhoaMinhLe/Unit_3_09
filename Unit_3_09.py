# Created by: Khoa Le
# Created on October 2017
# Created for ICS3U
# This program is the "unichar with alphebets".

for number in range(65,91):
    alphabet = unichr(number)
    for number in range(97,123):
        alphabet_row_two = unichr(number)
        print(str(alphabet) + '=>' + str(alphabet_row_two))
