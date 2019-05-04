# Crypto II Writeup

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (40 Pts)

### Part 2 (60 Pts)
Level 1:
The first level asked to inject a script that causes the Javascript alert() pop
up to be invoked through the search box. I initially tried 'asd' in the the search box
and it brought me to page where it says "Sorry, no results were found for asd. Try again." This immediately told me that the input from the search box is converted into HTML code and the input becomes embeded in the next page. This means I can write direct HTML code and the search box would convert the input into HTML code that would be executed. I then wrote in the search box "<script>alert('hi')</script>" which executed the alert() pop up. The site then said 'Congratulations, you have executed an alert: hi.'

Level 2:
In this level I tried using the same step as above but the script would not execute. I looked at the HTML code when adding a post and it creates an HTML element still. So I tried using this to my advantage and inserted a button. In HTML you can add the onclick attribute to a button which triggers the code set by that attribute when clicked. So I put the code:
'<button onclick="alert('gottem')">Ez</button>' 
in the textbox and shared my status. This created a button in the post which when clicked, fired  the onclick attribute and executed the alert. The alert said 'gottem' after the congrats message.

Level 3:
Looking at the HTML code in the script tag there is:
'function chooseTab(num) {
    var html = "Image " + parseInt(num) + "<br>";
    html += "<img src='/static/level3/cloud" + num + ".jpg' />";
     ... }'
This means if we change the frame number in the URL we can cause the chooseTab function to fail by making parseInt to fail. So I can pass an invalid input such as:
https://xss-game.appspot.com/level3/frame#'
where " ' " is not a invalid character to the function and will fail to parse. This causes an error as nothing loads so I can catch the error using:
https://xss-game.appspot.com/level3/frame#asd onerror="alert('lvl3');"
which will call the alert function when it crashes. We can't use letters such as 'asd' since it won't crash because parseInt will return NaN. 

Level 4:
I noticed when you pick a timer, then it adds to the url for 6:
?timer=6
I looked at the HTML code and there is a line
<img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />
I noticed the timer variable is being used with string literal syntax. So the time is passed in as a string and directly into that HTML code. The string:
"startTimer('{{ timer }}');"
has " (' " before timer so I could manually close it off with when I pass in timer by passing in " ') " as the timer. If I closed it off then I could continue the string with more javascript which is the alert function. I don't have to close the string inside of alert off since the HTML does that for me as I manually closed the previous (' off. Therefore I was able to plug in:
 6');alert('lvl4 
into the input which added to the HTML and invoked the alert function.

Level 5:
In the HTML is 
 <a href="{{ next }}">Next >></a
 href would redirect you to where you clicked. There is a way to execute javascript code instead through the href. Since we can use 'next' to insert whatever we want, 
 we can insert javascript code with the string:
 " javascript:alert('lvl5') "
 By doing this, when the next button is clicked, instead of going to the next link, it would execute the alert function.
 So I changed the URL to 
 https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('lvl5');
 which changes the function of the Next button. Then I clicked the next button and the alert showed.

 Level 6:
 I expolited the google.com/jsapi?callback=f vulnerability as it invokes the function associated with the callback. 
 If we replace f in the url above with alert and visit the link  google.com/jsapi?callback=alert , there is a bunch of data and at the bottom is
 alert(); which means it is invoked. Therefore we use the url https://xss-game.appspot.com/level6/frame#//www.google.com/jsapi?callback=alert which will use the vulnerability and invoke the alert function. It popped up as undefined since I did not pass in any string. This vulnerability works since we can load the data from google.com/jsapi?callback=alert instead of a gadget. I got this with the help from the hints and by messing with the url it provided.
