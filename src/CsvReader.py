class CsvReader:
    def read_file(self, file_path):
        try:
            with open(file_path) as csv_list:
                return csv_list.read()
        except:
            print("File not found | %s" % (file_path))