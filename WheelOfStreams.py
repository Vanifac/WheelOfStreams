import argparse
import WheelOfNames
import logging
import sys
import WheelColors


# https://docs.python.org/3/library/argparse.html#the-add-argument-method
# https://docs.streamer.bot/api/sub-actions/core/system/run-a-program


testing = True

logger = logging.getLogger(__name__)
logging.basicConfig(filename='WheelOfStreams.log', encoding='utf-8', level=logging.INFO)


def build_args():
    test_args = None
    if testing:
        logging.info("---Starting Test---")

        import WheelSecrets
        test_args = f"-key {WheelSecrets.api_key} -wheel Wheel -add Vanifac".split(" ")
        # test_args = f"-key {WheelSecrets.api_key} -wheel Wheel -color Vanifac yellow".split(" ")
        # test_args = f"-key {WheelSecrets.api_key} -wheel Wheel -clear".split(" ")

        if test_args is None:
            logging.error("Test Args not set")
        logging.info(test_args)
    else:
        logging.info("---Starting---")
        logging.info(sys.argv[1:])

    parser = argparse.ArgumentParser(description="Configures WheelOfNames")

    parser.add_argument('-wheel', nargs=1, required=True)
    parser.add_argument('-key', nargs=1, required=True)

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('-add', nargs=1)
    action_group.add_argument('-color', nargs=2)
    action_group.add_argument('-clear', action='store_true')

    return parser.parse_args(test_args)


def get_wheel_by_name(data: list, wheel_name: str):
    for wheel in data:
        if wheel['config']['title'] == wheel_name:
            logging.info(f"Found wheel: {wheel_name}")
            return wheel
    return None


def add_entry(wheel: dict, name: str):
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
        logging.info("{name} not found, creating.")
        new_entry = {
            "text": name,
            "weight": 1,
            "enabled": True}
        wheel['config']['entries'].append(new_entry)
    return


def set_entry_color(wheel: dict, name: str, color: str) -> bool:
    logging.info(f"Setting Color for {name} to {color}")
    i = 0
    for entry in wheel['config']['entries']:
        if entry['text'] == name:
            if wheel['config']['entries'][i]['color'] == color:
                logging.info("Color already set")
                return False
            wheel['config']['entries'][i]['color'] = color
            return True
        i += 1

    return False


def clear_entrys(wheel: dict):
    for entry in wheel['config']['entries']:
        entry['weight'] = 0
        entry['enabled'] = False


def run():
    args = build_args()

    # Validate Color before doing anything
    if args.color:
        if (new_color := WheelColors.validate_color(args.color[1])) is None:
            logging.info("Invalid Color String")
            logging.info('---Exiting---')
            return
        else:
            # Set color argument to the validated color hex
            args.color[1] = new_color

    logging.info("Downloading Wheel")
    wheel_data = WheelOfNames.get_wheels(args.key[0])
    if 'error' in wheel_data.keys():
        logging.error('Invalid API key')
        logging.error(wheel_data['error'])
        logging.error('---Exiting---')
        return

    wheel = get_wheel_by_name(wheel_data['data']['wheels'], args.wheel[0])
    if wheel is None:
        logging.error('Wheel by that name not found')
        logging.error('---Exiting---')
        return

    upload = False
    if args.add:
        add_entry(wheel, args.add[0])
        upload = True
    elif args.color:
        if set_entry_color(wheel, args.color[0], args.color[1]):
            upload = True

    elif args.clear:
        clear_entrys(wheel)
        upload = True

    if upload:
        logging.info("Uploading Wheel")
        logging.info(WheelOfNames.send_wheel(args.key[0], wheel))
    logging.info("---Closing---")


run()
