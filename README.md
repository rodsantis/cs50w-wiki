# cs50w-wiki
Implementing a Wiki encyclopedia

In this project I had to implement the bone structure of a wikipedia like page.

The first required inplementation was the entry page in which the user if type wiki/TITLE (for Title the name of the article) the user should be redericted to
that entry page. This entry page will be searched by a function in util.py and if found it should be displayed the information to the user if not found or 
if doesn't exist and error page should be shown.

The second implementation was to make the index.html page (which contain a list of all of the entries that we have in the wikipide) clickable, meaning that
if the user clicks in one of the names the user should be taken to the entry page with its information.

The third implementation was the search bar on the left menu. I had to allow the user to search in it and if the entry was found and the name was typed the 
entry page should be displayed with its information, but if the user typed just a couple of letters like "ytho" I should substring it and return all the possible
results in a list format with a hyperlink style so the user could click in the desired one and go to that page with its information. If the user doesn't type anything 
and just hit enter everything will be showns as list with a message that the User could find one of the links useful.

The fourth implementation was the New Entry Page, in which is a link from the left menu that the user could click to go to a page in which would be able to 
create a New Entry. If that entry doesn't exist it would be save, otherwise would show an error message letting the user knows that already exist. Everytime that
a new Page is created and saved successfully the user will be redirected to that new page entry.

The fifth implementation was to add an Edit button in every entry page information so that if clicked the user would be redirected to a page in which the textarea
 would be showing the existing text already and let the user edit it and hit save. Once the save button is clicked the user will be redirected to that entry page
 with its modifications.

The sixth implementation was to make the Random Page side bar menu work in a way that, everytime that it is clicked it should bring the user to a random page and
 display its information.

The seventh implementation was to translate the Markdown language (which is the language that every entry is written) to HTML language so that when displayed 
in our webpage it would be displyed using all the correct fonts, weights and style
