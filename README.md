Introduction
===================
The provider use the URL address for each subject:  General, Movies, TV Shows, Seasons and Animes.

The url has reserved word QUERY which will be replace with each query and the spaces will replaced by separator characters.

If you want to add some word to the search, you can use the queries. 

>{title}  => Title in english

>{year}	 => Year

>{title:ru}  => Title in russian

>{title:fr}  => Title in french

>{season}  => Season

>{season:n}  => Season with format in n digits

>{episode}  => Episode

>{episode:n}  => Episode with format in n digits

>s{season:2}e{episode:2}  =>  S02e02

>s{season}e{episode}  =>  S2e2

>s{season}e{episode:3}  => s2e002


For advanced queries:

>{title} swedish

It will search for the title in english plus the word swedish

Filtering
===================
This helps to parse the results according keywords.

The accepted keywords mean that the title needs to have any or all of those keywords to be accepted.
The blocked keywords mean that the title will be rejects if it has any or all of those keywords.

The keywords need to be inside curly brackets, ie:  {720p}

If you have several keywords:
> {720p}{hdtv}{4k}  
It means 720p OR HDTV or 4K.

If you have several words in the same curly brackets
> {720p hdtv}  
It means 720p AND HDTV.

It could possible different combination.

No keywords means the option is disabled.

The keywords are case case insensitive.

The keywords search any match, starting, in the middle or finishing, ie:  {cam}
it will be positive for words like webcam camera webcaming

If you want only the word, you need to use ? character, ie: 
{?cam} only starting with cam
{?cam?} only the word cam
{cam?} only finishing with cam

By default the provider always check that the name of the result has all the words of the title.  However, that option can be disabled from the settings.

Installation
============
Please, visit this link: https://github.com/mancuniancol/repository.magnetic


HTML Parsing
=============
For the HTML parsing, the provider uses instances of the tag class.  This tag object contains the html code of the tag.

There are two search functions which can be concatenated:

* **find_once(_tag_, _select_, _order_)**: it finds one element. It returns the tag class object.
    - _tag_: name of the tag to search, str.
    - _select_ (optional, by default, any attribute): tuple (attribute, value attribute).  Attribute is str. value attribute can be str where any space will act as AND operator.  It also can be a list of str where each element will be tested with the OR operator.
    - _order_ (optional, by default, 1): it will represent the n-th element to select.  If the n-th element doesn't exist will return empty string.

* **find_all(_tag_, _select_, _order_, _start_, _every_)**: it finds all the elements which match with the options.  It returns a list of tag class objects.
    - _tag_: name of the tag to search, str.
    - _select_: tuple (attribute, value attribute).  Attribute is str. value attribute can be str where any space will act as AND operator.  It also can be a list of str where each element will be tested with the OR operator.
    - _start_: it selects which will be the first tag object to be added to the result list.  It helps to skip the first elements.
    - _every_: it helps to select just every other element or more.  In conjunction with _start_ is possible to select just even or odd elements.

Examples:
    Select the first 'body' tag element and inside of that find all the 'tr' tag elements.
    
            "find_once(tag='body').find_all('tr')"

There is just one function to get information of the tag class object:
* **item(tag, attribute, order, selection)**: It returns the value of the selected attribute of the tag object.  By default the attribute is text.
    - _tag_ (optional): name of the tag to select, str.
    - _attribute_ (optional): the attribute which the value will be returned.
    - _select_: tuple (attribute, value attribute).  Attribute is str. value attribute can be str where any space will act as AND operator.  It also can be a list of str where each element will be tested with the OR operator.
    - _order_ (optional, by default, 1): it will represent the n-th element to select.  If the n-th element doesn't exist will return empty string.
    
    Examples:
     - Show the value of 'href' attribute of the second 'a' element in the tag object.
    
            "item(tag='a', attribute='href', order=2)"
     
     - Show the value of 'text' attribute of the fifth 'td' element in the tag object.

            "item(tag='td', order=5)"
     
     - Show the value of 'text' attribute of everything inside of the tag object.
            
            "item()"