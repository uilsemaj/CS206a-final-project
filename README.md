
## for offline execution (only my local)
conda activate roboticsfinalproject

# Signal Processing
## File
- bpm-detection taken from: https://github.com/scaperot/the-BPM-detector-python
- works decently enough.
- FOR ROS VERSION: use bpm_detection_ros.py

## calibration
- 80 bpm: shows up as 160 bpm on bpm_detection
- 104bpm.wav: shows up as 207.85219399538104 on bpm_detection
- starwars is about "Completed!  Estimated Beats Per Minute: 159.24642544499562" and based on 
- to run: ```python bpm_detection.py --filename calibration/104bpm.wav```

# Using SSH to retrieve and download Github
Password is deprecated and we can only use SSH to push new changes. Essentially you will first generate a SSH key, upload the ssh key you generate to Github, and then use ssh agent to authenticate your service against Github so Github knows it's you.

- Use this [link](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GitHub-SSH-Key-Setup-Config-Ubuntu-Linux) to set up the SSH connections. 
- Trouble shoot: (likely to happen if you already have a repo checked out prior to setting up ssh) Verify if the repository is with SSH and NOT HTTPS: if github is asking you for password, then you are using HTTPS. use [this](https://stackoverflow.com/questions/14762034/push-to-github-without-a-password-using-ssh-key) to switch to SSH.
  -  `c105-5 [525] ~/ros_workspaces/Github/CS206a-final-project # git remote set-url origin git@github.com:uilsemaj/CS206a-final-project.git `
