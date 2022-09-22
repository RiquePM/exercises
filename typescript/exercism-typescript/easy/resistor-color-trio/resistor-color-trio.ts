//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

let BandValues = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9
} as const;

export function decodedResistorValue(bands: Array<keyof typeof BandValues>): string  {
  
  let powOfTen: number = Math.pow(10, BandValues[bands[2]])
  
  let resistanceValue: number = (
    ((BandValues[bands[0]] * 10) + BandValues[bands[1]]) * powOfTen
  ) 

  return resistanceValue < 1000 ? 
    `${resistanceValue.toString()} ohms` : 
    `${(resistanceValue/1000).toString()} kiloohms`;
}

//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 

*/