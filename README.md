# Discord Token Checker
This script is used to check the validity of Discord tokens by sending a GET request to the Discord API. It also checks if the token is verified or not. It requires the `requests` library to be installed, which can be installed by running `pip install requests` in your command line.
And also saves usernames of each tokens on a `usernames.txt` read more below.

# Usage
1. Create a file called `tokens.txt` in the same directory as the script.
2. Add your tokens to the `tokens.txt` file, with each token on a new line.
3. Run the script by executing `python <scriptname.py>` in your command line.
4. The script will check each token and print whether it is valid, verified, or invalid.
5. The script will ask if you want to save the valid and invalid tokens to separate files, `valid_tokens.txt` and `dead_tokens.txt`, respectively. If the token is verified then it will save in `verified_tokens.txt`.
6. The script also saves the usernames of each tokens on a `usernames.txt` file in the same redirectory.

# Output
- Green color means the token is valid
- Red color means the token is invalid
- Yellow color means the script is asking for user input
-  This script uses the `colorama` library to print the output in different colors, and the `os` library to clear the console.

# Additional functionality
Script will fetch the username associated with the token.

# Known Issues
- This script is platform dependent and may not work as expected on non-Windows systems.
- If runned on a local machine, wait till the script closes itself for it to be completed, usernames might take a while to save depending on how many tokens you're checking.

# Note:
This script is for demonstration purpose and should not be used for any illegal activities. Also, it is best practice to not store plaintext password.
