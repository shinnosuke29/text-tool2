import sys
from itertools import zip_longest

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    differences = []
    for i, (line1, line2) in enumerate(zip_longest(lines1, lines2, fillvalue=''), start=1):
        if line1 != line2:
            if line1 == '':
                differences.append(f"Line {i}: Line present only in {file2}\n  File2: {line2.strip()}")
            elif line2 == '':
                differences.append(f"Line {i}: Line present only in {file1}\n  File1: {line1.strip()}")
            else:
                differences.append(f"Line {i}:\n  File1: {line1.strip()}\n  File2: {line2.strip()}")
    
    return differences

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 text_compare.py <file1> <file2>")
        sys.exit(1)
    
    file1, file2 = sys.argv[1], sys.argv[2]
    try:
        diffs = compare_files(file1, file2)
        if diffs:
            print("Differences found:")
            for diff in diffs:
                print(diff)
        else:
            print("Files are identical.")
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

