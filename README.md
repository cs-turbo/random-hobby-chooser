# Random Hobby Chooser
Random hobby chooser is a python script that allows your to randomize your hobbies

Don't know what to do for the day? Roll the dice and let it decide for you :)

## How to use
1. Download the script + folders (either by downloading the files as zip or cloning the repo )
2. Put your hobbies as text files within the hobbies folder
    - the file name will become the value of your "dice roll"
    - e.g. the file drawing.txt will become "Drawing"
3. Run the script 
4. There you go

## Technical
The hobby files within the hobbies folder are copied to the tmp folder

Every file within the tmp folder will be deleted after each roll - when the tmp folder is empty all files from the hobbies folder are copied again

That way you won't get duplicate rolls

## Can i contribute?
Sure! Feel free to fork the repo and create pull requests 

## License
[WTFPL 2.0](wtfpl.md)
