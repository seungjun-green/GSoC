import re
def file2List(fileName):
    res = set()
    with open(fileName, 'r') as f:
        all = f.readlines()
        for curr in all:
            res.add(curr)
    return res


def saveList2FIle(fileName, data):
    with open(fileName, 'w') as f:
        for curr in data:
            f.write(curr)



def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()  # remove leading/trailing whitespace
            if line:  # ignore empty lines
                # remove starting number & dot using regex
                line = re.sub(r"^\d+\.\s*", "", line)
                outfile.write(line + '\n')







