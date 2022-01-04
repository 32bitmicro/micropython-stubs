# micropython-stubs
<img src="docs/img/colorstubs.jpg"
     alt="pencil stubs"
     width=0%
     height=20%
     style="float: right; margin-right: 10px;" />

This repo stores stubs generated by the [MicroPython-Stubber](https://github.com/Josverl/micropython-stubber#readme) tool.
Currently over a 1.000 stubfiles of common MicroPython modules are available in this repo to help you : 
- write code quicker
- with less errors,
- get help from  code completion, 
- use static type checking 

and improve the overall development experience while writing MicroPython.

Demo using VSCode: 
![demo](docs/img/demo.gif)


## List of current firmwares and stubs 
The list of the current included firmwares, ports and boards includes stubs from the following micropython families: 
 - MicroPython
 - Pycopy
 - Loboris port (ESP32)

 - M5Stack
 - EV3 / Lego
 - LVGL

For a full overview of all stubs check out [the documentation on read the docs](https://micropython-stubs.readthedocs.io/en/latest/firmware_grp.html), or int the repo in  [docs/firmware_grp.md](docs/firmware_grp.md)

# Using the stubs 

To learn how to use the stubs please refer to [the documentaion on RTD](https://micropython-stubs.readthedocs.io/en/latest/02_using.html)

## Branch Main
The name of the default branch has been changed to `main`.
If you have cloned this repo before you main need to adjust the local repro to be aware of this, or create a fresh clone.

To update run the below command:  
``` bash
git branch -m master main                    
git fetch origin
git branch -u origin/main main                      
git remote set-head origin -a
```

for more info see [**Renaming a branch**](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch#updating-a-local-clone-after-a-branch-name-changes)

## Contributors
Thanks to everyone that has submitted stubs or other relevant pieces of code and information, or published relevant stubs on pypi or github.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Josverl"><img src="https://avatars2.githubusercontent.com/u/981654?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jos Verlinde</b></sub></a><br /><a href="https://github.com/Josverl/micropython-stubs/commits?author=josverl" title="Code">💻</a> <a href="#stubs-josverl" title="MicroPython stubs">📝</a> <a href="#test-josverl" title="Test">✔</a> <a href="#tool-josverl" title="Tools">🔧</a></td>
    <td align="center"><a href="https://micropython.org/"><img src="https://avatars1.githubusercontent.com/u/6298560?v=4?s=100" width="100px;" alt=""/><br /><sub><b>MicroPython</b></sub></a><br /><a href="#data-micropython" title="Data">🔣</a> <a href="#stubs-micropython" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="https://github.com/loboris"><img src="https://avatars3.githubusercontent.com/u/6280349?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Boris Lovosevic</b></sub></a><br /><a href="#data-loboris" title="Data">🔣</a> <a href="#stubs-loboris" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="https://github.com/pfalcon"><img src="https://avatars3.githubusercontent.com/u/500451?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Paul Sokolovsky</b></sub></a><br /><a href="#data-pfalcon" title="Data">🔣</a> <a href="#stubs-pfalcon" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="https://github.com/pycopy"><img src="https://avatars0.githubusercontent.com/u/67273174?v=4?s=100" width="100px;" alt=""/><br /><sub><b>pycopy</b></sub></a><br /><a href="#data-pycopy" title="Data">🔣</a> <a href="#stubs-pycopy" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="https://github.com/pycom"><img src="https://avatars2.githubusercontent.com/u/16415153?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Pycom</b></sub></a><br /><a href="#infra-pycom" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/BradenM"><img src="https://avatars1.githubusercontent.com/u/5913808?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Braden Mars</b></sub></a><br /><a href="#stubs-BradenM" title="MicroPython stubs">📝</a> <a href="#test-BradenM" title="Test">✔</a> <a href="#tool-BradenM" title="Tools">🔧</a> <a href="#platform-BradenM" title="Packaging/porting to new platform">📦</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/pfalcon"><img src="https://avatars3.githubusercontent.com/u/500451?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Paul Sokolovsky</b></sub></a><br /><a href="#stubs-pfalcon" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="https://github.com/dastultz"><img src="https://avatars3.githubusercontent.com/u/4334042?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Daryl Stultz</b></sub></a><br /><a href="#stubs-dastultz" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="http://patrickwalters.us/"><img src="https://avatars0.githubusercontent.com/u/4002194?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Patrick</b></sub></a><br /><a href="#test-askpatrickw" title="Test">✔</a> <a href="#stubs-askpatrickw" title="MicroPython stubs">📝</a></td>
    <td align="center"><a href="http://comingsoon.tm/"><img src="https://avatars0.githubusercontent.com/u/13251689?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Callum Jacob Hays</b></sub></a><br /><a href="#example-CallumJHays" title="Examples">💡</a> <a href="#research-CallumJHays" title="Research">🔬</a></td>
    <td align="center"><a href="https://github.com/RonaldHiemstra"><img src="https://avatars.githubusercontent.com/u/17012831?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ronald Hiemstra</b></sub></a><br /><a href="https://github.com/Josverl/micropython-stubs/commits?author=ronaldHiemstra" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/cpwood"><img src="https://avatars.githubusercontent.com/u/13966104?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chris Wood</b></sub></a><br /><a href="#stubs-cpwood" title="MicroPython stubs">📝</a> <a href="#tool-cpwood" title="Tools">🔧</a></td>
    <td align="center"><a href="https://github.com/thingslu"><img src="https://avatars.githubusercontent.com/u/34967785?v=4?s=100" width="100px;" alt=""/><br /><sub><b>thingslu</b></sub></a><br /><a href="#stubs-thingslu" title="MicroPython stubs">📝</a> <a href="#test-thingslu" title="Test">✔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/WerdoxDev"><img src="https://avatars.githubusercontent.com/u/32638453?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matin Tat</b></sub></a><br /><a href="#test-WerdoxDev" title="Test">✔</a></td>
    <td align="center"><a href="https://github.com/robertoetcheverryr"><img src="https://avatars.githubusercontent.com/u/63941860?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Roberto Jose Etcheverry Romero</b></sub></a><br /><a href="#test-robertoetcheverryr" title="Test">✔</a></td>
    <td align="center"><a href="https://github.com/jdsmith"><img src="https://avatars.githubusercontent.com/u/1379246?v=4?s=100" width="100px;" alt=""/><br /><sub><b>jdsmith</b></sub></a><br /><a href="#test-jdsmith" title="Test">✔</a></td>
    <td align="center"><a href="https://github.com/mrkeuz"><img src="https://avatars.githubusercontent.com/u/6247921?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mr Keuz</b></sub></a><br /><a href="#test-mrkeuz" title="Test">✔</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

I invite everyone that has generated stubs for a board or port not on the current list, or has another contribution, to submit the stubs via a pull request or by just zipping up your stubs and creating an issue. 

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. 
