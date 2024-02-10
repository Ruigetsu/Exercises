function Car(color, mark, model, cost) {
    return {
        color: color,
        mark: mark,
        model: model,
        cost: cost
    } 
}
let mycar = Car("Blue", "Mercedes",  "S-Class", 150000)
console.log(`My car is ${mycar.color} ${mycar.mark} ${mycar.model}, and it costs around ${mycar.cost}`)
for (let i in mycar) {
    console.log(mycar[i])
}