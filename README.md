## How to keep your Twitter timeline clean and tidy

1. Download the code.

2. Register the application on [this Twitter developer page](https://dev.twitter.com/).

3. Copy <code>config-sample.py</code> to <code>config.py</code> and edit the necessary variables. This includes the auth tokens that you will obtain from the page above and the number of tweets you want to have at any given point in time.

4. It turns out it is [very tricky](https://stackoverflow.com/questions/8471489/find-all-tweets-from-a-user-not-just-the-first-3-200) to obtain more than 3200 tweets for a given user. So, in order to batch-delete everything from the beginning, we are going to download the very handy Twitter archive. Go to [your settings page](https://twitter.com/settings/account) and click on *Your Twitter archive*. Follow the instructions, download the <code>.zip</code> file and then copy the <code>tweets.csv</code> file to the folder containing the code.

5. Run <code>$ python delete_from_archive.py</code>. This will delete all your tweets since the beginning of time and will leave only the most recent <code>n_keep</code> alive (you set this up in your <code>config.py</code> file).

6. Every day, or hour, or whatever works for you, run <code>delete_tweets.py</code>. This will trim your timeline to the desired size.

And that's it. As long as you keep running the script from point 6, everything will be kept clean and tidy. It should be very easy to modify the code so that, instead of keeping the last *N* tweets, it keeps the ones from the last *D* days. I have no time to do this, but if you feel so inclined just take the code and help yourself.

The usual caveats apply: read the code and make sure you understand what it's doing, please do some tests before running it unattended, all under your responsibility, this might break your coffee machine, blah, blah.

