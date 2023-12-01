import argparse
import io

def main(input_file: io.TextIOWrapper):
    calibration = 0
    with input_file as file:
        for line in file:
            calibration += parse_line(line)
    print(calibration)


def parse_line(line: str) -> int:
    digits = [i for i in line if i.isdigit()]
    return int(digits[0] + digits[-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", type=argparse.FileType()) 
    args = parser.parse_args()

    main(args.input)

