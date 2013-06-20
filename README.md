Proposal
========

Every time when I start to write new python application I needed to do all this boring stuff for creating Makefile, deb packaging scripts, README, setup.py and so on. So I decided to write skeleton that I will just simple clone and focus on making stuff not the routine actions.

Idea gracefully taken as you can see from the angular-seed, Chaplin Boilerplate, Rails CLI and all that great CoC world.

This skeleton should be as simply as possible. I don't want to force you to choose some libraries over others. Just minimal application structure.

Usage
=====

Init
----

It's recommended to use simple [seeder](https://github.com/Kagami/seeder) utility because there are many places to replace `python_app_seed` string with your own project name and utility do it all for you.

Makefile
--------

Makefile used for most project operations because it dramatically simplify the things. Read about available commands in the final [README](https://github.com/Kagami/python_app_seed/blob/master/README.final.md) (README of your project; seeder automatically rename it to `README.md`).

Config
------

Deb package
-----------

License
=======

*(Applies to the skeleton only not to the final application! This is possible because it's just Public Domain and you can use it AS you wish.)*

```
python_app_seed - simple skeleton for the python applications

Written in 2013 by Kagami Hiiragi <kagami@genshiken.org>

To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
```
