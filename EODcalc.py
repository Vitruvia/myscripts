import sys


class EODconverter(object):
    """
    An object relating weekly doses to EOD doses
    """

    def __init__(self):
        """
        generate a tuple with weekly and EOD values
        """
        self.value_dict = {}

    @staticmethod
    def eod_convert(weekly):
        """
        Takes the weekly value and converts it to EOD injections
        """
        return 8 * weekly / 28

    def eod_new(self, weekly):
        converted = self.eod_convert(weekly)
        self.value_dict[weekly] = converted
        print(self.value_dict)
        return


if __name__ == "__main__":
    new_converter = EODconverter()
    new_converter.eod_new(int(sys.argv[1]))
