import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))

        return data

def selection_sort(number_array, direction='ascending'):
    for i in range(len(number_array) - 1):
        min_idx = i
        for num_idx in range(i + 1, len(number_array)):
            if direction == 'ascending':
                if number_array[min_idx] > number_array[num_idx]:
                    min_idx = num_idx
            elif direction == 'descending':
                if number_array[min_idx] < number_array[num_idx]:
                    min_idx = num_idx
        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]

    return number_array

def bubble_sort(numbers):
    for k in range(len(numbers) - 1):
        for n in range(len(numbers) - k - 1):
            if numbers[n] > numbers[n + 1]:
                numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]

    return numbers

def insertion_sort(datas):
    for m in range(1, len(datas)):
        key = datas[m]
        l = m - 1
        while l >= 0 and datas[l] > key:
            datas[l + 1] = datas[l]
            l = l - 1
        datas[l + 1] = key

    return datas

def main():
    data = read_data('numbers.csv')
    print(data)
    # sorted_array = selection_sort(data['series_1'].copy(), 'descending')
    # print(sorted_array)
    # bubbles = bubble_sort(data['series_1'].copy())
    # print(bubbles)
    print(insertion_sort(data['series_1'].copy()))

if __name__ == '__main__':
    main()
