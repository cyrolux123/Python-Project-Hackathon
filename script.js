



document.addEventListener('DOMContentLoaded', function () {
    // Make an AJAX request to the Flask API endpoint
    fetch('http://127.0.0.1:5000/api/data')
        .then(response => response.json())
        .then(data => {
            // Update the DOM with the received data
            document.getElementById('data-container').innerHTML = JSON.stringify(data);
            console.log(data.detected);
            console.log(data.simScore);
            console.log(data.aiDecisions)
            const upload = document.getElementsByClassName("updata");
            upload[0].addEventListener("click", () => {
                let cardParent = document.querySelector(".card");
                if (data.detected) {
                    let cardContainer = document.createElement("div");
                result = "Since the result is true, Plagiarism is detected.";
                    cardContainer.innerHTML = `
        <div class="card mx-auto" style="width: 18rem">
        <ul class="list-group list-group-flush">
        <li class="list-group-item">${result}</li>
        <li class="list-group-item">similarity : ${data.simScore}</li>
        <li class="list-group-item">${data.aiDecisions}</li>
      </ul>
      </div>
        `
                    cardParent.appendChild(cardContainer);
                }
                else{
                    let cardParent = document.querySelector(".card");
                   
                        let cardContainer = document.createElement("div");
                    result = "Since the result is False, Plagiarism is not detected.";
                        cardContainer.innerHTML = `
            <div class="card mx-auto" style="width: 18rem">
            <ul class="list-group list-group-flush">
            <li class="list-group-item">${result}</li>
            <li class="list-group-item">similarity : ${data.simScore}</li>
            <li class="list-group-item">${data.aiDecisions}</li>
          </ul>
          </div>
            `
                        cardParent.appendChild(cardContainer);
                };


            })
        })
        .catch(error => console.error('Error:', error));
});

