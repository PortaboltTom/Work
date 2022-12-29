https://www.youtube.com/watch?v=Wuuiga0wKdQ
dit filmpje gekeken, als je exact de stappen volgt werkt het. Je maakt een venv aan in de root van je project. Dit doe je volgens mij elke keer als je een project begint. .
You can then use this file to install the same packages and versions in another environment by running the following command:

To freeze the packages installed in your Python environment and save the list to a file, you can use the pip freeze command. This command will list all of the packages and their versions that are currently installed in your environment, and you can redirect the output to a file using the > operator.

Here's an example of how to use the pip freeze command to save the package list to a file called requirements.txt:

Copy code
pip freeze > requirements.txt
This will create a new file called requirements.txt in the current directory and save the output of the pip freeze command to it. The file will contain a list of the packages and their versions, one per line, in the format package==version.

You can then use this file to install the same packages and versions in another environment by running the following command:

Copy code
pip install -r requirements.txt
This will install all of the packages listed in the requirements.txt file.