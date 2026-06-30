fetch('http://127.0.0.1:5000/events')
.then(response => {return response.json()})
.then(events => displayEvents(events))

function displayEvents(events){
    // console.log(events)
    eventList=document.querySelector('#event-list')
    for(const event of events){
        eventList.innerHTML += `<li>${event.title}</li>`
    }
}

function addEvent(){
    eventForm = document.querySelector('form')
    eventForm.addEventListener('submit', (event) => {
        event.preventDefault()
        eventTitle = event.target.elements['title'].value

    fetch('http://127.0.0.1:5000/events',{
        method: 'POST',
        headers: {
            "Content-Type" : "application/json",
            "accept":"application/json"
        },
        body: JSON.stringify({title:eventTitle})
    })
    .then(response => {return response.json()})
    .then(newEvent => console.log(newEvent))
    })
}

addEvent()