var ex,ey;

var world = [
    [[3,3,3,3,3,3,1,],
    [3,0,0,0,0,0,0,],
    [3,0,0,0,0,0,0,],
    [3,0,0,0,0,0,0,],
    [3,0,0,0,0,0,0,],
    [3,0,0,0,0,0,0,],
    [3,0,0,0,0,0,0,],
    [3,3,3,3,3,3,3,]],
    
    [[0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [1,0,1,0,1,0,1,]],
    
    [[0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,],
    [0,3,0,0,0,0,0,],
    [2,3,0,0,0,1,0,],
    [1,1,0,1,0,1,1,]],
    
    [[3,3,3,3,3,3,3,],
    [1,0,0,0,0,0,3,],
    [1,0,0,0,0,0,3,],
    [1,0,0,0,0,0,3,],
    [1,0,0,0,0,0,3,],
    [1,0,0,0,0,0,3,],
    [1,0,0,0,0,0,3,],
    [1,1,1,1,1,1,1,]],
    ];

var lengthZ = world.length;
var lengthY = world[0].length;
var lengthX = world[0][0].length;

var X3D = function(x, z, d) {
    return x * d - lengthX * 10 + ex * (z * d - lengthZ * 10);
};

var Y3D = function(y, z, d){
    return y * d - lengthY * 10 + ey * (z * d - lengthZ * 10);
};

var drawQuad = function(x, y, z, d, p) {
    quad(X3D(x + p[0][0], z + p[0][1], d), Y3D(y + p[0][2], z + p[0][3], d),
         X3D(x + p[1][0], z + p[1][1], d), Y3D(y + p[1][2], z + p[1][3], d),
         X3D(x + p[2][0], z + p[2][1], d), Y3D(y + p[2][2], z + p[2][3], d),
         X3D(x + p[3][0], z + p[3][1], d), Y3D(y + p[3][2], z + p[3][3], d));
};

var drawTop = function(x, y, z, d) {
    rect(X3D(x, z, 20), Y3D(y, z, 20), 20, 20);
};

var hight = 2.8;

var posX = 130, posY = 130, posZ = 60;
var posA = floor(posZ / (20 * hight));
var posB = floor(posY / 20);
var posC = floor(posX / 20);

var rotation = 45;
var fixedPos = 45;

var drawBlock = function(x, y, z){
    if (!world[z][y][x]) { 
        // Player
        if (posA + 1 === z && posB === y && posC === x) {
            fill(0, 0, 0, 60);
            ellipse(X3D(posX, posZ, 1), Y3D(posY, posZ, 1), 20, 20);
            
            strokeWeight(3);
            stroke(155, 0, 0);
            fill(255, 0, 0);
            for (var i = 0; i < 10; i++){
                ellipse(X3D(posX, posZ - i, 1), Y3D(posY, posZ - i, 1), 10, 10);
            }
            noStroke();
        }
        return;
    }
    
    var colors;
    if (world[z][y][x] === 2) {
        colors = [
            color(220 + sin(frameCount) * 45, 205 + sin(frameCount) * 50, 50 + sin(frameCount) * 100),
            color(225 + sin(frameCount) * 30, 220 + sin(frameCount) * 45, 100 + sin(frameCount) * 100),
            color(255, 255, 128 + sin(frameCount) * 127)
        ];
    } else {
        colors = [color(150), color(175), color(225)];
    }

    fill(colors[0]);
    if (cos(rotation) < 0) {
        drawQuad(x, y, z, 20, [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 1]]);
    } else {
        drawQuad(x, y, z, 20, [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1]]);
    }
    
    fill(colors[1]);
    if (sin(rotation) < 0){
        drawQuad(x, y, z, 20, [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 1], [0, 1, 0, 1]]);
    } else {
        drawQuad(x, y, z, 20, [[1, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 1, 0, 1]]);
    }
    
    fill(colors[2]);
    drawTop(x, y, z, 20);

    // Add path
    if (world[z][y][x] === 3) {
        fill(0, 255, 255, sin(frameCount * 10) * 50 + 50);
        ellipse(X3D(x + 0.5, z, 20), Y3D(y + 0.5, z, 20), 10, 10);
    }
};

var drawRow = function(rotX, lengthX, y, z) {
    if (rotX) {
        for (var x = 0; x < lengthX; x++) {
            drawBlock(x, y, z);
        }
    } else {
        for(var x = lengthX - 1; x >= 0; x--){
            drawBlock(x, y, z);
        }
    }
};

draw = function() {
    // Update rotation
    rotation += (fixedPos - rotation) / 5;
    ex = sin(rotation)*hight;
    ey = cos(rotation)*hight;
    
    // Background
    noStroke();
    background(0, 100, 125);
    for (var i = 0; i < 40; i++){
        fill(0, 0, 0, i * 4);
        rect(0, i * 10, 400, 10);
    }
    
    pushMatrix();
    translate(200,200);
    scale(1,0.5);
    rotate(rotation);
    
    var rotY = cos(rotation) > 0;
    var rotX = sin(rotation) > 0;
    
    for (var z = lengthZ - 1; z >= 0; z--) {
        if (rotY){
            for (var y = 0; y < lengthY; y++) {
                drawRow(rotX, lengthX, y, z);
            }
        } else {
            for (var y = lengthY - 1; y >= 0; y--) {
                drawRow(rotX, lengthX, y, z);
            }
        }
    }
    popMatrix();
    
    fill(255);
    text("Rotation: " + round(rotation % 360), 20, 20);
    
    // Arrows
    strokeWeight(10);
    stroke(255, 255, 255, 128 + sin(frameCount) * 127);
    noFill();
    
    beginShape();
    vertex(100, 100);
    vertex(20, 200);
    vertex(100, 300);
    endShape();
    
    beginShape();
    vertex(300, 100);
    vertex(380, 200);
    vertex(300, 300);
    endShape();
};

mouseClicked = function(){
    if (mouseX < 200) {
        fixedPos -= 90;
    } else {
        fixedPos += 90;
    }
};
