# import http.client
import argparse
# import config
# import WheelOfNames

# https://docs.python.org/3/library/argparse.html#the-add-argument-method
# https://docs.streamer.bot/api/sub-actions/core/system/run-a-program


testing = True
args = None

if testing:
    print("Testing")
    args = "-add vanifac".split(" ")

parser = argparse.ArgumentParser(description="Configures WheelOfNames")

action_group = parser.add_mutually_exclusive_group()
action_group.add_argument('-add', nargs=1)
action_group.add_argument('-clear')

args = parser.parse_args(args)

if args.add:
    print("adding entry to", args.add[0])
