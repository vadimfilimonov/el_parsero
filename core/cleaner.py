class Clear:

    @staticmethod
    def delrubbish(x):
        import re
        x = re.sub("^\s+|\n|\r|\t|\s*$|\t*$;", '', x)
        x = re.sub('"', "'", x)
        return x

    @staticmethod
    def toBlue(x):
        x = '\033[96m' + x + '\033[0m'
        return x