# Sam's text adventure!

## What is this mysterious thing?

This is a game I made that I think I am gonna call Deepstone.
It's a text adventure I began working on as part of my final project for a intro to programming class I took.

## What does the player need?

The player will need a python interpreter that can run the file. I personally use and recommend Visual Studio Code.

https://code.visualstudio.com/

There's a link ^^^

Once that is downloaded, you will open the app and go to extensions and download "Python". Now open the downloaded .py file and click the "run" arrow at the top. If you quit the game or wish to restart, first quit the game, and type clear in the terminal to erase the history of messages. Enjoy!

## How?

A. Lot. Of. If. Then. Statements. Also a couple of lists.

## Timeline

From start until current time (Circa April 18th 2024 - now, April 29th 2024) will be very muddy as I lazily did not write any documentation as the project was going swimmingly well with little to no snags.

April 18th, 2024 - April 29th, 2024: Beginning of game created. Concept for Warl made, first bit of journey coded, created the first village and first three rows of houses with their "environments" and scenarios are coded. Fourth row currently in the making. Inventory system implemented, first few key items coded in. Obstacles list created, it's a mystery tool to help us later!

April 30th, 2024: Foundation for fourth of row of houses made.

## Some problems I ran into.

Python is not made to make video games. I discovered this quite quickly. It scopes out very fast, so the order at which things are implemented became key quickly. For instance, starting in line 282 is the scenario for row 2 house 2 of the First Village.

In row 2 house 2 there is a painting that if the room it is in is inspected, a new choice in the user input control will appear allowing the user to inspect the painting. The way I originally went about doing this was to set a counter called row_2_house_2_counter that started at 0, and if the user inspected the room, it added 1 to the counter (row_2_house_2_counter += 1), and then an if/elif/else statement would check if the counter was greater than 0. If so, a new dialogue would be printed that was the exact same as before, but with a new line added called "Inspect painting." Theoretically, this would work. But I soon found out that because the row_2_house_2_scenario function was defined inside the row_2_houses_scenario, that it could not identify the counter I had set that I assumed would be global.

Setting the counter inside the function didn't work, because every time you inspected the room, it would send you back to the dialogue function I made so that the user didn't only have one chance at input. But because of this, it kept resetting the counter to 0. It was no go.

I tried making a global list called row_2_house_2_obstacle that = []. If row_2_house_2_obstacle did not contain 'A', then the original dialogue would be shown. If the user chose to inspect the room, then 'A' would be added to row_2_house_2_obstacle using the append function. It could not find the list. I was infuriated, what I didn't understand is why the inventory list could still be registered as valid and global, yet when I made a list in the same level it could not be recognized here.

Here was the fix. I made two separate input functions for the same scenario. My method of having the player back to the same dialogue function until either something "happens", they move on, or quit is to just put the same function back into each if else statement representing user choice. So, if the player chose to inspect the room, instead of sending the player back to the first dialogue function, it would send it to the second one, completely identical except for the addition of a new option, to inspect the portrait. Success!

Besides that problem, I haven't really had any else that I've encountered yet. I have some things for later already coded in, but because I haven't coded the later parts they are found in I can't test if they are functional or not.

# What resources did I use to construct this mess?

Literally just this:

https://www.w3schools.com/python/python_ref_list.asp

That is a list of list/array methods in python. Absolute life saver.

# Updates will be added as updates are added!
