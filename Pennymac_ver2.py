def getData(file):
    """
    Read each line in the file as a string and store as an element in a list.

    """
    lst = []
    f = open(file)
    for line in f.readlines():
        # Replace unnecessary characters with empty space
        line = line.replace('-', " ").replace('*', " ")
        # Eliminate any blank lines
        if line.strip():
            lst += [line]
    return lst


def header_index(header):
    """
    Return the index of where each column name starts

    """
    col_names = header.split()
    indexes = []
    start = 0
    for word in col_names:
        # find the index of first occurrence of the column name in the header string after index start
        index = header.find(word, start)
        start = index + len(word)  # e.g.: if not track, the index of 'PDir' will be returned when we want 'Dir'.
        indexes += [index]
    return indexes + [len(header)]


def header_index_range(indexes):
    """
    [1, 4, 5] ---> [[1, 4], [4, 5]]
    """

    column_index = []
    for first, last in zip(indexes, indexes[1:]):
        column_index += [[first, last]]
    return column_index


def empty_matrix(row_size, col_size):
    """
    Create a row_size x col_size matrix filled with zero.

    """
    return [[0 for i in range(col_size)] for j in range(row_size)]


def data_matrix(raw_data, row_size, col_size, col_index):
    """
    Fill the matrix with corresponding data
    """
    data = empty_matrix(row_size, col_size)
    for row_num in range(row_size):
        pointer = 0
        words = raw_data[row_num].split()
        for word in words:
            index = raw_data[row_num].find(word, pointer) + len(word) #the index of where the entry ends
            pointer = index
            for column_num in range(col_size):
                # Check if the index is in the column range
                if col_index[column_num][0] <= index < col_index[column_num][1]:
                    data[row_num][column_num] = word
                    break;
    return data


def data_dictionary(data_matrix):
    """
    Return a dictionary with
    key: headers
    value: data for each header
    """
    data_dict = {}
    headers = data_matrix[0]
    for i in range(len(headers)):
        data_dict[headers[i]] = [x[i] for x in data_matrix[1:]]
    return data_dict


# convert a column of strings to floats
def convertStr(colA):
    for i in range(len(colA)):
        colA[i] = float(colA[i])
    return colA


# Take the absolute difference between two columns, sort the difference, and return the least one
def leastDiffItem(itemCol, colA, colB):
    difference = [[item, abs(a - b)] for item, a, b in zip(itemCol, colA, colB)]
    sorted_diff = sorted(difference, key=lambda x: x[1])
    return sorted_diff[0][0]

def result(file, id, colA, colB):
    raw_data = getData(file)
    header = raw_data[0]

    indexes = header_index(header)
    col_index = header_index_range(indexes)

    row_size = len(raw_data)
    col_size = len(col_index)
    matrix = data_matrix(raw_data, row_size, col_size, col_index)
    data = data_dictionary(matrix)

    id_col = data[id]
    col_A = convertStr(data[colA])
    col_B = convertStr(data[colB])
    # return result
    return leastDiffItem(id_col, col_A, col_B)

if __name__ == "__main__":
    print('Smallest temperature spread is on day', result('w_data.dat', 'Dy', 'MxT', 'MnT'))
    print("The team with the smallest difference in 'for' and 'against' goals is", result('soccer.dat', 'Team', 'F', 'A'))

