// 1. 0-11 free
// 2. 12-18 or welfare 75%
// 3. 19-120 full price
// 4. else error

function ticketprice(age, price, welfare = false){
    if (age < 12){
        return 0
    } else if (age < 19 || welfare){
        return price * 0.75
    }   else if (age < 121){
        return price
    }   else {
        return "Error"
    }
}

console.log(ticketprice(77, 100, true))