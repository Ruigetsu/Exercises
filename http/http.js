let a = XMLHttpRequest()
a.open("GET" , "https://github.com/Ruigetsu")
a.responeType  = 'json'

try {
    a.send()
    if (a.status == 200) {
        console.log(`${a.response}`)
    } else {
        console.log(`Ошибка ${a.status}: ${a.statusText}`)
    }
} catch(err) {
    console.log("Запрос не удался")
}


let b = new FormData()
b.append("name", "Jhon")

a.upload.onprogress = function(event) {
    console.log(`Отправлено ${event.loaded} из ${event.total}`)
}
a.open("POST", "https://github.com/Ruigetsu")
a.send(b)