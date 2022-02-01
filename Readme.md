Install all the modules using requirements.cmd
--------------------------------------------------------------------------------------------------------------------------------------------

Window 1(Password Generator):

1)Enter length of password.
2)Enter 'Y' for including special characters, 'N' for no
3)Enter the website where you are going to use the password.
4)Click Generate button.
5)A QR Code will also be generated in case you need to send the details to your phone.
6)The password will be copied to the clipboard and can be used wherever needed.(COPIED message will be displayed).
	NOTE: i)If Generate button is clicked with the first entry empty a message will be shown(length of password must be atleast 4),
	        if any other entry is empty, it would not display any message and the password will not be generated).
	      ii)"Passwords.bin" file will be automatically created, if such file is already found, all the generated passwords will
		  appended in that file.
	      iii)Length of the password should be atlest 4, or else no password will be generated.

--------------------------------------------------------------------------------------------------------------------------------------------

If using the code for te 1st time:
    When "Show Passwords" button is clicked a new window(Sign Up) will pop up asking to enter password which will be encrypted and saved.

-------------------------------------------------------------------------------------------------------------------------------------------

When the button is clicked again a window(Log In) will pop up asking for the password.The password entered in the 'Sign Up' window should
be entered to view the passwords.

-------------------------------------------------------------------------------------------------------------------------------------------

Forgot Password?
Locate the files 'key.key' and 'password_file.key' (can be found in the same path where the code is located), select these two file and 
delete them, the next time you click "Show Passwords" the "Sign Up" window will pop up and new password can be entered.

-------------------------------------------------------------------------------------------------------------------------------------------
Show Passwords button clicked
Window 2(Passwords):

	NOTE: Always close the window and reopen it to refresh the records.

Update:
	1)Select the record you need to update.
	2)Click Update button.
	3)Details will be displayed, change the password and website, time will be automatically updated.
	4)Close the window.

Delete:
	1)Select the record you need to delete.
	2)Click Delete button.
	3)Close the window.

Delete All:
	1)Double click on the Delete All button, all the records will be deleted.
	2)"Deleted Successfully" message will be displayed.
	3)Close the window.

Search:
	1)Click on Search button.
	2)Enter the password or website to search, click search button, all the matching record(s) will be highlighted(if highlighted
	  record(s) are not displayed scroll manually and you will find the highlighted record(s) this is because auto scroll to the
	  highlighted record is not implemented).
	NOTE: Recently updated records can't be searched without closing the window and reopening it, to do so close the window and 
	      search again.

Features:
	1)Double click any record, the respective password will be copied to the clipboard and also a QR Code will be generated.
	2)Triple click any record, the respective website will be opened in your default web-browser.

--------------------------------------------------------------------------------------------------------------------------------------------

Errors:
	#If the file "Passwords.bin" is not found, and in that case Show Passwords button is clicked a window opens displaying the 
	 message "File Not Found" and closes automatically.
	#Don't change the path of "Passwords.bin" file.

-------------------------------------------------------------------------------------------------------------------------------------------