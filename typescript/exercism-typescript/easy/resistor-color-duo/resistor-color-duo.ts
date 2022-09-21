//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

let BandValues = {
  black: "0",
  brown: "1",
  red: "2",
  orange: "3",
  yellow: "4",
  green: "5",
  blue: "6",
  violet: "7",
  grey: "8",
  white: "9"
} as const;

export function decodedValue(bands: Array<keyof typeof BandValues>): number {
    return Number(BandValues[bands[0]].concat('', BandValues[bands[1]]));
}

//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 

credits: https://exercism.org/tracks/typescript/exercises/resistor-color-duo/solutions/SleeplessByte
// since the color values are equal to their index values
// there is no need to create an object mapping colors to values

const COLORS = ['black', 'brown', ...]
const colorCode = (color: string): number => COLORS.indexOf(color)
export const decodedValue = ([tens, ones]: string[]): number =>
  colorCode(tens) * 10 + colorCode(ones)

*/
