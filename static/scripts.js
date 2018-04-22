function clearCanvas() {
	ctx.clearRect(0,0,canvas.width,canvas.height);
}

function drawAllPoints(ctx) {
	if (points) {
		for(var i=0;i<points.length;i++) {
			drawPoint(ctx, points[i]);
		}
	}
}

function drawPoint(ctx, elem) {
	ctx.fillStyle = "#000";
	ctx.beginPath()
	ctx.arc(elem.x, elem.y, 4, 0, 2*Math.PI);
	ctx.fill();
	ctx.stroke();
}

function setIdCookie() {
	var string = "chosen-ids=";
	for(var i=0; i<chosenIds.length;i++) {
		var id = chosenIds[i];
		console.log(id);
		string += id + ",";
	}
	string = string.slice(0,string.length-1);
	string += "; expires=Fri, 31 Dec 9999 23:59:59 GMT";
	document.cookie = string;
	console.log(string);
}

function getIdCookie() {
	var oldCookie = document.cookie;
	var value = ";" + oldCookie;
	var parts = oldCookie.split("chosen-ids=");
	if (parts.length == 2) {
		return parts.pop().split(";").shift();
	}
	else return "";
}

function getPointsCookie() {
	var parts = document.cookie.split("points=");
	if (parts.length == 2) {
		return JSON.parse(parts.pop().split(";").shift());
	} else {
		return;
	}
}

function setPointsCookie() {
	var string = "points=";
	string += JSON.stringify(points);
	string += "; expires=Fri, 31 Dec 9999 23:59:59 GMT";
	document.cookie = string;
	return string;
}

function clearCookies() {
	document.cookie = "points=; expires=Thu, 01 Jan 1970 00:00:01 GMT";
	document.cookie = "chosen-ids=; expires=Thu, 01 Jan 1970 00:00:01 GMT";
	points = [];
	chosenIds = [];
	deleteAllIdRows();
}

function loadFromCookie() {
	points = getPointsCookie();
	var cookie = getIdCookie();
	console.log(cookie);
	if (cookie) {
		chosenIds = cookie.split(",");
	}
}

function getTemp(deviceId) {
	var d =getMostRecentData(deviceId); 
	if (d) {
		return d["temp"];
	}
	else {
		return 0;
	}
}

function getHumid(deviceId) {
	var d =getMostRecentData(deviceId); 
	if (d) {
		return d["humid"];
	}
	else {
		return 0;
	}
}

function getMoist1(deviceId) {
	var d =getMostRecentData(deviceId); 
	if (d) {
		return d["moist1"];
	}
	else {
		return 0;
	}
}

function getMoist2(deviceId) {
	var d =getMostRecentData(deviceId); 
	if (d) {
		return d["moist2"];
	}
	else {
		return 0;
	}
}

function getMostRecentData(deviceId) {
	if (data) {
		for(var i=data.length-1;i>=0;i--) {
			if (data[i]["device_id"] == deviceId) {
				return data[i];
			}
		}
	}
	return;
	//var mostRecentDate = Math.min.apply(Math, data.map(function(d) {if (d["device_id"]==deviceId) return data["timestamp"]}));
	//var mostRecentData = data.find(d => d["device_id"] == deviceId && d["time"] == mostRecentDate);
	//return mostRecentData;
}