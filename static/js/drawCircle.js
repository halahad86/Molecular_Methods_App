function drawCircle(data,size, area, dimension) {

	// Create the area for the map to be drawn
	var stage = new Kinetic.Stage({
		container: ('container' + area),
		width: dimension,
		height:  dimension
	});

	// This is where everything is held before being drawn at the end
	var layer = new Kinetic.Layer();

	// Start values so that the circle is drawn from the top round clockwise
	var currAng = -90;
	var nextAng = 0;

	// Set the center point of the circle
	var midW = stage.getWidth() / 2;
	var midH = stage.getHeight() / 2;

	// Create the circle to be the DNA being cut
	var circle = new Kinetic.Circle({
		x: midW,
		y: midH,
		radius: 70,
		fill: 'gray',
		stroke: 'black',
		strokeWidth: 1,
		opacity: 0.3
	});

	// Add the circle to the draw area
	layer.add(circle);

	// Loop over the Data by the pairs of values of size and name
	for (var i = 0; i < data.length; i = i + 2){
	
		// find the end location for the current segment
		var value = Number(data[i+1]);
		nextAng = (value/size) * 360;
		var cutW = Math.cos(currAng * Math.PI/180)
		var cutH = Math.sin(currAng * Math.PI/180)

		// write the text for showing cut size 
		var sizeText = new Kinetic.Text({
			x: midW + 90*Math.cos( (currAng + nextAng / 2) * Math.PI/180) - 10,
			y: midH + 90*Math.sin( (currAng + nextAng / 2) * Math.PI/180) - 10,
			text: (value/10.0).toPrecision(2),
			fontSize: 20,
			fontFamily: 'Calibri',
			fill: 'black'
		});

		// write the name of the emzyme responsible for this cut
		var nameText = new Kinetic.Text({
			x: midW + 90*cutW - 10,
			y: midH + 90*cutH - 10,
			text: data[i],
			fontSize: 20,
			fontFamily: 'Calibri',
			fill: 'black'
		});

		// Draw the line desginating the current cut
		var cutLine = new Kinetic.Line({
			points: [midW + 60*cutW, midH + 60*cutH, midW + 80*cutW, midH + 80*cutH],
			stroke: 'black',
			strokeWidth: 5,
			lineCap: 'square',
			lineJoin: 'square'
		});

		// Update the start pos for the next cur
		currAng = currAng + nextAng;

		// Add the pieces to the draw area
		layer.add(nameText);
		layer.add(sizeText);
		layer.add(cutLine);
	}
	
	// Now draw the pieces
	stage.add(layer);
}
