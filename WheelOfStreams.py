import argparse
import WheelOfNames
import logging
import WheelColors


# https://docs.python.org/3/library/argparse.html
# https://docs.streamer.bot/api/sub-actions/core/system/run-a-program


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='WheelOfStreams.log',
    encoding='utf-8',
    level=logging.INFO,
    force=True,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def build_args():
    logging.info("---Parsing Arguments---")

    parser = argparse.ArgumentParser(description="Configures WheelOfNames")

    parser.add_argument('-test', action='store_true')
    parser.add_argument('-key', nargs=1, required=True)
    parser.add_argument('-wheel', nargs=1, required=True)

    wheel_type_group = parser.add_mutually_exclusive_group(required=True)
    wheel_type_group.add_argument('-shared', action='store_true')
    wheel_type_group.add_argument('-private', action='store_true')

    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('-add', nargs=1)
    action_group.add_argument('-color', nargs=2)
    action_group.add_argument('-clear', action='store_true')

    return parser.parse_args()


def get_wheel_by_name_or_path(data: list, identifier: str):
    logging.info(f"Looking for wheel: {identifier}")
    for wheel in data:
        logging.info(f"Checking wheel: {wheel['config']['title']} - {wheel['path']}")
        if wheel['path'] == identifier or wheel['config']['title'] == identifier:
            logging.info(f"Wheel Match: {identifier}")
            return wheel['config']

    return None


def add_entry(wheel: dict, name: str):
    logging.info(f"Adding entry to {name}")
    i = 0
    entry_found = False
    for entry in wheel['entries']:
        if entry['text'] == name:
            # print(entry)
            wheel['entries'][i]['weight'] += 1
            wheel['entries'][i]['enabled'] = True
            entry_found = True
            # print(entry)
            print(wheel['entries'][i]['weight'])
            break
        i += 1
    if not entry_found:
        logging.info(f"{name} not found, creating.")
        new_entry = {
            "weight": 1,
            "text": name,
            "enabled": True}
        print(1)
        wheel['entries'].append(new_entry)
    return


def set_entry_color(wheel: dict, name: str, color: str) -> bool:
    logging.info(f"Setting Color for {name} to {color}")
    i = 0
    for entry in wheel['entries']:
        if entry['text'] == name:
            if wheel['entries'][i]['color'] == color:
                logging.info("Color already set")
                return False
            wheel['entries'][i]['color'] = color
            return True
        i += 1

    return False


def clear_entries(wheel: dict):
    for entry in wheel['entries']:
        entry['weight'] = 0
        entry['enabled'] = False


def run():
    args = build_args()
    if args.test:
        logging.info("---Test Run---")
    else:
        logging.info("---Running---")
    args_to_log = vars(args).copy()
    args_to_log['key'] = 'REDACTED'
    logging.info(args_to_log)

    if args.private or args.shared:
        run_wheel(args)
    else:  # This should never happen
        logging.error("Neither private nor shared option is set")
        logging.error('---Exiting---')
    logging.shutdown()


def run_wheel(args):
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
    if args.private:
        wheel_data = WheelOfNames.get_private_wheels(args.key[0])
    elif args.shared:
        wheel_data = WheelOfNames.get_shared_wheels(args.key[0])
    else:  # This should never happen
        logging.error("Neither private nor shared option is set")
        logging.error('---Exiting---')
        return

    if 'error' in wheel_data.keys():
        logging.error('Invalid API key')
        logging.error(wheel_data['error'])
        logging.error('---Exiting---')
        return

    wheel = get_wheel_by_name_or_path(wheel_data['data']['wheels'], args.wheel[0])
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
        clear_entries(wheel)
        upload = True

    if upload:
        logging.info("Uploading Wheel")
        if args.shared:
            logging.info(WheelOfNames.send_shared_wheel(
                args.key[0], args.wheel[0], {'wheelConfig': wheel}
            ))
        elif args.private:
            logging.info(WheelOfNames.send_private_wheel(
                args.key[0], {'config': wheel}
            ))


run()
