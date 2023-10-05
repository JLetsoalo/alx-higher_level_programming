#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    dir_names = dir(hidden_4)
    for name in dir_names:
        if name[:2] != "__":
            print(name)
