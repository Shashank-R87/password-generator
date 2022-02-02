# Password Generator

### Install all the modules using requirements.cmd
--------------------------------------------------------------------------------------------------------------------------------------------

Window 1(Password Generator):<br><br>

1. Enter length of password.<br>
2. Enter 'Y' for including special characters, 'N' for no<br>
3. Enter the website where you are going to use the password.<br>
4. Click Generate button.<br>
5. A QR Code will also be generated in case you need to send the details to your phone.<br>
6. The password will be copied to the clipboard and can be used wherever needed.(COPIED message will be displayed).<br><br>

	NOTE: If Generate button is clicked with the first entry empty a message will be shown(length of password must be atleast 4),
	      if any other entry is empty, it would not display any message and the password will not be generated).
	      ii)"Passwords.bin" file will be automatically created, if such file is already found, all the generated passwords will
		  appended in that file.
	      iii)Length of the password should be atlest 4, or else no password will be generated.
<br>

--------------------------------------------------------------------------------------------------------------------------------------------

Using the code for the 1st time?<br>
    When "Show Passwords" button is clicked a new window(Sign Up) will pop up asking to enter password which will be encrypted and saved.<br>

-------------------------------------------------------------------------------------------------------------------------------------------

When the button is clicked again a window(Log In) will pop up asking for the password.The password entered in the 'Sign Up' window should
be entered to view the passwords.

-------------------------------------------------------------------------------------------------------------------------------------------

Forgot Password?<br>
Locate the files 'key.key' and 'password_file.key' (can be found in the same path where the code is located), select these two file and 
delete them, the next time you click "Show Passwords" the "Sign Up" window will pop up and new password can be entered.<br>

-------------------------------------------------------------------------------------------------------------------------------------------
Show Passwords button clicked<br>
Window 2(Passwords):<br>

	NOTE: Always close the window and reopen it to refresh the records.
<br>
Update:<br>
	1)Select the record you need to update.<br>
	2)Click Update button.<br>
	3)Details will be displayed, change the password and website, time will be automatically updated.<br>
	4)Close the window.<br>
<br>
Delete:<br>
	1)Select the record you need to delete.<br>
	2)Click Delete button.<br>
	3)Close the window.<br>
<br>
Delete All:<br>
	1)Double click on the Delete All button, all the records will be deleted.<br>
	2)"Deleted Successfully" message will be displayed.<br>
	3)Close the window.<br>
<br>
Search:<br>
	1)Click on Search button.<br>
	2)Enter the password or website to search, click search button, all the matching record(s) will be highlighted(if highlighted
	  record(s) are not displayed scroll manually and you will find the highlighted record(s) this is because auto scroll to the
	  highlighted record is not implemented).<br>
	NOTE: Recently updated records can't be searched without closing the window and reopening it, to do so close the window and 
	      search again.<br>
<br>
Features:<br>
	1)Double click any record, the respective password will be copied to the clipboard and also a QR Code will be generated.<br>
	2)Triple click any record, the respective website will be opened in your default web-browser.<br>

--------------------------------------------------------------------------------------------------------------------------------------------
<br>
Errors:
	#If the file "Passwords.bin" is not found, and in that case Show Passwords button is clicked a window opens displaying the 
	 message "File Not Found" and closes automatically.<br>
	#Don't change the path of "Passwords.bin" file.<br>

-------------------------------------------------------------------------------------------------------------------------------------------
