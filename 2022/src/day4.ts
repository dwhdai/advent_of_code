import * as fs from "fs";

const dataPath = 'data/day4.txt'
const rawData = fs.readFileSync(dataPath, 'utf8').split("\n")

const range = (start, stop, step) =>
  Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + i * step);

export function part1(): number {
    let out = 0
    for (let i = 0; i < rawData.length; i++) {
        let pair = rawData[i].split(",")
        let start1 = Number(pair[0].split("-")[0])
        let end1 = Number(pair[0].split("-")[1])
        let start2 = Number(pair[1].split("-")[0])
        let end2 = Number(pair[1].split("-")[1])
        if (start1 >= start2 && end1 <= end2) {
            out += 1
        } else if (start2 >= start1 && end2 <= end1) {
            out +=1
        }
    }
    return out
}

export function part2(): number {
    let out = 0
    for (let i = 0; i < rawData.length; i++) {
        let pair = rawData[i].split(",") 
        let start1 = Number(pair[0].split("-")[0])
        let end1 = Number(pair[0].split("-")[1])
        let start2 = Number(pair[1].split("-")[0])
        let end2 = Number(pair[1].split("-")[1])
        let set1 = range(start1, end1, 1)
        let set2 = range(start2, end2, 1)
        let intersection = new Set([...set1].filter(x => new Set(set2).has(x)))
        if (intersection.size) {
            out += 1
        }
    }
    return out 
}