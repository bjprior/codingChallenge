# required unique terms below 100
terms = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}

thousands = {1000: 'thousand', 1000000: 'million', 1000000000: 'billion', 1000000000000: 'trillion',
             1000000000000000: 'quadrillion'}

MAXINTEGER = 999999999999999999


class Number:
    def __init__(self, text):
        self.raw = text[:-1]
        self.wholeInt = self._parseInt()

    def print(self):
        """
        this function prints number in English text
        :return: No return value
        """
        string = self._integerToEnglish(self.wholeInt)
        string = placeAnd(string)
        print(string)

    def _parseInt(self):
        number = ""
        counter = 0

        # Cut off full stop, assumption in README

        # Collect all integers in string provided they are not proceeded by a non whitespace or integer (part 1)
        for char in self.raw:
            if counter > 0:
                if char.isdigit() and (self.raw[counter - 1] == ' ' or self.raw[counter - 1].isdigit()):
                    number += char
            elif char.isdigit():
                number += char
            counter += 1

        # Ensure only one integer is collected (part 2)
        stringParts = self.raw.split(" ")
        Integers = []
        for part in stringParts:
            if part.isdigit():
                Integers.append(int(part))

        if len(Integers) != 1:
            return "Invalid Number!"

        # Ensure part 1 matches part 2
        if Integers[0] != int(number):
            return "Invalid Number!"

        return Integers[0]

    def _integerToEnglish(self, num):
        if isinstance(num, str):
            return "number invalid"
        elif num > MAXINTEGER:
            return "number too large"
        else:
            assert (num >= 0)

            if num < 20:
                return terms[num]

            if num < 100:
                if num % 10 == 0:
                    return terms[num]
                else:
                    return terms[num // 10 * 10] + '-' + terms[num % 10]

            if num < 1000:
                if num % 100 == 0:
                    return terms[num // 100] + ' hundred'
                else:
                    return terms[num // 100] + ' hundred and ' + self._integerToEnglish(num % 100)

            for thou in thousands:
                if num < thou * 1000:
                    if num % thou == 0:
                        return self._integerToEnglish(num // thou) + ' ' + thousands[thou]
                    else:
                        return self._integerToEnglish(num // thou) + ' ' + thousands[
                            thou] + ', ' + self._integerToEnglish(
                            num % thou)


def placeAnd(string):
    """
    This function ensures the 'and' is placed correctly
    :param string
    :return: string with the and in correct place
    """
    comma = ','
    strAnd = 'and'
    lastComma = string.rfind(comma)
    lastAnd = string.rfind(strAnd)

    if lastComma < 0:
        return string
    if lastAnd > lastComma:
        return string
    else:
        return string[0:lastComma] + ' and' + string[lastComma + 1:]
