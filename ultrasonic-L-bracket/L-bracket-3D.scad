standWidth = 15;
standHeight = 4;
standLength = 46;

ultrasonicWidth = 4;
ultrasonicHeight = 21;
ultrasonicLength = 46;
totalUltrasonicHeight = ultrasonicHeight + standHeight;

cube([ultrasonicWidth, ultrasonicLength, totalUltrasonicHeight]);
cube([standWidth, standLength, standHeight]);