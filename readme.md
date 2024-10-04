# Wheel of Streams

Wheel of Streams is a program created to assist with automating www.wheelofnames.com

## Setup

## Arguments
The following arguments MUST used with the Wheel of Streams:

### `-key API_KEY`

Your WheelOfNames API Key.

### `-wheel NAME`
The name of the wheel you wish to edit.

## Arguments
The following arguments can be used with the Wheel of Streams:


### `-add NAME`
Adds an entry with NAME to the wheel. If an entry of that name is already found, adds +1 weight to that entry.

### `-clear`
Sets all entries on the wheel to be disabled with a weight of 0.

### `-color VALUE`
Specify the color of the wheel. Acceptable values are either a color hex (eg. #a4c5b9) or a preset listed below.

- White - #FFFFFF
- Silver - #C0C0C0
- Gray - #808080
- Black - #000000
- Red - #FF0000
- Maroon - #800000
- Yellow - #FFFF00
- Olive - #808000
- Lime - #00FF00
- Green - #008000
- Aqua - #00FFFF
- Teal - #008080
- Blue - #0000FF
- Navy - #000080
- Fuchsia - #FF00FF
- Purple - #800080

Make sure to check the `WheelColors.py` file for the most up-to-date list of colors.
