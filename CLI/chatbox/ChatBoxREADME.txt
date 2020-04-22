Note:Doctor ID is to be used as it is.
User ID should be used as USER ID + 1000
eg. userID 1 should input user no.= 1000+1=1001

INPUT FORMAT

For Individual message:
<user no. of the recipient><space><message>

For Group message:
0<space><message>


EXPECTED OUTPUT

For Individual message:
“Received from <user no>:<message>”

For Group message:
“Received in group chat from <user no>:<message>”


ERROR HANDLED AND ERROR 
Invalid User No.

•	User no. should be between 1 and 2000.
•	User no. should be a integer value.

Duplicate users
•	There should not exist a user with same user no. already.

Invalid recipient
•	Recipient no. should be between 0 and 2000.
•	User no. should be a integer value.
•	There should exist a user with that user no. already.
