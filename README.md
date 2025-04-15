## followers-check
check who you're mutuals with, who doesn't follow you back, and who you don't follow back on instagram!

### step 1: get your data
request your official data from instagram [here](https://www.instagram.com/download/request/)
- download or transfer information -> some of your information -> check the 'followers & following' box
- download to device
- date range: all time
- format: either html or json. remember which one when running the script!

now, wait for your data to download. you will be notified through email when it's ready.

### step 2: clone the repository
git clone https://github.com/iriszhou-iyz/followers-check.git

### step 3: drag & drop
- unzip the data folder
- drag and drop the followers_and_following folder into the repository.
- the repository should now look like:  
  followers_and_following  
  |_ followers_1.html  
  |_ following.html  
  |_ ... other files from instagram  
  out  
  |_ mutuals.txt  
  |_ not_following_you_back.txt  
  |_ you_dont_follow_back.txt  
  src  
  |_ insta-follow-check.py  
  README.md  
