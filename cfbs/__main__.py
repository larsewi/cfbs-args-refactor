#!/usr/bin/env python3
if __name__ == "__main__":
    import os
    import sys

    above_dir = os.path.dirname(os.path.realpath(__file__)) + "/../"
    abspath = os.path.abspath(above_dir)
    sys.path.insert(0, abspath)

    from cfbs.main import main

    exit_status = main()
    sys.exit(exit_status)
