var heartX = 185;
var heartY = 182;
var heartColour = color(153, 8, 0);
var wallColour = color(230, 125, 87);

var drawLV = function(x, y, vol) {
    var h = (vol - 40) / 4;
    
    // Wall
    fill(wallColour);
    beginShape();
    curveVertex(x - 20,  y - 35);
    curveVertex(x,       y + 10);
    curveVertex(x + 35,  y + 22);
    curveVertex(x + 120, y + 20);
    curveVertex(x + 174 + h/4, y - 14);
    curveVertex(x + 120, y - 70 - h);
    curveVertex(x + 60,  y - 110);
    curveVertex(x + 27,  y - 89);
    curveVertex(x + 11,  y - 20);
    curveVertex(x, y);
    curveVertex(x, y);
    endShape();
    
    // Inside
    fill(heartColour);
    beginShape();
    curveVertex(x - 66,  y + -3);
    curveVertex(x,       y);
    curveVertex(x + 93,  y + h/3);
    curveVertex(x + 136 + h/2, y - 12);
    curveVertex(x + 100 + h/2, y - 43 - h);
    curveVertex(x + 45,  y - 84);
    curveVertex(x + 3,   y - 32);
    curveVertex(x, y);
    endShape();
};

var drawLA = function(x, y) {
    // Outside
    fill(wallColour);
    beginShape();
    curveVertex(x +  4, y - 45);
    curveVertex(x +  5, y - 36);
    curveVertex(x - 40, y - 38);
    curveVertex(x - 50, y - 68);
    curveVertex(x - 12, y - 100);
    curveVertex(x + 25, y - 96);
    curveVertex(x + 51, y - 100);
    curveVertex(x, y);
    endShape();
    
    // Inside
    fill(heartColour);
    beginShape();
    curveVertex(x + 20, y - 50);
    curveVertex(x + 20, y - 43);
    curveVertex(x - 36, y - 43);
    curveVertex(x - 44, y - 68);
    curveVertex(x -  7, y - 95);
    curveVertex(x + 38, y - 69);
    curveVertex(x, y);
    endShape();
    
    // Pulmonary vein walls
    fill(wallColour);
    beginShape();
    vertex(x +  9, y - 116);
    vertex(x + 25, y - 110);
    vertex(x + 20, y - 95);
    vertex(x +  3, y - 97);
    endShape();

    beginShape();
    vertex(x -  4, y - 116);
    vertex(x - 22, y - 114);
    vertex(x - 20, y - 95);
    vertex(x -  3, y - 97);
    endShape();
    
    // Pulmonary veins
    fill(heartColour);
    beginShape();
    vertex(x + 12, y - 116);
    vertex(x + 23, y - 112);
    vertex(x + 15, y - 88);
    vertex(x +  4, y - 90);
    endShape();

    beginShape();
    vertex(x - 7, y - 116);
    vertex(x - 19, y - 115);
    vertex(x - 16, y - 88);
    vertex(x -  5, y - 90);
    endShape();
};

var drawAorta = function(x, y) {
    // Aorta Outside
    fill(wallColour);
    beginShape();
    curveVertex(x, y + 56);
    curveVertex(x + 2, y + 11);
    curveVertex(x - 61, y - 2);
    curveVertex(x - 100, y - 14);
    curveVertex(x - 128, y - 50);
    curveVertex(x - 132, y - 123);
    curveVertex(x - 101, y - 125);
    curveVertex(x - 96, y - 68);
    curveVertex(x - 80, y - 46);
    curveVertex(x - 52, y - 36);
    curveVertex(x +  7, y - 40);
    curveVertex(x -  20, y - 75);
    endShape();
    
    fill(heartColour);
    beginShape();
    curveVertex(x - 10, y + 27);
    curveVertex(x +  3, y );
    curveVertex(x - 88, y - 15);
    curveVertex(x - 124, y - 54);
    curveVertex(x - 127, y - 125);
    curveVertex(x - 105, y - 127);
    curveVertex(x - 101, y - 72);
    curveVertex(x - 89, y - 47);
    curveVertex(x - 55, y - 31);
    curveVertex(x +  14, y - 34);
    curveVertex(x -  20, y - 92);
    endShape();
};

var draw = function() {
    background(255, 255, 255);
    noStroke();
    
    var vol = 3 * (frameCount % 30) + 40;
    vol = 96;
    
    drawLV(heartX, heartY, vol);
    drawLA(heartX, heartY);
    drawAorta(heartX, heartY);
};
