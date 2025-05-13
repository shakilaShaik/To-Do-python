Setup for Flask Application:

1.  `mkdir backend` --> cd backend - Creating Floder
2.  ` python -m venv venv` -- To generate the virtual Environment where all the modules stored and used in the application. This will rectify the problem being adding of the dependencies to the global which cause conflicts.
3.  `source venv/bin/activate ` -- It will activate the virtual Environment located in the venv directory. It refers the virtual environment rather than the pointing to global modules. 4.`pip install flask flask-cors python-dotenv` -- This install all the modules defined from the python package manager pip.
4.  ` pip freeze > requirements.txt` -- It saves the packages being used in our application for future use like cloning and setup this project on new system.
