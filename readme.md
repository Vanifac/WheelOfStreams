# Wheel of Streams

Wheel of Streams is a program created to assist with automating www.wheelofnames.com wheels.

## Setup
How to setup
1. 
2. 
3. USESHELLEXECUTE: False
4. Settings > General > Process Watcher Start/Auto Start

## Arguments
`-key KEY -wheel NAMEOFWHEEL (-shared | -private) (-add NAME | -color NAME COLOR | -clear)`

The following arguments MUST used with the Wheel of Streams:
### -key API_KEY
Your WheelOfNames API Key. This can be found at ##

### -wheel NAME
The name or path of the wheel you wish to edit.


### -shared / -private
Indicate whether the wheel is shared or private.


### Option Arguments
One of the following arguments must be included:

#### -add NAME
Adds an entry with NAME to the wheel. If an entry of that name already exists, adds +1 weight to that entry.

#### -clear
Sets all entries on the wheel to be disabled with a weight of 0.

#### -color NAME VALUE
NAME is the name of the entry you wish to set.

COLOR is the color you wish to set on the entry.
##### Color Values
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
### Examples
`-key API_KEY -shared -wheel xxx-xxx -add Vanifac`

`-key API_KEY -private -wheel wheeloffortune -color lemonguy yellow`

`-key API_KEY -private -wheel RiggedRaffleWheel -color brian #1f6a78`

`-key API_KEY -shared -wheel xxx-xxx -clear`
