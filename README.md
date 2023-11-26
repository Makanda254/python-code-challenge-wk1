# python-code-challenge-wk1

# Description
This project has three files;

1. A convert_time.py file within which has a function that converts 12-hour time like "8:30 am" or "8:30 pm" to  24-hour time (like "0830" or "2030"). The hour is always in the range of 1 to 12, a minute is always in the range of 0 to 59 and a period takes either "am" or "pm" as input. 

2. A positive_numbers.py file which has a function takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.
```
   Example:
   (2, 4, -3) == True, 
   (-4, 6, 8) == True
   (4, -6, 9) == True
   (-4, 6, 0) == False
   (4, 6, 10) == False
   (-14, -3, -4) == False
```

3. A consonant_value.py file that defines a function in which given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
```
   Example:
   For the word "zodiacs", solve("zodiacs") = 26

     For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

     -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22.    
        The highest is 26.

   For the word "strength", solve("strength") = 57.

     The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 
     8 = 49. The highest is 57.

```

# Set Up/ Installation 
- Clone the repository or download the source code.
- Make sure you have python or python3 installed on your system.
- Open the cloned folder with vscode.
- Run the program by executing the following command: python3 lib/name_of_the_file i.e python3 lib/convert_time.py

**Ensure your internet connection is stable to facilitate the download of the source code**

## Known Bugs
The application works well.

## Technologies used
- Terminal
- Python

## License
MIT License

Copyright (c) 2023 Makanda254

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgement
This project was done to establish my personal progress in grasping content related to the fundamentals of python programming namely: data types, python shell, functions,conditionals and loops.

## Support and contact details
- email :: victormakanda254@gmail.com
- phone :: +254768918629