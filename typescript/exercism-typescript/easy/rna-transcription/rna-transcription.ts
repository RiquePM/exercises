//---------------------------------------------//
//                My Solution                  //
//---------------------------------------------//

let BandValues = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
} as any;

export function toRna(dnaStrand: string): string {
  
  if (/[^GCTA]/.test(dnaStrand)) {
    throw new Error('Invalid input DNA.');
  }
  else {
    return dnaStrand.replace(/G|C|T|A/g, (match: string) => (BandValues[match]));
  }  

}

//---------------------------------------------//
//          Other/Better Solutions             //
//---------------------------------------------//
/* 

credits: https://exercism.org/tracks/typescript/exercises/rna-transcription/solutions/CharCampbell

// More functional approach, plus eliminates the use of regex or if statements
// and is type safe since does not make use of type "any"
const dnaToRnaMapping: Map<string, string> = new Map<string, string>([
    ['G', 'C'],
    ['C', 'G'],
    ['T', 'A'],
    ['A', 'U']
])

const invalidDnaError = () => {
    throw Error('Invalid input DNA.')
}

export function toRna(dna: string): string {
    return [...dna].map(char => dnaToRnaMapping.get(char) || invalidDnaError()).join('')
}

*/