
var inputs = readline().split(' ');
const W = parseInt(inputs[0]); // width of the building.
const H = parseInt(inputs[1]); // height of the building.
const N = parseInt(readline()); // maximum number of turns before game over.
var inputs = readline().split(' ');
var x0 = parseInt(inputs[0]);
var y0 = parseInt(inputs[1]);

var lowestY = 0;
var lowestX = 0;
var highestY = H;
var highestX = W;

// game loop
while (true) {
    const bombDir = readline(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    switch(bombDir[0]) {
        case 'D': lowestY = y0 + 1; break;
        case 'U': highestY = y0 - 1; break;
        case 'L': highestX = x0 - 1; break;
        case 'R': lowestX = x0 + 1; break;
    }
    switch(bombDir[1]) {
        case 'L': highestX = x0 - 1; break;
        case 'R': lowestX = x0 + 1; break;
    }

    x0 = Math.floor((highestX + lowestX) / 2);
    y0 = Math.floor((highestY + lowestY) / 2);

    console.log(x0, y0);

}
