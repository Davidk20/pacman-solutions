"""
Main driver file for running the backend locally.

Inspiration taken from:

https://realpython.com/command-line-interfaces-python-argparse/
"""
import argparse
import sys

from solving_pacman_backend.server import server
from solving_pacman_backend.services.game_manager import GameManager

usage = """
Pac-Man Solutions - Back-End

Usage:
    python3 main.py command [options] [arguments]

Commands:

    server           Run the server application
    local            Run the CLI application

Options:
  -h --help          Show this screen.
  -v                 Verbose output.
  -n --level_num     Level number (Integer).
"""


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"\nError: {message}\n\n")
        self.print_help()
        sys.exit(2)


def main():
    parser = ArgParser(
        prog="main.py",
        description="""
        Pac-Man Solutions - Back-End: AI solutions to abstractions of Pac-Man levels.
        """,
    )

    parser.add_argument(
        "run_config",
        choices=["server", "local"],
        help="server = Run Flask server, local = Run single game",
    )

    local_options = parser.add_argument_group("Local Script Options")

    local_options.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=0,
        help="enable verbose output - full final state printing",
    )

    local_options.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=0,
        help="enable debug output - full final state printing + all noteworthy events",
    )

    parser.add_argument(
        "-l", "--level", type=int, help="specify level number as an integer"
    )

    args = parser.parse_args()

    match args.run_config:
        case "local":
            game = GameManager(args.level, local=True)
            game.start()
        case "server":
            server.app.run(host="0.0.0.0", debug=True, port=4000)


if __name__ == "__main__":
    main()
