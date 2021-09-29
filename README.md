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