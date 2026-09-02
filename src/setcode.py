import sys
import argparse
def parseArgs():
	Parser = argparse.ArgumentParser(prog="setcode", description="Exit with the specified code.", allow_abbrev=False)
	Parser.add_argument("code", type=int, help="Exit code to use.")
	Parser.add_argument("-v", "--version", action="version", version="%(prog)s version 1.0")
	return Parser.parse_args()
def main():
	sys.exit(parseArgs().code)
if __name__ == "__main__":
	main()