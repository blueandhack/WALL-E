standWidth = 15;
standHeight = 4;
standLength = 50;

ultrasonicWidth = 3;
ultrasonicHeight = 22;
ultrasonicLength = 50;
totalUltrasonicHeight = ultrasonicHeight + standHeight;

difference(){
    cube([ultrasonicWidth, ultrasonicLength, totalUltrasonicHeight]);
    translate([0, 12.5, 11+standHeight]){
        rotate ([90,0,90]) cylinder(ultrasonicWidth,8,8);
    }
    translate([0, 37.5, 11+standHeight]){
        rotate ([90,0,90]) cylinder(ultrasonicWidth,8,8);
    }
    translate([0, 4, 19.5+standHeight]){
        rotate ([90,0,90]) cylinder(ultrasonicWidth,1.5,1.5);
    }
    translate([0, 45.5, 2.5+standHeight]){
        rotate ([90,0,90]) cylinder(ultrasonicWidth,1.5,1.5);
    }
}

difference(){
    cube([standWidth, standLength, standHeight]);
    translate([4, 13.5, 0]){
        difference(){
            cube([7, 23, 2]);
        }
    }
}


difference(){
    translate([0, 48, 0]){
        cube([standWidth, 2, totalUltrasonicHeight]);
    }
    color("Yellow") translate([15, 48, 4]){
        rotate ([0,-30,0]){
            cube([standWidth, 2, totalUltrasonicHeight]);
        }
    }
}

difference(){
    cube([standWidth, 2, totalUltrasonicHeight]);
    color("Yellow") translate([15, 0, 4]){
        rotate ([0,-30,0]){
            cube([standWidth, 2, totalUltrasonicHeight]);
        }
    }
}
