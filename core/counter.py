class Count:

    @staticmethod
    def rowsnumber(filename):
        file = open(filename)
        content = file.read()
        content_list = content.split('\n')
        return len(content_list)
