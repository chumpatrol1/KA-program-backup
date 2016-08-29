noStroke();

var drawFish = function(x, y, w, h) {
    // main body
    fill(245, 142, 73);
    ellipse(x, y, w, h);
    
    var getX = function(n) { return x + n * w; };
    var getY = function(n) { return y + n * h; };
    
    var myTriangle = function(x1, y1, x2, y2, x3, y3) {
        triangle(getX(x1), getY(y1), getX(x2), getY(y2), getX(x3), getY(y3));
    };

    // tail
    fill(224, 156, 117);
    myTriangle(-0.3, 0, -1.2, 0.4, -1.2, -0.4);
    
    fill(219, 133, 83);
    myTriangle(-0.3, 0, -0.75, 0.2, -0.75, -0.2);
    
    // midbody
    fill(235, 149, 99);
    myTriangle(-0.7, 0, -0.28, 0.42, -0.28, -0.42);
    
    fill(232, 162, 121);
    myTriangle(-0.7, 0, -0.4, 0.31, -0.4, -0.31);
    
    fill(219, 133, 83);
    myTriangle(-0.7, 0, -0.5, 0.2, -0.5, -0.20);
    
    // fins
    fill(230, 149, 106);
    myTriangle(-0.23, -0.43, -0.66, -0.62, -0.38, -0.08);
    
    fill(219, 133, 83);
    myTriangle(-0.23, -0.43, -0.58, -0.58, -0.36, -0.16);
    
};

var x = 200;

var draw = function() {
    background(150, 221, 242);
    
    x += 2;
    if (x > 600) {
        x -= 650;
    }
    
    var y = 150 + 30 * sin(frameCount * 2);
    var w = 120 + 10 * sin(frameCount * 8);
    var h = 80 + 5 * sin(frameCount * 8 + 90);
    drawFish(x, y, w, h);
};







