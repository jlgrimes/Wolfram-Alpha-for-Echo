# Wolfram-Alpha-for-Echo
A python script that hooks wolfram alpha to the amazon echo. Works with normal questions as well as calculus :D (hopefully)

## How to get this thing to work:

What you need first is a **Wolfram Alpha App ID**. This allows you to access the API as a developer, which you kind of need to do anything. To get one, go to https://developer.wolframalpha.com/portal/signin.html and log in to the Developer Portal using your Wolfram ID (if you don't have one of those, go to https://developer.wolframalpha.com/portal/signup.html). Click the "Get an AppID" button, and bam, there's your AppID.

Next up, download a .zip of everything in this repository. First thing's first though, you need to put your AppID into the program. To do this, open up alexa-wolframalpha.py, scroll down to line 119, and enter your AppID into the quotation marks.

Here's where things get real. You're going to need two websites to get this program up and running: the Amazon Lambda Management Console, and the Amazon Developer Portal. If you're not an Amazon developer already, go to https://developer.amazon.com/home.html and make one with your existing Amazon account (if you don't have an Amazon account, you should probably make one!). Next, go to https://developer.amazon.com/home.html yet again once you have an account to access the dashboard. Hit the Alexa tab from the top, and then Get Started to the Alexa Skills Kit. Then, hit Add a New Skill. You can name the skill whatever you want, but ultimately this is going to be what's run on your Amazon Echo, so try to name it something like Wolfram Alpha. The Invocation Name should be wolfram alpha as well.

