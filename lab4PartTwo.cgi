
<html><head><title>Perl-html Example</title></head>
 
<body bgcolor=white>
 
<center><H2>Math 210 A Simple Web Form Using Perl</H2></center>
 
<form method="POST" 
action="http://johnny.sas.upenn.edu/~kazdan/cgi-bin/210/web_script1.pl">
 
<B>What is your first name? </B><input type=text name="first_name" size=20>
<P>
<B>How old are you?</B> <input type=text name="age" size=5></b></center>
<p>
This computes your age 11 years from now.
<p>
<center><input type=submit value="Submit"></center>
</form>

<hr><hr>
<center><tt><b>Here is the text of the Perl script that this form calls</b></tt>
</center>
<hr>
<pre>
#!/usr/bin/perl
require 5.003;
#push(@INC,"/www/cgi-bin");
push(@INC,"/home/httpd/cgi-bin");
require 5.003;
require "cgi-lib.pl";
 
