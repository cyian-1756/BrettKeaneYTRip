# BrettKeane YouTube Ripper
A Youtube dl script that will allow someone to constantly download Brett Keane videos.

# Installation
To use the batch file, you won't need to download anything. You can just run brettkeane.bat and the file will do the work. To use the python script, which allows you to loop to batch file to run every hour, you will need to install Python. I used ver 3.5.2. So make sure that you have a version that will be compatible with the code I use.

# What do it do?
The batch file downloads every video from Brett Keane's channel, BrettKeaneSuperstar. If the bat file is run again, it will only download videos that haven't already been downloaded. The downloads are given a 5Mbit speed limit but this can be changed in the bat file. To learn more about what Youtube dl does and how to get your bat file to do other things, [view the docs here](https://github.com/rg3/youtube-dl/blob/master/README.md#readme)

Running breatkeane.bat for the first time will download all of his channels videos into folders. These folders are named after the date the video(s) were uploaded. (YYYYMMDD)

The python script opens the batch file in a infinate loop. This allows you to leave the bot unattended and allow it to keep checking for new uploads after the inital download. There is a check that will stop you automatically looping until you say yes. This can be easilly removed if you cba with that.

# Why
Because why not? Also Brett Keane is famous for deleting videos that make him look like an idiot. So make sure you have all of his videos so you can mirror them immediately and then send that to The Drunken Peasants. Cause why not?
