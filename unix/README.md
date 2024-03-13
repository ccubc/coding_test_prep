Source of the notes: The Unix Workbench, The missing semester in CS education by MIT

### Useful terminal commands:
* `ls`: list files and directories; `ls -l`: long list (more detailed information); `ls -a`: list all files including hidden files
* `mkdir`: create a new directory
* `cd`: change directories
* `cd -`: go to your previous directory
* `rm`: remove files and directories
* `pwd`: print working directory
* `history`: print command history



### About directory:
* `/`: root directory, e.g. use `cd /` to change to root directory
* `~`: home directory, to cd to home directory: use any one of (1) `cd ` (2) `cd ~` (3) `cd /Users/username`

### Creation and Inspection
* `touch journal-2020-03-14.txt`: create a new file in the current directory
* `wc todo.txt`: word count command, # lines, # words, # characters
* `ls -1 | wc -l`: count number of files in current directory (-1("one") means only one entry per line, "|" means to pipe output onto, -l means to count lines)
* `cat todo.txt todo.txt`: concatenate files and print them to terminal
* `cat part1.txt part2.txt > all.txt`: concatenate files to a new file
* `less Documents/a-tale-of-two-cities.txt`: print a preview of multi-page files (print the first several lines)
* `head document.txt`: print the head of the document
* `tail document.txt`: print the tail of the document
* `grep "San" cities.txt`: search str in the text (will print the strings that contain "San")
* `echo "I'm in the file." > echo-output.txt`: use `>` for **output redirection**
* `echo "I have been appended." >> echo-output.txt`: use `>>` to **append** text to the end of a file.
* nano is a simple text editor in terminal.


### Migration and Destruction: moving, renaming, copying, deleting files and folders
* `mv journal-2020-03-14.txt ~/Journal`: move the file journal-2020-03-14.txt to the Journal folder
* `mv Journal ~/Documents`: move the Journal folder to Documents folder
* `mv todo.txt todo-2020-03-14.txt`: use mv to rename file and folders
* `cp echo-out.txt ~/Desktop`: copy a file from one location to another
* `cp -r Documents ~/Desktop`: copy a file folder, r means recursive, every underlying directory structure will be copied
* `rm echo-out.txt`: remove file, i.e. permanently delete, not recommended (no way to undo)
* `rmdir data`: remove data folder (if it's empty)
* `rm -r data`: remove recursively for the data folder (remove the entire folder and its contents)


### Help
* `man ls` will take you to the help documentation of the command `ls`
* While in `man`, use `\` to search for words, e.g. `\page`
* `apropos editor`: search for all available commands with description including editor. Use this when you don't know which command to use.


### Use wildcard
* `ls 2019*`: list all files starting with '2019'
* `ls 2019*.jpg`: list all jpg files starting with '2019'
* `mv 2019*.jpg 2019/`: move all jpg files starting with 2019 to folder 2019


### Regex

* `egrep "i.g" cities.txt`: search str in the text that contains "i+some char+ g"
* `egrep "s+as" cities.txt`: search for one or more "s" followed by "as"
* `egrep "\w" small.txt`: all word characters ( eng + number)
* `egrep "\d" small.txt`: all number characters
* `egrep "\s" small.txt`: all space characters
* There are also other use cases for using Regex to search for str.


### Find
* `find . -name "states.txt"`: look for a file called states.txt (within the dir or sub dir of current dir)
* `find . -name "*.jpg"`: look for all jpg inside this dir
* You don't need it since you use Spotlight ^O^


### Difference
* `diff result_v1.txt result_v2.txt`: will print out the difference between two files
* `sdiff result_v1.txt result_v2.txt`: will print the differing lines in a side-by-side comparison
* `diff result_v1.txt result_v2.txt > diff_res.txt`: save the difference to diff_res.txt









