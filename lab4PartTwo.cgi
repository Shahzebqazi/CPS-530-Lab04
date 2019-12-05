#!/usr/bin/perl
use CGI ':standard';

my $name = param("Name");
my $music = param("music");
my $genre = param("genre");

print "Content-type: text/html\n\n";
print ( qq( <link href="https://fonts.googleapis.com/css?family=Cuprum" rel="stylesheet">
  <head>
    <style>
    body
    {
      background-color:black;
    }
    p
   {
      font-size:28px;
      color: white;
      font-family: 'Cuprum', sans-serif;
      text-align: center;
    }
    </style>
  </head>

  <body>
	<p> Results: </p>
        <p>Hello, $name. </p>
	<p>Do you like music: $music?</p>
      	<p> What Genre(s):  </p>
  </body>
  </html>
));