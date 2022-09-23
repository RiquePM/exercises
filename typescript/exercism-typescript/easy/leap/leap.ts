//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

export function isLeap(year: number): boolean {
  let isDivisableBy4: boolean = year%4 === 0 ? true : false; 
  let isDivisableBy100: boolean = year%100 === 0 ? true : false;
  let isDivisableBy400: boolean = year%400 === 0 ? true : false;

  if (!isDivisableBy4) {
    return false;
  }
  else if (!isDivisableBy100) {
    return true;
  }
  else if (!isDivisableBy400) {
    return false
  }
  else {
    return true
  }
}


//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 
credit: https://exercism.org/tracks/typescript/exercises/leap/solutions/chris-ianson

export function isLeap(year: number):boolean {
  
  // Ternary operator in my solution is not necessary
  // since the expression always evaluates to a boolean
  const divisibleBy4: boolean = year %4 === 0;
  const divisibleBy100: boolean = year %100 === 0;
  const divisibleBy400: boolean = year %400 === 0;
  
  return (divisibleBy4 && !divisibleBy100) || (divisibleBy4 && divisibleBy100 && divisibleBy400);
}


credits: https://exercism.org/tracks/typescript/exercises/leap/solutions/jdehaan

export function isLeap(year: number): boolean {
    
  // eliminate conditional statements and variable declarations
  return ((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0)
}

*/