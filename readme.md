# Wheel of Streams

Wheel of Streams is a program created to assist with automating www.wheelofnames.com

## Setup
How to setup
1. 
2. 

## Arguments
`-key KEY -wheel NAMEOFWHEEL (-add NAME | -color NAME COLOR | -clear)`

The following arguments MUST used with the Wheel of Streams:
### -key API_KEY
Your WheelOfNames API Key.

### -wheel NAME
The name of the wheel you wish to edit.

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
`-key put-key-here -wheel Wheel -add Vanifac`

`-key put-key-here -wheel wheeloffortune -color lemonguy yellow`

`-key put-key-here -wheel RiggedRaffleWheel -color brian #1f6a78`

`-key put-key-here -wheel Wheel2 -clear`
