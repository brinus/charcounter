# charcounter
Given plain text as input, get detailed informations about chars frequency in the text. The file must be in plain text format (.txt), it can be placed in /test folder or called with its absolute path.

## Usage

To use properly the program give in input the text file you want to analize:

```
    python count.py file_name.txt
```

The program gives in output a dictionary containig the occurences of each char. For example, analyzing `animalfarm.txt` given in `\test` folder:

```
    {'a': 11213, 'b': 2329, 'c': 2856, 'd': 6345, 'e': 17399, 'f': 3078, 'g': 2810, 'h': 8655, 'i': 8202, 'j': 219, 'k': 993, 'l': 5926, 'm': 3705, 'n': 9543, 'o': 10034, 'p': 2219, 'q': 157, 'r': 7751, 's': 8058, 't': 12020, 'u': 3477, 'v': 1206, 'w': 3651, 'x': 278, 'y': 2207, 'z': 45}
```
## Optional functions
The program gives two optional arguments, one for plotting an histo of the relative frequency, one for printing some stats of the text.
A guide for seeing optional functions can be seen typing 

```
    python count.py -h
```
This returns:
```
    usage: count.py [-h] [-p [ORDERING]] [-s] file_name

positional arguments:
  file_name             The file to be analized must be in plain text format (.txt),
                        it can be placed in /test folder or called with its abso lute
                        path.

optional arguments:
  -h, --help            show this help message and exit
  -p [ORDERING], --plothist [ORDERING]
                        [ORDERING] = [alphabetic, decreasing] Enables histogram plot.
                        The user can specify if t he histogram bar must be ordered in
                        values-decreasing order or alphabetic-ke ys order. If nothing
                        is passed to -p/--plothist, the default choice is alpha betic
                        ordering.
  -s, --stats           Prints on terminal the stats of the text

```

