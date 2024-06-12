window.onload(masterFunction())

function masterFunction() {
    //drawRect(100, 475, 475, 100, '#000000', false, 1.0)
    drawLine(100, 475, 475, 475)
    drawLine(510, 475, 525, 475)
    drawLine(525, 475, 525, 575, )

    drawLine(510, 475, 510, 125, "#000000")
    drawLine(475, 475, 475, 125, "#000000")


}


function drawLine(x1, y1, x2, y2, color) {
    var canvas = document.getElementById('Canvas').getContext("2d");
    canvas.beginPath();
    canvas.moveTo(x1, y1);
    canvas.lineTo(x2, y2);

    canvas.strokeStyle = color;
    canvas.stroke();
}

function drawRect(x, y, width, height, color, filled, transparency) {
    var canvas = document.getElementById('Canvas').getContext("2d");
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