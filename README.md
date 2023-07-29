# simple-python-application
Step 1: Open your terminal application.

Step 2: Type the following command and press Enter to install Python 3 and pip:


sudo apt install python3 python3-pip


Step 3: After the installation is complete, create a virtual environment for your project by running the following command:


python3 -m venv venv


Step 4: Activate the virtual environment by running the following command:


source venv/bin/activate


Step 5: Install Flask by running the following command:


pip install flask


Step 6: Now, create a Flask application file. You can use any text editor for this.

Step 7: Copy the code from pyhton.py into your Flask application file:


Step 8: Save the file and go back to your terminal.

Step 9: To run the Flask application in the background using `nohup`, use the following command:


nohup python3 your_file_name.py &


Replace "your_file_name.py" with the actual name of your Flask application file.

Step 10: The Flask application will now be running in the background. You can close the terminal and the application will continue to run.

Step 11: To access the Flask application, open your web browser and enter the following URL: `http://localhost:3000`. You should see the message "Hello, world!" displayed on the page.

Step 12: To stop the Flask application that is running in the background, you can use the `kill` command. First, find the process ID (PID) of the Flask application by running the following command:


ps aux | grep your_file_name.py


Replace "your_file_name.py" with the actual name of your Flask application file. Look for the process ID (PID) in the output.

Step 13: Once you have the process ID (PID), use the following command to stop the Flask application:


kill PID


Replace "PID" with the actual process ID of the Flask application.

That's it! You have successfully installed Python, created a Flask application, and used `nohup` to run the application in the background. 








To leave the virtual environment (venv) on Linux, you can use the following command:


deactivate


Simply type `deactivate` in the terminal and press Enter. This command will deactivate the currently active virtual environment and return you to the system's default Python environment. You will no longer be inside the venv.

After running `deactivate`, you can confirm that you have exited the virtual environment by checking if the virtual environment's name (e.g., `(venv)`) is no longer displayed at the beginning of the command prompt.

