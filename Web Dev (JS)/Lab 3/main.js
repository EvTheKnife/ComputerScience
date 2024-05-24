function drawScreen() {


    drawRect1(0, 0, 200, 200, "#f0f0e6", true, 1); //draw paper color
    //drawLine(40, 0, 40, 200, "#1111ff"); //draw vert line
    
    //draw horiz lines
    drawLine(0, 10, 200, 10, "#333333")
    drawLine (0, 30, 200, 30, "#333333");
    drawLine (0, 50, 200, 50, "#333333");
    drawLine (0, 70, 200, 70, "#333333");
    drawLine (0, 90, 200, 90, "#333333");
    drawLine (0, 110, 200, 110, "#333333");
    drawLine (0, 130, 200, 130, "#333333");
    drawLine (0, 150, 200, 150, "#333333");
    drawLine (0, 170, 200, 170, "#333333");
    drawLine (0, 190, 200, 190, "#333333");

    //Draw 6 S lines
    drawLine(70, 35, 70, 80, "#000000")
    drawLine(100, 35, 100, 80, "#000000")
    drawLine(130, 35, 130, 80, "#000000")
    drawLine(70, 115, 70, 165, "#000000")
    drawLine(100, 115, 100, 165, "#000000")
    drawLine(130, 115, 130, 165, "#000000")

    //Draw top
    drawLine(70, 35, 100, 10, "#000000")
    drawLine(130, 35, 100, 10, "#000000")

    //Draw bottom
    drawLine(70, 165, 100, 190, "#000000")
    drawLine(130, 165, 100, 190, "#000000")

    //Draw middle
    drawLine(70, 80, 100, 115, "#000000")
    drawLine(100, 80, 130, 115, "#000000")
    drawLine(70, 115, 85, 97, "#000000")
    drawLine(130, 80, 115, 97, "#000000")

}

function drawLine(x1, y1, x2, y2, color) {
    var canvas = document.getElementById('canvas').getContext("2d");
    canvas.beginPath();
    canvas.moveTo(x1, y1);
    canvas.lineTo(x2, y2);

    canvas.strokeStyle = color;
    canvas.stroke();
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

function drawRect1(x, y, width, height, color, filled, transparency) {
    var canvas = document.getElementById('canvas').getContext("2d");
    canvas.beginPath();
    canvas.rect(x, y, width, height)
    if (filled) { // if filled is true 
        canvas.globalAlpha = transparency;
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

function clearRectangle(x, y, width, height)
{
    var canvas = document.getElementById("canvas").getContext("2d");
    canvas.clearRect(x, y, width, height);
}

