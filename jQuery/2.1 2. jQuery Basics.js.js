// Try just the dollar sign: https://www.w3schools.com/jquery/jquery_selectors.asp
$

//$(selector).action()

//A $ sign to define/access jQuery
//A (selector) to "query (or find)" HTML elements
//A jQuery action() to be performed on the element(s)


// Grab the h1 header:
$('h1');

// Save it to variable:
var x = $('h1');

// Edit the css properties:
x.css("color",'green');
x.css("background","white");

// Multiple CSS properties variable(like an array):
var newCSS = {
  "color":"blue",
  "background":"white",
  "border":"black"
}

x.css(newCSS);

// Grabbing multiple returns an array-like object:
var listItems = $('li');

// Affects all items:
listItems.css("color",'red');

// Grab a single index item:
listItems.eq(0).css('color','green');

listItems.eq(1).css('color','yellow');

// Last item
listItems.eq(-1).css('background','red');

// TEXT and HTML

// Grabbing Text:
$('h1').text()

// Manipulating Text:
$('h1').text("Different Text")

// Grabbing HTML
$('h1').html()

// Manipulating HTML
$('h1').html("<b>Now in BOLD</b>")

// ATTRIBUTES and VALUES

// Manipulating an attribute
$("input").eq(1).attr('type','checkbox');

// Manipulating values
$("input").eq(0).attr('value',"DIFFERENT VALUE");

// Can do this more directly:
$("input").eq(0).val("cleared up");


// CLASSES

// Add a Class
$('h2').addClass("NewClass")

// Remove a Class
$("h2").removeClass("NewClass");

// Toggle the Class
$("h3").addClass("Temp");

$("h3").toggleClass("Temp");
