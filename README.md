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

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/be5e4afb-7249-414f-be85-ac1b3426b9b4)

At this point, I think I'm going to have to do more shenanigans to get the data set to the flag image, but decided to checkout the assets first.

## Extracting the assets
I used [AssetStudioGUI](https://github.com/Perfare/AssetStudio/) for this. This repo is deprecated so there are probably other tools out there. Simply loaded the folder in AssetStudioGUI (hint: turn off `Debug -> Show Error Messages`) and waited. Once it had extracted the assets, I exported them all to search outside the AssetStudioGUI UI.

## Finding the flag
Looking in the `Texture2D` folder there is a picture called `flag.png` and sure enough it has a flag fitting our format. At this point, I was still sure it would be a red herring, but submitted it and it was correct!

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/d624505a-77c5-415b-b9ca-bce0b4551a97)

## The flag

![image](https://github.com/amygurski/sekai-ctf-writeup/assets/49253356/4c4f1f38-6e97-4065-ba73-8d99ee2b4d4c)

## References
[https://www.kodeco.com/36285673-how-to-reverse-engineer-a-unity-game](https://www.kodeco.com/36285673-how-to-reverse-engineer-a-unity-game)


