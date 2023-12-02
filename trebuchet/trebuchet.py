import argparse
import io

TEXT_TO_NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main(input_file: io.TextIOWrapper):
    with input_file as file:
        calibration = calibration_sum(file)
    print(calibration)

def calibration_sum(data):
    calibration = 0
    for line in data:
        calibration += parse_line(line.strip())

    return calibration


def parse_line(line: str) -> int:
    first = parse_first_number(line)    
    last = parse_last_number(line)    
    return int(first + last)


def parse_first_number(line: str) -> str:
    for i, v in enumerate(line):
        if v.isdigit():
            return v

        for k in TEXT_TO_NUMBERS:
            if line[i:i + len(k)] == k:
                return TEXT_TO_NUMBERS[k]

    raise ValueError("Couldn't parse first number")
        


def parse_last_number(line: str) -> str:
    for i in range(len(line) - 1, 0, -1):
        v = line[i]
        if v.isdigit():
            return v

        for k in TEXT_TO_NUMBERS:
            subline = line[i - len(k) + 1:i + 1]
            if subline == k:
                return TEXT_TO_NUMBERS[k]

    raise ValueError("Couldn't parse last number")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", type=argparse.FileType()) 
    args = parser.parse_args()

    main(args.input)

