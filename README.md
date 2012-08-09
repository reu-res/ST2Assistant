#Sublime Text 2 Assistant

This script allows you to get a little more information about the state of Sublime Text 2, you can use when writing their own plugins.

##Installation
You can copy `ST2Assistant.py` to directory when installed Sublime Text 2, or to **User** package directory.

The **User** package directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/User

* Linux:

        ~/.config/sublime-text-2/Packages/User

* Windows:

        %APPDATA%/Sublime Text 2/Packages/User

    If you use portable version:

        <Sublime Text 2 directory>/Data/Packages/User

##Usage
    import ST2Assistant
    ...
    assistant = ST2Assistant.assistant()
    if assistant.is_side_bar_visible():
        print 'Side bar is visible'
    else:
        print 'Side bar is hidden'

##Functions
[List of functions](wiki/Functions)