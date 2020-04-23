#! /usr/bin/awk -f
BEGIN {
  print "Content-type:text/html\n"
  print "<head>"
  print "<script>"
  print "window.onload = function () {"
  print "var chart = new CanvasJS.Chart("chartContainer", {"
  print "animationEnabled: true,"
  print "theme: 'light2',
  title:{
		text: 'Simple Line Chart'
	},
	axisY:{
		includeZero: false
	},
	data: [{        
		type: 'line',
      	indexLabelFontSize: 16,
		dataPoints: [
			{ y: 450 },
			{ y: 414},
			{ y: 520, indexLabel: '\u2191 highest',markerColor: 'red', markerType: 'triangle' },
			{ y: 460 },
			{ y: 450 },
			{ y: 500 },
			{ y: 480 },
			{ y: 480 },
			{ y: 410 , indexLabel: '\u2193 lowest',markerColor: 'DarkSlateGrey', markerType: 'cross' },
			{ y: 500 },
			{ y: 480 },
			{ y: 510 }
		]
	}]
});"
   print "chart.render();"
   print "}"
   print "</script>"
   print "</head>"
   print "<body>"
   print "<div id="chartContainer" style="height: 370px; width: 100%;"></div>"
   print "<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>" 
}