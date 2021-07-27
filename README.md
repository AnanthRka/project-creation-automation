This is to automate the first few steps of project creation and Version Control using GitHub.

The pre-conditions are
1. Store the create.bat file in "C:\Windows\System32\" directory or add the PATH of the folder containing this file in the Environment Variables.
2. Edit the create.bat file to specify the path to the python file "automate.py" and the project directory.

You can simply run the command "create test-project", without quotes, in the terminal from any directory to start the program. This will create a folder "test-project" in the mentioned projects directory, open GitHub and create a repo with the same name.
Additionally a simple README.md file is also created.

For best results keep project names to minimal and try to use hyphens and underscores than spaces while naming it.