import * as fs from "fs";

const rawData = fs.readFileSync("data/day2.txt", 'utf8').split("\n")

interface Round {
    // the actions taken by opponent/self during a single round
    opponent: string,
    self: string
}

enum OutcomeScores {
    "lose" = 0,
    "draw" = 3,
    "win" = 6
}

enum OutcomeScores2 {
    "X" = 0,
    "Y" = 3,
    "Z" = 6
}

enum ShapeScores {
    "X" = 1,
    "Y" = 2,
    "Z" = 3
}

const opponentToSelfAction = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

const selfToOpponentAction = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

const win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

const loss = {
    "C": "Y",
    "A": "Z",
    "B": "X"
}

function processData(rawData: string[]): Round[] {
    const processedData = []
    for (let i = 0; i < rawData.length; i++) {
        let opponent = rawData[i].slice(0, 1)
        let self = rawData[i].slice(-1)
        processedData.push({ opponent, self })
    }
    return processedData
}

function winLoseDraw(round: Round): string {
    if (opponentToSelfAction[round.opponent] == round.self) {
        return "draw"
    } else if (win[round.opponent] == round.self) {
        return "win"
    } else {
        return "lose"
    }
}

function shapeFromOutcome(round: Round): string {
    switch (round.self) {
        case "Z":
            return win[round.opponent];
        case "Y":
            return opponentToSelfAction[round.opponent];
        default:
            return loss[round.opponent];
    }
}

export function part1() {
    const processedData = processData(rawData)
    let outcomeScore = 0;
    let shapeScore = 0;
    let totalScore = 0;
    for (let i = 0; i < processedData.length; i++) {
        let currentRound = processedData[i]
        outcomeScore = OutcomeScores[winLoseDraw(currentRound)];
        shapeScore = ShapeScores[currentRound.self];
        totalScore += outcomeScore + shapeScore;
    }
    return totalScore
}

export function part2() {
    const processedData = processData(rawData)
    let outcomeScore = 0;
    let shapeScore = 0;
    let totalScore = 0;
    for (let i = 0; i < processedData.length; i++) {
        let currentRound = processedData[i]
        outcomeScore = OutcomeScores2[currentRound.self];
        shapeScore = ShapeScores[shapeFromOutcome(currentRound)];
        totalScore += outcomeScore + shapeScore;
    }
    return totalScore
}