# Best Practices

Programming **is not just writing code** but there is also a huge world around it.

## Must do

### Reproducibility

#### Log versions and library versions.

Manage all the dependencies can be an hell if not done right.
Using virtual environments like `venv` or `UV` or `conda` can help you manage all the dependencies and help with code reproducibility.

#### Use Version Control and collaborations

With version control (`git`) you can roll back to a previous stable version if your code. It is good practice to always use version control even in solo projects.
Also using `GitHub` or `GitLab` you can share your project and collaborate with others.

#### Configuration files

Use one of the following: `.json`, `.yaml`, `.toml` to make configuration files, containing the standard values of settings variables.

### Documentation

Well-documented code is essential for reproducibility and collaboration.
Add docstrings to functions and classes, with clear and coincise explanations, also consider adding code examples.

#### README

Write a `README.md` (the `.md` extension is not obligatory, but it's the most common) file containing important information about the project like: 
purpose, how to install and use, 

### Error handling

The title is self-explanatory, you don't want to trow an error in your user face if they don't know your code base or, worse, if they don't even know how to program.
So you should make sure your code properly handles all errors.

#### Validate inputs

When you have to get an input validate as soon as possible if that input is correct.
**Do not trust the user!** not even if the user is yourself. 

#### Provide helpful error messages

When an input is not correct you have to make the user understand why the input is not working properly, 
so write a short but complete error message containing all the information he needs to correct the input.

## Should do

### Project Structure

Big projects usually have a well-defined file structure, and it's decided based on preferences, but when you are not given a project structure you should follow the following structure:

```shell
project_name/
├── README.md
├── LICENSE
├── pyproject.toml            # Or requirements.txt + setup.py
├── Makefile                  # Optional: common tasks (run, clean, lint, etc.)
├── .gitignore                # List of ignored files and directories to NOT add on git
├── data/                     # Raw and processed data files (ignored if too large)
│   ├── raw/                  # Unmodified data
│   └── processed/            # Cleaned and transformed data
├── notebooks/                # Jupyter notebooks for exploration, figures, etc.
│   └── analysis.ipynb
├── docs/                     # Documentation (Markdown or Sphinx)
│   ├── index.md / index.rst
│   └── api/
├── project_name/             # Main package directory (same name as project or "src")
│   ├── __init__.py
│   ├── config.py             # Global config and parameters
│   ├── main.py               # CLI entrypoint or main script
│   ├── core/                 # Core algorithms / numerical solvers
│   │   ├── __init__.py
│   │   └── solver.py
│   ├── examples/             # Optional: Code examples
│   │   └── simple_example.py
│   └── utils/                # Utility functions (I/O, plotting, etc.)
│       ├── __init__.py
│       ├── io.py
│       └── plotting.py
├── tests/                    # Unit and integration tests
│   ├── __init__.py
│   ├── test_solver.py
│   └── test_io.py
├── logs/                     # Logging output (can be added to .gitignore)
│   └── run_2025_06_18.log
├── results/                  # Plots, figures, output data, etc.
│   ├── figs/
│   └── tables/
└── scripts/                  # Bash or Python scripts for automation
    ├── run_simulation.py
    └── clean_output.sh
```

A structure similar to this makes the project scalable.

### Logging

Use a logging module instead of printing everything to the console, also save the log files so you can check what went wrong.

### Make tests

Write test using `pytest` or `unittest` and validate them with analytical results. This makes sures your code does not have an unexpected behaviour. 

Note is best practice to test edge cases and stress conditions. 

You can also use **CI pipelines** to run automated tests.

### Code Quality

Write quality code by following the rules:

 - Follow PEP8, to help with that you can use linters or formatters like `ruff` and `black`.
 - Use typehints and then do type checks with `mypy` or other tools.
 - Write modular code, with each function has a single aim. (This advice is to take with caution because not always writing modular code is the best choice, sometimes you don't want to write too many functions, it is up to you to choose which approach is better each time)

### Other Tools

#### Jupiter Notebooks

Use Jupiter Notebooks to write and test fast code, then when you asserted the correctness of the code you can go back to a python script (you can create a `.py` file from a notebook).

#### Profilers

If performance is important use profilers to understand what function calls take the majority of time and should be optimized.

#### Makefiles automations

Use makefiles or other scripts (like shell scripting or even other python scripts) to make automations like: downloading data, cleaning the project, resetting settings, updating the project, ecc..

### Outputs

#### Save outputs as standard formats

If you don't have a specific constrain on your data output follow these rules:

 - Use `.txt` or `.md` for texts.
 - Use `.dat`, `.csv` or `.npy` for data tables.
 - Use `.jpg`, `.png` or `.svg` for images.
 - Use `.mp4` or `.gif` for videos and animations.

#### Add metadata to outputs

### Use Checkpoints

For long simulations you should save your state to disk at time intervals (or when a certain condition occurs) like every hour.
So if the program fails, after reading the logs to check when the error started, you can resume your program saving computational time.

### Changelog

Maintain a changelog with updates for each version.

### Write short usage manuals or API references

If your program has to be used by other people consider writing a detailed reference to your code.
