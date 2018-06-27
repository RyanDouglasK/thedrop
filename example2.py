import argparse

parser = argparse.ArgumentParser(description='wants to be grep')
parser.add_argument('word')
parser.add_argument('filepath')

args = parser.parse_args()

with open(args.filepath, 'r') as f:
    #print(f)
    file_contents = f.read()
    #print(file_contents)

print('is the word in the file')
print(args.word in file_contents)
