import argparse

from pymongo.errors import PyMongoError

from src.config.context.application_context import ApplicationContext
from src.config.context.development_context import DevelopmentContext

LAUNCH_DEVELOPMENT_CONTEXT_NAME = "dev"


def read_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Start the popato backend server")

    parser.add_argument(
        "--env",
        type=str,
        nargs="?",
        dest="env",
        choices=[
            LAUNCH_DEVELOPMENT_CONTEXT_NAME,
        ],
        default=LAUNCH_DEVELOPMENT_CONTEXT_NAME,
        help=(
            f"Specify if you want to launch the server in development ({LAUNCH_DEVELOPMENT_CONTEXT_NAME}) mode."
        ),
    )

    return parser.parse_args()


def get_application_context(args: argparse.Namespace) -> ApplicationContext:
    return DevelopmentContext()


def main():
    args = read_arguments()
    application_context = get_application_context(args)

    try:
        application_context.build_application()
        print("Application built.")
    except PyMongoError as e:
        print(e)
        print("Unable to connect to mongodb. Exiting.")
        exit(-1)
    except Exception as e:
        print(e)
        print("Something went wrong during the application building. Exiting")
        exit(-1)

    print("Starting application.")
    application_context.start_application()


if __name__ == "__main__":
    main()
