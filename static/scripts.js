
var background = new Image();
background.src = "https://lh3.googleusercontent.com/lpuKECB0msW6wEUXdlIihu1hyt14DvyTQ8csxVLlfxN_YkM-sz3P6MkfKM427lc4DZnEPrho5FrlvdJJtDhWkjj5HsEr8SUzJfdY_du5Po3Z6OUTjVMfqtDIdK710Lz7ySjlUEd6K6g=s766-no";

function drawBackground(ctx) {
}

function clearCanvas(ctx) {
	ctx.clearRect(0,0,300,300);
	ctx.drawImage(background, 0, 0, 300, 300);
	return background.url;
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

function setImageCookie() {
	var string = 'bgimage=';
	string+=background.src;
	string += "; expires=Fri, 31 Dec 9999 23:59:59 GMT";
	document.cookie = string;
}

function getImageCookie() {
	var oldCookie = document.cookie;
	var parts = oldCookie.split("bgimage=");
	if (parts.length == 2) {
		return parts.pop().split(";").shift();
	}
	else return "";
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
		return [];
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
	var bgimage = getImageCookie();
	if (bgimage != "") {
		background.src = bgimage;
	}
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


function findMinObj(obj, ind) {
	if (!obj) return;
	var min = obj[0];
	for (var i=0;i<obj.length; i++) {
		if (min[ind] > obj[i][ind]) {
			min = obj[i];
		}
	}
	return min;
}

function changeBackgroundImage() {
	var imageUrl = document.getElementById("image-entry").value;
	background.src = imageUrl;
	setImageCookie();
	drawAll(ctx);
}
