//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

export function twoFer(name?: string): string {
  return `One for ${name ? name : "you"}, one for me.`;
}


//---------------------------------------------//
//           Better Solutions                  //
//---------------------------------------------//
/* 

set the default value of name to 'you' to avoid conditional branching.
export function twoFer(name = "you"): string {
  return `One for ${name}, one for me.`;
}

*/