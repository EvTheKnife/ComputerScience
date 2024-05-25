function drawScreen() {

    drawTri(150, 100, 160, 10, 75, 125, "#00ff00", false);
    drawRect1(100, 150, 50, 70, "#ff0000", false);
    drawArc(180, 270, 50, 180, 360, "#00ff00", false);
    drawCirc(150, 200, 50, "#000000", true)

}


function drawTri(x1, y1, x2, y2, x3, y3, color, filled) {
    var canvas = document.getElementById('canvas').getContext("2d");

    canvas.beginPath();
    canvas.moveTo(x1, y1);
    canvas.lineTo(x2, y2);
    canvas.lineTo(x3, y3);
    canvas.lineTo(x1, y1);
    canvas.closePath();

    if (filled) { // if filled is true 
        canvas.fillStyle = color;
        canvas.fill();
    } 
    else { // if filled is false
        canvas.strokeStyle = color;
        canvas.stroke();
    }
}

function drawRect1(x, y, width, height, color, filled) {
    var canvas = document.getElementById('canvas').getContext("2d");
    canvas.beginPath();
    canvas.rect(x, y, width, height)
    if (filled) { // if filled is true 
        canvas.fillStyle = color;
        canvas.fill();
    } 
    else { // if filled is false
        canvas.strokeStyle = color;
        canvas.stroke();
    }

}

function drawCirc(x, y, radius, color, filled) {
    var canvas = document.getElementById('canvas').getContext("2d");
    canvas.beginPath();
    canvas.arc(x, y, radius, 0, 2* Math.PI)

    if (filled) { // if filled is true 
        canvas.fillStyle = color;
        canvas.fill();
    } 
    else { // if filled is false
        canvas.strokeStyle = color;
        canvas.stroke();
    }
}

function drawArc(x, y, radius, start, stop, color, filled) {
    var canvas = document.getElementById('canvas').getContext("2d");
    canvas.beginPath();
    canvas.arc(x, y, radius, start * (180/Math.PI), stop * (180/Math.PI))
    if (filled) { // if filled is true 
        canvas.fillStyle = color;
        canvas.fill();
    } 
    else { // if filled is false
        canvas.strokeStyle = color;
        canvas.stroke();
    }
}


