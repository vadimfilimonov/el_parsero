class Count:

    @staticmethod
    def rowsnumber(file):
        f = open(file)
        filelength = 0
        for i in f:
            filelength += 1
        f.close()
        return filelength