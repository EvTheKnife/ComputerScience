function drawLine(x1, y1, x2, y2, color) {
    var canvas = document.getElementById('canvas').getContext("2d");
    canvas.beginPath();
    canvas.moveTo(x1, y1);
    canvas.lineTo(x2, y2);

    canvas.strokeStyle = color;
    canvas.stroke();
}