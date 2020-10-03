## Yuki-Generator-C-Project V1

Hi! :smile:

This project is to generate a **C project architecture**, like:
1. include directory
   * include file
2. library directory
   * file of library
   * Makefile of library
3. src directory for your file
4. Main file
5. Makefile

So the generator can actively generate your library, makefile and include, following of project and your wishes! :wink:

The advantage of this generator is that you can easily make an optimized library. And which follow your necessity! :fire:

## How to start

# Launch

For launching the process you need to execute the command:
```
./Init-Project
```

# Config :hamster:
In Data folder you have config.json where you can active or desactive option.
> 1 = activate
> 0 = desactivate

# Makefile :koala:
In Data folder you have 2 Makefile:
* Makefile -> Makefile for the project
* Makefile_lib -> Makefile for the library

You can change this if you want **BUT** don't touch to lines between comments.
:exclamation: They are modified, deleted or filled during the generation!

# Include :mouse:
In Data folder you have Include.h where you can add functions declarations and others includes.

# Library :fish:
You can add all files of your complete lib inside the folder Data/lib/
