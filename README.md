# SEKAI CTF Writeups
|   |   |
|---|---|
| Date: | Fri, 25 Aug. 2023, 16:00 UTC — Sun, 27 Aug. 2023, 16:00 UTC  |
| Event Details: | https://ctftime.org/event/1923/ |

Because this was geared toward more intermediate players, I focused on the one ⭐ (least difficult) challenges.

## Azusawa’s Gacha World
|   |   |
|---|---|
| Category: | Reverse  |
| Tools used: | [ILSpy](https://github.com/icsharpcode/ILSpy/) & [AssetStudioGUI](https://github.com/Perfare/AssetStudio/) 

## Problem Statement

We are given a [dist.zip](https://storage.googleapis.com/sekaictf-2023/azusawa/dist.zip) file to download.

## Initial Discovery
The first thing to note is that it's a Unity game. 

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/b689bfd1-48e7-4102-87f5-579014e0767a)

We can even run the game and check it out.
![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/4fbe0a93-dbab-4353-b8ef-e88140d8d40e)

## Decompiling the game

I used [ILSpy](https://github.com/icsharpcode/ILSpy/) to decompile the game.

By default, Unity compiles all scripts together into a single file named `Assembly-CSharp.dll`. Open this file in ILSpy so it can decompile it back into C#:

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/31cdfd67-0620-4bb1-953a-cc5b7e8300b5)

## Inspecting the code
Navigating to the `-` namespace and reading the source code, we see a variable named `flagimage` inside the `UIManager`. That sounds promising!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/9a69053c-3a6d-4d70-9784-b821b9c1b684)

Looking at the code further, there is a `DisplayFourStarCharacter` method, which loads a `Texture2D` image:

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/b1c1a647-ca93-4291-9e7a-9a5c04bd061d)

At this point, I think I'm going to have to do more shenanigans and understanding the code to get the flag, but decided to checkout the assets first.

## Extracting the assets
I used [AssetStudioGUI](https://github.com/Perfare/AssetStudio/) for this. This repo is deprecated so there are probably other tools out there. Simply loaded the folder in AssetStudioGUI (hint: turn off `Debug -> Show Error Messages`) and waited. Once it had extracted the assets, I exported them all to search outside the AssetStudioGUI UI.

## Finding the flag
Looking in the `Texture2D` folder there is a picture called `flag.png` and sure enough it has a flag fitting our format. At this point, I was still sure it would be a red herring, but submitted it and it was correct!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/d624505a-77c5-415b-b9ca-bce0b4551a97)

## The flag

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/4c4f1f38-6e97-4065-ba73-8d99ee2b4d4c)

## I Love This World
|   |   |
|---|---|
| Category: | Misc  |
| Tools used: | python scripting (optional) |

## Problem Statement

We are given an [SVG file](https://ctf.sekai.team/files/d7ced45e98c0db6d2423ebd85f2a7a2e/ilovethisworld.svp?token=eyJ1c2VyX2lkIjoxMDQsInRlYW1faWQiOjU5LCJmaWxlX2lkIjoyMH0.ZO0g4w.MDAuLn5HJot8BDRh-7SKVQA0HRE) to download with this description:

> Vocaloid is a great software to get your computer sing the flag out to you, but what if you can’t afford it? No worries, there are plenty of other free tools you can use. How about — let’s say — this one?

## Initial Discovery

The file is an SVP file. Googling `svp file` one of the 1st results that gomes up in the search has the snippet:

> An SVP file is a Dreamtronics Synthesizer V project. It contains JSON-formatted text used to load a voice synthesizer project in Synthesizer V. 

Ooh, JSON.

Opening the file (I used VSCode with a json-prettifier extension), we see it looks really readable, so lets drill into it further!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/0d6c4111-f72b-45b9-a80b-44a41aac1004)

## Rabbit Hole
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

## Solution is in the phonemes
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

## The flag
`sekai{some1zfarawaytmr15sequeltoourdreamtdy}`
