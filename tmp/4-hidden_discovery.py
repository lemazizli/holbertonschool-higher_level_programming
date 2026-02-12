#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    all_names = dir(hidden_4)
    all_names.sort()
    for name in all_names:
        if not name.startswith("__"):
            print(name)
