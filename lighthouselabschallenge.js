const GRID = [
  ["", "", "", "^", "", "", "", "", "", ""],
  ["", "", "", "", "~", "", "", "", "", ""],
  ["", "", "", "", "^", "^", "", "", "", ""],
  ["", "", "", "", "^", "^", "", "", "", ""],
  ["", "", "", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", "", "", ""],
  ["", "^", "~", "~", "", "", "", "^", "", ""],
  ["", "^", "", "~", "~", "", "", "", "", ""],
  ["", "^", "", "", "~", "~", "", "", "", ""],
];

// helper methods
parseStringCoords = (coords) => ({
  x: coords.charCodeAt(0) - 'A'.charCodeAt(0),
  y: parseInt(coords.substring(1) - 1)
})

toStringCoords = (x, y) => String.fromCharCode('A'.charCodeAt(0) + x) + (y + 1)

// challenges
gridSize = () => GRID[0].length + ' x ' + GRID.length

totalCells = () => GRID[0].length * GRID.length

lightCell = (coords) => {
  const size = gridSize().split(' x ');
  const {x, y} = parseStringCoords(coords);
  
  if (x < 0 || x >= size[0] || y < 0 || y >= size[1]) {
    return false;
  }
  return GRID[y][x];
}

isRock = (coords) => lightCell(coords) === '^' ? true : false

isCurrent = (coords) => lightCell(coords) === '~' ? true : false

lightRow = (yVal) => GRID[yVal - 1]

lightColumn = (xVal) => {
  const x = xVal.charCodeAt(0) - 'A'.charCodeAt(0);
  return GRID.map(row => row[x]);
}

isSafe = (coords) => !isRock(coords) && !isCurrent(coords)

allRocks = () => {
  return GRID.reduce((acc, row, yVal) => {
    let transformedRow = row.reduce((acc, cell, xVal) => {
      if (cell === "^") {
        return acc.concat(toStringCoords(xVal, yVal));
      }
      return acc;
    }, []);
    return acc.concat(transformedRow);
  }, []);
}

allCurrents = () => {
  return GRID.reduce((acc, row, yVal) => {
    let transformedRow = row.reduce((acc, cell, xVal) => {
      if (cell === "~") {
        return acc.concat(toStringCoords(xVal, yVal));
      }
      return acc;
    }, []);
    return acc.concat(transformedRow);
  }, []);
}

firstRock = () => allRocks()[0]

firstCurrent = () => allCurrents()[0]

move = (coords, xVal, yVal) => {
  let {x, y} = parseStringCoords(coords);
  
  x += xVal;
  y += yVal;
  
  return toStringCoords(x, y);
}

isDangerous = (coords) => !isSafe(coords) ? true :
    (!isSafe(move(coords, -1, 0)) || !isSafe(move(coords, 1, 0)) || !isSafe(move(coords, 0, -1)) || !isSafe(move(coords, 0, 1))) ? true 
      : false

distressBeacon = (coords) => {
  for (let i = -1; i <= 1; i++) {
    for (let j = -1; j <= 1; j++) {
      if (i === 0 && j === 0) { 
        continue;
      }
      const target = move(coords, i, j);
      if (isSafe(target)) {
        return target;
      }
    }
  }
}

setRock = (coords) => {
  const {x, y} = parseStringCoords(coords);
  GRID[y][x] = '^';
}

setRock('J9');

percentageReport = () => [totalCells() - allRocks().length - allCurrents().length, allRocks().length, allCurrents().length]

safetyReport = () => {
  var numOfSafeCells = GRID.reduce((acc, row) => {
    return acc + row.reduce((acc, cell) => {
      return acc + (cell === "" ? 1 : 0);
      }, 0)
    }, 0);
  return (numOfSafeCells / totalCells() * 100).toFixed(1)  + "%";
}

calcDistance = (coord1, coord2) => {
  const {x: x1, y: y1} = parseStringCoords(coord1);
  const {x: x2, y: y2} = parseStringCoords(coord2);
  return (Math.sqrt((x2 - x1)**2 + (y2 - y1)**2)).toFixed(2);
}

evaluateRoute = (coords) => {
  let currentCount = 0;
  for (let i = 0; i < coords.length; i++) {
    if (isRock(coords[i])) {
      return false;
    }
    if (isCurrent(coords[i])) {
      currentCount++;
      if (currentCount >= 2) {
        return false;
      }
    }
  }
  return true;
}