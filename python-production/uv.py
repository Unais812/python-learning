# virtual env is seperate private toolbox of python packages for one project
# uv creates environments and installs packages also manages list of dependencies required for project

# create a new project folder with uv
# uv init my-project
# cd my-project

# Every serious Python project uses a virtual environment. 
# When you clone a data pipeline, a model training repo,
# or an AI application, the first thing you do is create its environment and install its packages.
# The lock file guarantees your setup matches everyone else's and matches production. 
# This is the foundation of reproducibility, which is central to all of MLOps. 
# Getting comfortable with uv now pays off in every project after.