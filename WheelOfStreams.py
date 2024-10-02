# import http.client
import argparse
# import config
# import WheelOfNames

# https://docs.python.org/3/library/argparse.html#the-add-argument-method
# https://docs.streamer.bot/api/sub-actions/core/system/run-a-program


testing = True


def build_args():
    test_args = None
    if testing:
        print("Testing")
        test_args = "-key 1342 -wheel Wheel -add vanifac".split(" ")

    parser = argparse.ArgumentParser(description="Configures WheelOfNames")

    parser.add_argument('-wheel', nargs=1, required=True)
    parser.add_argument('-key', nargs=1, required=True)

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('-add', nargs=1)
    action_group.add_argument('-clear')

    return parser.parse_args(test_args)


def run():
    args = build_args()
    if args.add:
        print("adding entry to", args.add[0])
    elif args.clear:
        print("clearing wheel")


run()
