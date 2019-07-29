#!/usr/bin/python

import sys
import os

def MainProcess():
    print("Weather Mini Challenge")

def main():
    try:
        MainProcess()
        sys.exit(0)
    except KeyboardInterrupt:
        print("Weather Mini Challenge Interrupted!")
        sys.exit(1)

if __name__ == "__main__":
    main()
