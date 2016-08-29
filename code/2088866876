/*******************************************************
 * Spacebar = pause
********************************************************/

// Angle around the orbit
var theta = 0;

// Rotation of ellipse
var phi = 20;

// Trigonometric values
var cp = cos(phi);
var sp = sin(phi);

// Axes
var a = 160;
var b = 100;
var major = max(a, b);
var minor = min(a, b);

// Center of ellipse
var cx = 180;
var cy = 240;

// Position of focus
var focus = sqrt(major * major - minor * minor);
var focusX = cx - focus * cos(phi);
var focusY = cy - focus * sin(phi);

// Calculating ellipse properties
var major = max(a, b);
var minor = min(a, b);
var e = focus / major;
var totalArea = PI * a * b;         // pixels ^ 2
var sector = totalArea / 720;       // pixels ^ 2
var standardGravity = 25.6;         // GM in m^3 / s^2
var periodicity = sqrt(a * a * a / standardGravity);    // s
var area;

// The larger this is the more accurate the speed is
var resolution = 10;

// Initial position (angle = 0)
var x = a;
var y = 0;
var r = a + focus;

// Variables for storing previous positions
var oldPoints = [];
var pointInterval = 5;
var oldTime = 0;
var periodTime = false;

// This allows us to pause the simulation
var running = true;

// Colours
var BACKGROUND = color(0, 0, 0);
var ORBITER = color(120, 80, 255, 255);
var ORBITER_T = color(120, 80, 255, 0);

var triangleArea = function(x1, y1, x2, y2, x3, y3) {
    return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2));
};

var t = 0;

var draw = function() {        
    var area = 0;
    if (running) {
        t++;
        
        var k = 360 * a * b / (periodicity * resolution);
        
        for (var i = 0; i < resolution; i++) {
            theta += k / (r * r);
            r = major * (1 - e * e) / (1 - e * cos(theta));   
        }
        
        var x1 = r * cos(theta) - focus;
        var y1 = r * sin(theta);
        var newX = cx + x1 * cp - y1 * sp;
        var newY = cy + x1 * sp + y1 * cp;
        
        area = triangleArea(focusX, focusY, x, y, newX, newY);
        
        x = newX;
        y = newY;
        
        if (theta > 360) {
            theta -= 360;
            if (oldTime) {
                periodTime = t - oldTime;
            }
            oldTime = t;
        }
 
        // Record some points so we can draw them
        if (t % pointInterval === 0) {
            oldPoints.push([x, y]);
            if (oldPoints.length > 360 / pointInterval) {
                oldPoints.shift();
            }
        }
    }
    
    background(BACKGROUND);
    
    // Background ellipse
    fill(lerpColor(ORBITER, ORBITER_T, 0.8));
    translate(cx, cy);
    rotate(phi);
    ellipse(0, 0, a*2, b*2);
    resetMatrix();
    
    // Info
    fill(255);
    textSize(14);
    text("Angle: " + round(10 * (theta % 360)) / 10 + "°", 8, 20);
    text("Eccentricity: " + round(1000 * e)/1000, 8, 40);
    text("Area: " + round(area), 8, 60);
    text("Period: " + round(periodicity), 8, 80);
    
    // Axes
    stroke(100);
    line(0, 200, 400, 200);
    line(200, -0, 200, 400);
    
    // Connecting line
    noFill();
    stroke(250);
    
    line(focusX, focusY, x, y);
    arc(focusX, focusY, 40, 40, phi,
        (180 + atan2(focusY - y, focusX - x)) % 360);
    
    // Foci
    fill(160);
    noStroke();
    ellipse(focusX, focusY, 10, 10);
    ellipse(cx + focus * cos(phi), cy + focus * sin(phi), 10, 10);
    
    // Draw orbiting body
    fill(ORBITER);
    ellipse(x, y, 10, 10);
    
    // Draw previous points
    for (var i=0; i<oldPoints.length; i++) {
        fill(lerpColor(ORBITER_T, ORBITER, i/(oldPoints.length)));
        ellipse(oldPoints[i][0], oldPoints[i][1], 8, 8);
    }
    
};

// Spacebar toggles animation
var keyPressed = function() {
    if (keyCode === 32) { running = !running; }
};