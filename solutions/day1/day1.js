function dayOne(input){
    const answers = []
    const puzzle = input.split('\n').map(n => parseInt(n))
    
    potentialNums = new Set()
    // puzzle.forEach(num => {
    //     let target = 2020 - num
    //     if (potentialNums.has(target)){
    //         answers.push(target * num)
    //     } else {
    //         potentialNums.add(num)
    //     }
    // })

    for (let i = 0; i < puzzle.length; i++){
        let target  = 2020 - puzzle[i]
        if (potentialNums.has(target)){
            answers.push(target*puzzle[i])
            break
        } else {
            potentialNums.add(puzzle[i])
        }
    }

    for (let i = 0; i < puzzle.length; i++){
        for (let j = i+1; j < puzzle.length; j++){
            for (let k = j+1; k < puzzle.length; k++){
                let total = puzzle[i] + puzzle[j] + puzzle[k]
                if (total === 2020){
                    answers.push(puzzle[i] * puzzle[j] * puzzle[k])
                    return answers
                }
            }
        }
    }

}

const input = `1721
979
366
299
675
1456`

console.log(dayOne(input))