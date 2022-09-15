import csv 



def open_file_from_csv(file_relative_path):
    file = open(file_relative_path)
    type(file)
    csv_reader = csv.reader(file)
    return csv_reader

def read_headers(csv_reader):
    header = []
    header = next(csv_reader)
    return header


def __main__():
    relative_path = 'blocked_60hz_no_mass.xlsx'
    open_file_from_csv(relative_path)

    read_headers(open_file_from_csv(relative_path))

