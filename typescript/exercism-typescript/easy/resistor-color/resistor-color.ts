//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

let ColorValues = {
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

export const colorCode = (color: keyof typeof ColorValues): number => {
  return ColorValues[color]
}

export const COLORS = Object.keys(
  ColorValues) as Array<keyof typeof ColorValues>

//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 


credits: https://exercism.org/tracks/typescript/exercises/resistor-color/solutions/Prasannavk94

export const colorCode = (color: typeof COLORS[number]) =>
  COLORS.indexOf(color);

  export const COLORS = ["black", "brown", ...] as const;

*/