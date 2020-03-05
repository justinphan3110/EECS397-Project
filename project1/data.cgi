#! /usr/bin/awk -f
BEGIN {
  print "Content-type:text/html\n"
  print "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
  print "<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">"

  print "<body style=\"background-color:RosyBrown\">"
  print "<pre>"
  print "<h1> <a href=\"https://en.wikipedia.org/wiki/List_of_most_popular_given_names\"> List of most popular given names </a></h1>"
  
  printTable("Africa")
  printTable("Americas")
  printTable("Europe")
  printTable("Asia")

  buttonToggle()
  print "</body>"
}
func printTable(continent) {
    print "<button class=\"w3-button w3-red\" onClick=buttonToggle('" continent "')>" continent "</button>"
    print "<div id=" continent " style=\"display: none;\">"
    print "<h2>" continent "</h2>"
    print "<h3> Male names </h3>"
    print "<table>"
    printHeader()
    printNames("data/" continent "/male.txt")
    print "</table>"

    print "<h3> Female names </h3>"
    print "<table>"
    printHeader()
    printNames("data/" continent "/female.txt")
    print "</table>"
    print "</div>"	
}

func myFunction() {
	print "<script>"
        print "function myFunction() {}"
        print "</script"
}

func buttonToggle() {
   print "<script>"
   print "function buttonToggle(c){"
   print "var continent = 'Africa'"
   print "var x = document.getElementById(c);"
   print "if (x.style.display == 'none') {"
   print "x.style.display = 'block';"
   print "} else {"
   print "x.style.display = 'none';"
   print "}"
   print "}"
   print "</script>" 	 
}
func printNames(filePath) {
  print "<tr>"
  while ("cat -s " filePath | getline) {
     if($0 ~ /^$/) print "</tr>"
     else print "<td>" $0 "</td>"
  }

}

func printHeader() {
	print "<tr>"
        print "<th> Region (year) </th>"
        print "<th> No. 1 </th>"
        print "<th> No. 2 </th>"
        print "<th> No. 3 </th>"
        print "<th> No. 4 </th>"
        print "<th> No. 5 </th>"
	print "<th> No. 6 </th>"
	print "<th> No. 7 </th>"
	print "<th> No. 8 </th>"
	print "<th> No. 9 </th>"
	print "<th> No. 10 </th>"
	print "</tr>"
 }
