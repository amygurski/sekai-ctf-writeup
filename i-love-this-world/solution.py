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
