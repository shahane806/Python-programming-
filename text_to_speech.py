import pyttsx3
import pyautogui

engine = pyttsx3.init('sapi5')
engine.getProperty('voice')
engine.setProperty('voice', [0])

rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

volume = engine.getProperty('volume')
engine.setProperty('volume', 100)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':

    speak('Hello guys, i am friday oms personal assistant and todays topic is top five programming languages for you to learn in 20 21.are you ready ,lets get started.')

    speak('     Number five, c plus plus. Now i know youre talking about the new you just bad,is so old, its not interesting, no listen to me c plus plus it is the first languages that came out not only that this is a language that all the other languages stem from if you know c plus,you will pretty much be able to learn all the other languages now, on top of that some of the top companies like uber, google, amazon, facebook they all use c plus plus. Gaming companies like E A, nintendo ,sony blizzard are all using c plus plus for their gaming engine to build games. So if you want to build games like star wars were talking assassins creed anything else related to games you need to know c plus plus ,  for example actually machine learning, teslas auto pilot system is actually built on c plus plus like what?how crazy is that!! and according to indeed.com and the average c plus plus developer still makes a hundred and four thousand dollars this is a program language that is not going away anytime soon and is still going to be a very pinnacle of software development.')

    speak('     Number four. c sharp, now it is a very useful laker, that is easy to learn and it was built to compete with java and right now it is having a crazy comeback. Heres why right now windows applications like microsoft office ,microsoft excel were talking photoshop ,were talking internet explorer scratch that one though now on top of this right now.  VR development which is going really high is actually using c-sharp so if you are interested in building games with c-sharp okay!! this is the place to go over a few years coming its going to skyrocket like ,crazy believe me theres an amazing community with c-sharp developers and you will not be left out another. Fun fact about c-sharp is, its actually used for building virtual reality games right were talking oculus were talking google the google virtual reality glasses i think right whatever, its called so as its going up in ranks as more people use virtual reality. C is going to be even more popular and more demanded now according to indeed.com c developers right now make over 98000 on average but i really think its gonna increase throughout the time with the whole virtual reality aspect.')

    speak('     Number three, JAVA Now java is a very popular language to learn so when youre talking about building android applications that is what its used for also very much known in the enterprise software and actually listen this, 97 of enterprise applications use java for developing large-scale software that means that if you want to work at companies like google, like microsoft, like uber, they all use java for their large applications. Web applications enterprise software that is what they use now according to indeed.com java developers on average make a hundred and nineteen thousand dollars and in terms of demand at the time of filming there are over 33000 jobs so the demand is there the necessity is there and, based on that it is one of the most demanded programming languages out there now if we do take a look at google trends we can see that, this programming language is declining just a little bit because all languages like kotlin which are trying to replace, it but i personally think its going to take a long time for these languages, to replace something as big as java that is used by so many diverse applications i personally learned it when i was a beginner as well and so you should learn it too...')

    speak('     Number two is python, now you are hate me why? python is number two i know the python is super  cool i was coded in python by om. Python is on the actual upscale and because of the amazing community for python because of the amazing libraries lik psychiclearn, like django that allows people to build humongous applications right were talking machine learning, were talkin AI,were talking voice assistants like siri, were talking data science or accommodation engines like on amazon where you say heyyou might also like this that is why python is so important. Number one, javascript now but, no hold on, this is not javascripts no hold on, listen to this, the javascript is its a languag i always recommend to any beginner not only because its so easy to learn but also because its visual.')

    speak('     lets talk about some facts, javascript has been the number one programming language on stack over, for developer story for the past seven years applications like facebook, front end like instagram anything you see on the website what do you think its built with javascript? because of its popularity right we have frameworks like react.js, liveview.js like english and and many others to go ahead and come in use javascript to allow people to build more applications tesla for example,  right especially right now cross platform replication meaning applications for ios and for android are being built with technologies like react native which is using javascript, for example tesla the tesla app that you see on the app store that is built using javascript that is built using react native netflix their whole system on the back end they are using node.js with javascript.')

    speak('     if youre an absolute beginner if you want to learn  free courses i specially recommended you to check the CodeWithHarrys channel you get all courses free and in Hindi.')

    speak('if you are new in this channel please subscribe the channel and like the video.')
    speak('Thank you so much guys for watching this video and i will see you next time!!')

    # speak('Thank you so much for watching this video like the video and subscribe the channel')
