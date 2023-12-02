import argparse
import io

def main(input_file: io.TextIOWrapper):
    calibration = 0
    with input_file as file:
        for line in file:
            calibration += parse_line(line)
    print(calibration)


def parse_line(line: str) -> int:
    first = parse_first_number(line)    
    last = parse_last_number(line)    
    return int(first + last)


def parse_first_number(line: str) -> str:
    first = [i for i in line if i.isdigit()][0]
    return first


def parse_last_number(line: str) -> str:
    last = [i for i in line if i.isdigit()][-1]
    return last

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", type=argparse.FileType()) 
    args = parser.parse_args()

    main(args.input)

