noStroke();
var generator = new Random(1);
var stdev = 30;

var mouseClicked = function() {
    var c = constrain(160 + 30 * generator.nextGaussian(), 0, 255);
    fill(c, 0, 0);
    
    for (var i = 0; i < random(80, 100); i++) {
        var x = mouseX + stdev * generator.nextGaussian();
        var y = mouseY + stdev * generator.nextGaussian();
        var d = dist(mouseX, mouseY, x, y);
        var a = atan2(mouseY - y, mouseX - x);
        var p = d / (d + 30);
        var r = 30 * (1 - p);
        
        //fill(100 + 155 * p, 0, 0);
        
        translate(x, y);
        rotate(a);
        ellipse(0, 0, r, r * (1 - d / (d + 120)));
        resetMatrix();
    }
};
