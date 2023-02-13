"""Console script for ping."""
import logging
import argparse
import sys


from ping import PingManager


def main():
    """Console script for ping."""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="hello.out", help="File to which message is written.")
    parser.add_argument("url", help="URL which is pinged.")
    args = parser.parse_args()

    manager = PingManager()
    manager.run(args.file, args.url)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
