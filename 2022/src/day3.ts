import * as fs from "fs";

const dataPath = 'data/day3.txt'
const rawData = fs.readFileSync(dataPath, 'utf8').split("\n")

let alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

export function part1(): number {
    let prioritySum = 0
    for (let i = 0; i < rawData.length; i++) {
        let firstHalf = rawData[i].substring(0, rawData[i].length / 2)
        let secondHalf = rawData[i].substring(rawData[i].length / 2, rawData[i].length)
        let intersection = firstHalf.split("").filter((x) => secondHalf.includes(x))
        prioritySum += alphabet.indexOf(intersection[0]) + 1
    }
    return prioritySum
}

export function part2(): number {
    let prioritySum = 0

    for (let i = 0; i < rawData.length - 2; i = i + 3) {
        let group = rawData.slice(i, i + 3)
        let firstElf = group[0].split("")
        let secondElf = group[1].split("")
        let thirdElf = group[2].split("")
        let intersection = firstElf.filter((x) => secondElf.includes(x)).filter((x) => thirdElf.includes(x))
        prioritySum += alphabet.indexOf(intersection[0]) + 1
    }
    return prioritySum
}
