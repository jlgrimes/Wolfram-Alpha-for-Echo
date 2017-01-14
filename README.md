# Wolfram-Alpha-for-Echo
A python script that hooks wolfram alpha to the amazon echo. Works with normal questions as well as calculus :D (hopefully). Functions currently include:
* Any standard question (mass of the sun, atoms in the universe, one plus one, etc.)
* Derivatives (derive inverse tangent of x, find the derivative of 2x squared)
* Indefinite Integrals (integrate cosine of x, find the antiderivative of x)

The default trigger for the skill is "Ask Wolfram Alpha", but of course you can customize it to whatever you'd like through the Intent Schema.

## Prerequisites

What you need first is a **Wolfram Alpha App ID**. This allows you to access the API as a developer, which you kind of need to do anything. To get one, go to https://developer.wolframalpha.com/portal/signin.html and log in to the Developer Portal using your Wolfram ID (if you don't have one of those, go to https://developer.wolframalpha.com/portal/signup.html). Click the "Get an AppID" button, and bam, there's your AppID.

Next up, download a .zip of everything in this repository. First thing's first though, you need to put your AppID into the program. To do this, open up alexa-wolframalpha.py, scroll down to line 119, and enter your AppID into the quotation marks.

You're going to need two websites to get this program up and running: the AWS Management Console, and the Amazon Developer Portal. If you're not an Amazon developer already, go to https://developer.amazon.com/home.html and make one with your existing Amazon account (if you don't have an Amazon account, you should probably make one!). Leave these websites open on different tabs, because there's oging to be a lot of switching!

## Creating the Lambda Function

First, go to https://aws.amazon.com/console/, and click Sign Into Console on the upper right to go to the AWS Management Console. **Now, go to the upper-right corner next to your name, and click N. Virginia as your region. If you don't do this, you'll have to redo everything.** Under the Build a Solution header, click Deploy a serverless microservice to get to the Lambda Management Console.

Once you're there, go ahead and create a new Lambda Function, and **make sure to add the Alexa Skills trigger.** Name it something like Wolfram Alpha, change the code type to Python 2.7, and copy and paste the code from wolfram-alexa.py into the box. You can put whatever you want for the role and description.

After you've made the Lambda Function, jump into the Dashboard for the funciton you just made by clicking on it. Go to Actions on the top next to Test, then Configure test event. Copy and paste the code from test_event.json into the box, then save. Next, go to the Configuration tab, click on Advanced Settings, and change the timeout time from the default of 3 seconds to something more generous, such as 10 seconds. 

Oh yeah, you see on the top right of the screen where it says **ARN** - arn:aws:lambda:us-east-1:xxxxxxxxxx:function:WolframAlpha? Copy and paste everything after **ARN** into a seperate document, because you're going to need to this.

## Creating the Alexa Skill

Next, go to https://developer.amazon.com/home.html yet again once you have an account to access the dashboard. Hit the Alexa tab from the top, and then Get Started to the Alexa Skills Kit. Then, hit Add a New Skill. You can name the skill whatever you want, but ultimately this is going to be what's run on your Amazon Echo, so try to name it something like Wolfram Alpha. The Invocation Name should be wolfram alpha as well.

Now, click Next. Copy everything from intent_schema.json into the Intent Schema box, and everything from sample_utterances.txt into the Sample Utterances box. Click Next again, and you should see a spot to enter in an ARN for the lambda function you made. Sound familiar? It's because that's the string we copied earlier fro the upper-right corner of AWS Console. Take that entire string and paste it in, and select the appropriate region identifiers when prompted.

Go ahead and finish the skill creation process (it should be pretty straight forward), but **leave it in Developer mode. Do not publish your Alexa skill.**

## Deploying all of this onto your Amazon Echo

Guess what, you've already done all of the hard work! Amazon now has automagically put the Wolfram Alpha skill you made onto your Echo through your Amazon account!

## Debugging

If you want to contribute to this project in any way possible, there are several ways you can debug, so I'll be listing all of them in the order that I personally prefer, starting with the most preferable.

### Through the Alexa Skills Portal

The most responsive way to debug is through the Alexa Skills tab in the Developer Portal we talked about earlier. All you have to do is enter the speech input, and it will give you the speech output, card output, and many more useful things. To access this option, edit your Wolfram Alpha skill, and click on the Test tab on the left side of the screen.

### Through the Echo itself

Ultimately, the easiest way to see what's going to happen with the Echo is, you guessed it, using the Echo. The problem with this approach is the lack of debugging tools, but you kind of have to test it on the Echo *eventually* if you want to use this skill at all :P

### Through the Lambda Management Console

Another way to debug is through the Lambda Management Console. This approach doesn't really have any benifits over the others, except that you can debug the Lambda function seperately from the Alexa Skill, which could be useful in some cases. To access this option, inside of the Lambda function you made, click the Actions button (next to Test), then Configure test event. As you can see, there's going to be a question that I already put in there, which happens to be "what is the antiderivative of two x squared". Replace this with whatever you want, save and test the Lambda function, and you should get an output at the bottom of the screen.
