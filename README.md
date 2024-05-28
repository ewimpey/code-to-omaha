# ~Road~ Code to Omaha 24!
![Code to Omaha!](/helpers/code-to-omaha.jpg)

Join our NCAA Baseball Tournament Challenge and sharpen your coding skills at the same time! Whether you're a newbie or a seasoned veteran, follow these steps to submit your bracket predictions.

### Follow the instructions below to participate

## Step 1: Fork the Repository
At the top-right corner of the page, click the Fork button. This creates a copy of the repository in your GitHub account.

## Step 2: Clone Your Fork
Open your terminal or Git Bash.
Clone your forked repository to your local machine with the following command:

```sh
git clone https://github.com/<your-github-username>/code-to-omaha.git
```

Change directory to the cloned repository:
```sh
cd code-to-omaha
```

## Step 3: Fill Out Your Bracket

Fill out the bracket by running `fill_bracket.py`.
This will first prompt you for your GitHub username.

Then you'll be promptedto provide the winner and runner-up for each round. 

After picking each game, it will generate a new file called `[username]-submission.json` with all of your picks.

## Step 4: Commit Your Changes
After you've filled out your bracket, it's time to commit your changes:

Add the modified bracket.json file:
```sh
git add submission/[username]-submission.json
```
Commit your changes with a meaningful message:
```sh
git commit -m "Submitting <your-github-username> bracket"
```

## Step 5: Push Your Branch to GitHub
Push your submission to your remote repository.

```sh
git push origin main
```

## Step 6: Submit a Pull Request
Go to your forked repository on GitHub.
You'll see a Compare & pull request button for your recently pushed branches. Click it to create a pull request.

Ensure the base repository is set to ewimpey/code-to-omaha and the base branch is main.
Give your pull request a title and description, such as `<your-github-username> bracket submission`
Click Create pull request.

***
Congratulations! You've successfully submitted your bracket for the Code-To-Omaha challenge.

Next Steps:
* Confirm that the pull request gets approved
* Watch the repository for updates, including the leaderboard and game results.
* Feel free to discuss predictions, strategies, and Git tips in the Issues section!


## Thank you for participating, and may the best bracket win!
