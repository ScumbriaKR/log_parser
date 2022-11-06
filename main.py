import sys
import os

if len(sys.argv) == 1:
    print("Path to file or folder must be here :\\")
else:
    errors = open("errors.log", "w")
    for filename in os.listdir(sys.argv[1]):
        with open(os.path.join(sys.argv[1], filename), 'r') as f:
            for line in f:
                if line.lower().find("error") != -1:
                    errors.write(line)
        f.close()
    errors.close()
