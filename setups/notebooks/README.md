# Setup Gotchas
## Setup Python on Windows
- How to use `pip` >>> `python -m pip` so upgrading pip is `pyhton -m pip upgrade pip`
- How to use `easy_install` >>> like as mentioned above `python -m easy_install` but first you need to install `setuptools` via `pip install`.
- How to install `bpython` >>> `python -m pip install bpython` only this still isn't enough to work. you also need to install `_curses module` which is done by `pip install windows-curses`. finally hit the command `bpython-curses`
## Where is the global installing destination
- `C:\ProgramData\[Your Program Name]` so all users can use. If just you want to use it, then install `C:\Users\[Your User Name]\[Your Program Name]`
## How to use Pandas on Windows
- Install anaconda (not miniconda) and it snstalls all of dependancies such as, numpy, matplotlib as well as pandas.
## How to use Jupyter Notebook on windows
- **Install anaconda (and of course add the path)** then you can hit the command `jupyter notebook` on **Powershell or whatever**. the localhost will be running and redirect to local browser.
- The path should be added is below five paths if you still haven't added them.
- `C:\Users\[Your User Name]\Anaconda3`
- `C:\Users\[Your User Name]\Anaconda3\Library\mingw-w64\bin`
- `C:\Users\[Your User Name]\Anaconda3\Library\usr\bin`
- `C:\Users\[Your User Name]\Anaconda3\Library\bin`
- `C:\Users\[Your User Name]\Anaconda3\Scripts`

### How to use Julia on Jupyter Notebook on Windows.
- First insatll Julia from official [page](https://julialang.org/downloads/)
- Then open REPL and follow the following commands.
- `import Pkg` Hit the `]` to enter `package mode`(the collor of texts change from green to blue) 
- hit the `add IJulia` and `build IJulia`
- after these to exit package mode, type `back space or delete for mac`
- type `using IJulia` to precompile 
- type `notebook()` to open up Jupyter Notebook. idk why but this command begins to install `miniconda` although I did already install `anaconda`