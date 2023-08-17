function deleteNote(noteId) {
    fetch("/delete_note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId}),
        headers: {
            'Content-Type': 'application/json'

        } 
    })
        .then(response => {
            if(!response.ok){
                // Not a successful response (e.g. 404 or 500)
                throw new Error('Network response was not ok');
            }
            return response.json(); // this will pass the response to the next then
        })
        .then(data => {
              // Handle successful deletion or any other action you might want to perform
              window.location.href = "/"
        })
        .catch(error =>{
            console.error('There was a problem with the fetch operation:', error.message);
        }); 
}