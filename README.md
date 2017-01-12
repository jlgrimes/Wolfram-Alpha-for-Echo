# Wolfram-Alpha-for-Echo
A python script that hooks wolfram alpha to the amazon echo. Works with normal questions as well as calculus :D (hopefully)

## Prerequisites

What you need first is a **Wolfram Alpha App ID**. This allows you to access the API as a developer, which you kind of need to do anything. To get one, go to https://developer.wolframalpha.com/portal/signin.html and log in to the Developer Portal using your Wolfram ID (if you don't have one of those, go to https://developer.wolframalpha.com/portal/signup.html). Click the "Get an AppID" button, and bam, there's your AppID.

Next up, download a .zip of everything in this repository. First thing's first though, you need to put your AppID into the program. To do this, open up alexa-wolframalpha.py, scroll down to line 119, and enter your AppID into the quotation marks.

You're going to need two websites to get this program up and running: the AWS Management Console, and the Amazon Developer Portal. If you're not an Amazon developer already, go to https://developer.amazon.com/home.html and make one with your existing Amazon account (if you don't have an Amazon account, you should probably make one!). Leave these websites open on different tabs, because there's oging to be a lot of switching!

## Creating the Lambda Function

First, go to https://aws.amazon.com/console/, and click Sign Into Console on the upper right to go to the AWS Management Console. **Now, go to the upper-right corner next to your name, and click N. Virginia as your region. If you don't do this, you'll have to redo everything.** Under the Build a Solution header, click Deploy a serverless microservice to get to the Lambda Management Console.

## Creating the Alexa Skill
Next, go to https://developer.amazon.com/home.html yet again once you have an account to access the dashboard. Hit the Alexa tab from the top, and then Get Started to the Alexa Skills Kit. Then, hit Add a New Skill. You can name the skill whatever you want, but ultimately this is going to be what's run on your Amazon Echo, so try to name it something like Wolfram Alpha. The Invocation Name should be wolfram alpha as well.

Now, click Next. Copy everything from intent_schema.json into the Intent Schema box, and everything from sample_utterances.txt into the Sample Utterances box.
