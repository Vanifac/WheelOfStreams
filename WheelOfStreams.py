import argparse
import WheelOfNames
# import json
import logging
import sys
import time

# https://docs.python.org/3/library/argparse.html#the-add-argument-method
# https://docs.streamer.bot/api/sub-actions/core/system/run-a-program


testing = False

logger = logging.getLogger(__name__)
logging.basicConfig(filename='WheelOfStreams.log', encoding='utf-8', level=logging.INFO)


def build_args():
    test_args = None
    if testing:
        print("Testing")
        logging.info("Starting Test")
        test_args = "-key baf23025-e96b-4feb-a3d5-ca807746adfb -wheel Wheel -add Vanifac".split(" ")
        logging.info(test_args)
        # test_args = "-key baf23025-e96b-4feb-a3d5-ca807746adfb -wheel Wheel -clear".split(" ")
    else:
        logging.info("Starting")
        logging.info(sys.argv)

    parser = argparse.ArgumentParser(description="Configures WheelOfNames")

    parser.add_argument('-wheel', nargs=1, required=True)
    parser.add_argument('-key', nargs=1, required=True)

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('-add', nargs=1)
    action_group.add_argument('-color', nargs=1)
    action_group.add_argument('-clear', action='store_true')
    return parser.parse_args(test_args)


def get_wheel_by_name(data: list, wheel_name: str):
    for wheel in data:
        if wheel['config']['title'] == wheel_name:
            logging.info(f"Found wheel: {wheel_name}")
            return wheel
    return None


def add_entry(wheel: dict, name: str):
    print("Adding entry to", name)
    logging.info(f"Adding entry to {name}")
    i = 0
    entry_found = False
    for entry in wheel['config']['entries']:
        if entry['text'] == name:
            wheel['config']['entries'][i]['weight'] += 1
            wheel['config']['entries'][i]['enabled'] = True
            entry_found = True
            break
        i += 1
    if not entry_found:
        print("Entry not Found")
        new_entry = {
            "text": name,
            "weight": 1,
            "enabled": True}
        wheel['config']['entries'].append(new_entry)
    return


def clear_entrys(wheel: dict):
    for entry in wheel['config']['entries']:
        entry['weight'] = 0
        entry['enabled'] = False


def run():
    args = build_args()
    wheel_data = WheelOfNames.get_wheels(args.key[0])

    wheel = get_wheel_by_name(wheel_data['data']['wheels'], args.wheel[0])
    if not wheel:
        print('wheel not found')
        logging.error('Wheel by that name not found')
        return

    if args.add:
        add_entry(wheel, args.add[0])
    elif args.color:
        print("setting color")
    elif args.clear:
        clear_entrys(wheel)
    WheelOfNames.send_wheel(args.key[0], wheel)


run()
