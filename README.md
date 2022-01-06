# GOACS2 Python Modules and Packages

First, try installing the PyGame Zero package, which we will be using to create some animations in this course module.

## PYTHON MODULES

In this assignment, you will import a **Python package** called `pygamezero` to help you run some sample code.  
Then, you will write some short programs that show your ability to use code that has been imported from simpler modules.

Instructions for importing packages are below. The most important steps are <ins>underlined</ins>.


> ### WINDOWS
> 1. <ins>Open the Terminal</ins>
>     * At the top of the VSCode window, you'll see the Terminal menu in the menu bar. 
Choose `New Terminal` from the menu, or use the shortcut `Ctrl` + `Shift` + \`
> 2. Create a virtual environment
>     * <ins>In the Terminal, type `Python -m venv venv`</ins>
>         * This creates a new folder called `venv`
>         * The purpose of this folder is to have only the Python modules we need in our program.
>         * Select "Yes" if VS Code asks if you want to select this as the environment folder.
> 3. Activate the virtual environment
>     * <ins>In the Terminal, type `Set-ExecutionPolicy -ExecutionPolicy remoteSigned -Scope Process`</ins>
>         * This gives our program permission to install modules in the virtual environment
>     * <ins>In the Terminal, type `.\venv\Scripts\activate`
>         * You'll see that the Terminal prompt changes to include `(venv)` at the beginning of the prompt. That's how you know you're in the right environment.
> 4. Install the required package(s)
>     * <ins>In the Terminal, type `pip install pgzero`</ins>
>     * Bokeh is the package used for this visualization
>     * IF THIS DOESN'T WORK - please try upgrading pip using the following command: `pip install --upgrade pip` and try `pip install pgzero` again.
> 5. Run the program
>     * Select the `pygamesample.py` file in the explorer
>         * If you don't see the file list, click on the icon on the top left of the window
>     * Click the play button on the top right of the window


> ### MACOS
> 1. <ins>Open the Terminal</ins>
>     * In the menu bar at the top of your screen, you'should see the Terminal menu. Choose `New Terminal` from the menu, or use the shortcut `Ctrl` + `Shift` + \`
> 2. Create a virtual environment
>     * <ins>In the Terminal, type `python3 -m venv venv`</ins>
>         * This creates a new folder called `venv`
>         * The purpose of this folder is to have only the Python modules we need in our program.
>         * Select "Yes" if VS Code asks if you want to select this as the environment folder.
> 3. Activate the virtual environment
>     * <ins>In the Terminal, type `source venv/bin/activate`
>         * You'll see that the Terminal prompt changes to include `(venv)` at the beginning of the prompt. That's how you know you're in the right environment.
> 4. Install the required package(s)
>     * <ins>In the Terminal, type `pip install pgzero`</ins>
>     * This installs the PyGame Zero package that we'll be using this module.
>     * IF THIS DOESN'T WORK - please try upgrading pip using the following command: `pip install --upgrade pip` and try `pip install pgzero` again.
> 5. Choose your Interpreter
>     * At the bottom of VS Code is a version of Python. Please be sure that it says 'venv' after the version number.
>     * If it doesn't, click on the Python version and choose the one that includes 'venv'. This is your virtual environment.
> 6. Run the program
>     * Select the `pygamesample.py` file in the explorer
>         * If you don't see the file list, click on the icon on the top left of the window
>     * Click the play button on the top right of the window
