import * as fs from "fs";

const dataPath = 'data/day1.txt'
const rawData = fs.readFileSync(dataPath, 'utf8').split("\n\n")
const splitData = rawData.map((data) => data.split("\n"))

export function part1(): number {
    let totalCalories = []
    for (var i = 0; i < splitData.length; i++) {
        totalCalories.push(splitData[i].map(x=>+x).reduce((a, b) => a + b))
    }

    return Math.max.apply(null, totalCalories)
}

export function part2(): number {
    let totalCalories = []
    for (var i = 0; i < splitData.length; i++) {
        totalCalories.push(splitData[i].map(x=>+x).reduce((a, b) => a + b))
    }
    totalCalories.sort((a, b) => a - b)
    return totalCalories.slice(-3).reduce((a, b) => a+b)
}