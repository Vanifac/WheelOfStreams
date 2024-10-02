# import http.client
import argparse


# https://docs.python.org/3/library/argparse.html#the-add-argument-method

parser = argparse.ArgumentParser(description="Configures WheelOfNames")

action_group = parser.add_mutually_exclusive_group()
action_group.add_argument("-add", "--add", action="store_true")
action_group.add_argument("-subtract", "--sub", action="store_true")

parser.add_argument("action", type=int)
parser.add_argument("chatter", type=int)

args = parser.parse_args()
