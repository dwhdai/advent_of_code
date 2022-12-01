import * as fs from "fs";

const dataPath = 'data/day1.txt'
const rawData = fs.readFileSync(dataPath, 'utf8').split("\n\n")
const splitData = rawData.map((data) => data.split("\n"))
let formattedData = []
for (var i = 0; i < splitData.length; i++) {
    // console.log(i, split_data[i])
    formattedData.push(splitData[i].map(x=>+x))
}

console.log(formattedData)

export function run(d: number[]): number {
    return d[0]
}