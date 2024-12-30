# Command Line for the Win

## Overview

This project is an optional challenge to improve and demonstrate Bash scripting and command-line skills. It involves completing tasks on the CMD CHALLENGE website, taking screenshots of the completed tasks, transferring them to a sandbox environment via SFTP, and pushing them to GitHub. 

By completing this project, I was able to further develop my understanding of the command line and SFTP commands.

## Project Structure

This project consists of three stages:

1. Complete the first 9 tasks on CMD CHALLENGE.
2. Complete the next 9 tasks, bringing the total to 18.
3. Complete the final 9 tasks, bringing the total to 27.

Screenshots are taken after each stage and transferred to the sandbox environment using SFTP.

### Files in the Repository

- `0-first_9_tasks.jpg` - Screenshot showing completion of the first 9 tasks.
- `1-next_9_tasks.jpg` - Screenshot showing completion of 18 tasks.
- `2-next_9_tasks.jpg` - Screenshot showing completion of all 27 tasks.
- `README.md` - This file, documenting the process of completing the project.

## Steps Followed

### Task Completion

1. **Access CMD CHALLENGE**:
   I accessed [CMD CHALLENGE](https://cmdchallenge.com) to complete the tasks.

2. **Complete the Tasks**:
   - I completed the first 9 tasks and took a screenshot after finishing them.
   - Then, I completed the next 9 tasks (total of 18) and took a second screenshot.
   - Finally, I completed the last 9 tasks (total of 27) and took a third screenshot.

3. **Name the Screenshots**:
 Kindly note that I saved the screenshots with the following names:
   - `0-first_9_tasks.jpg`
   - `1-next_9_tasks.jpg`
   - `2-next_9_tasks.jpg`

### SFTP File Transfer

After taking the screenshots, I used the SFTP command-line tool to transfer them to the sandbox environment.

Steps I followed:

1. **Open Terminal and Connect to the Sandbox**:
   I connected to the sandbox environment using the provided credentials:
   ```bash
   sftp username@sandbox-hostname
   ```
2. **Navigate to the Directory:** Once connected, I navigated to the appropriate directory:

```bash
cd /root/alx-system_engineering-devops/command_line_for_the_win/
```

3. **Transfer the Screenshots:** I used the put command to transfer the screenshots:

```bash
put /path/to/local/0-first_9_tasks.jpg
put /path/to/local/1-next_9_tasks.jpg
put /path/to/local/2-next_9_tasks.jpg
```

4. **Verify the Transfer:** I verified the files were successfully transferred using the ls command:

```bash
ls
```

### Pushing Screenshots to GitHub
1. **Add the Files to Git:** I added the screenshots and the README.md to my local Git repository:

```bash
git add 0-first_9_tasks.jpg 1-next_9_tasks.jpg 2-next_9_tasks.jpg README.md
```
2. **Commit the Changes:** I committed the changes with an appropriate commit message:

```bash
git commit -m "Added screenshots for CMD CHALLENGE tasks and updated README"
```
3. **Push to GitHub:** Finally, I pushed the changes to the remote GitHub repository:

```bash
git push origin main
```

## Conclusion
The CMD CHALLENGE project was a valuable exercise in improving my command-line proficiency and mastering the use of SFTP for file transfers. The tasks progressively increased in complexity, providing a challenging yet rewarding experience.
