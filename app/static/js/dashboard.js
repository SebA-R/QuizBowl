document.addEventListener('DOMContentLoaded', (event) => {
    const base_url = 'https://www.qbreader.org/api/';
    const buzzBtn = document.getElementById('buzz-btn');
    let globalData;
    let isPaused = false;
    let isLocked = false;
    let text;
    let container;
    let i;

    const modal = document.getElementById("myModal");
    const openModalBtn = document.getElementById("open-modal-btn");
    const span = document.getElementsByClassName("close")[0];

    openModalBtn.onclick = function () {
        modal.style.display = "block";
    }

    span.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    function typeWriter() {
        if (i < text.length && !isPaused) {
            container.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, 50);
        }
    }

    

    document.getElementById('get-btn').addEventListener('click', function () {
        isLocked = false;

        
        fetch('/api/random-tossup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                difficulties: document.getElementById('difficulty').value,
                categories: document.getElementById('category').value,
                minYear: document.getElementById('minYear').value,
                maxYear: document.getElementById('maxYear').value,
            })
        }).then(response => response.json())
            .then(data => {
                globalData = data;

                document.getElementById('pause-btn').style.display = 'inline-block';
                document.getElementById('buzz-btn').style.display = 'inline-block';
                buzzBtn.disabled = false;

                text = data.tossups[0].question;
                container = document.getElementById('question-section');
                i = 0;
                container.innerText = '';
                document.getElementById('answer-section').innerHTML = '';
                isPaused = false;

                typeWriter();
            })
            .catch(error => {
                console.error('Error querying database:', error);
            });
    });

    document.getElementById('pause-btn').addEventListener('click', function () {
        isPaused = !isPaused;
        if (!isPaused) {
            typeWriter();
        }
    });

    document.getElementById('buzz-btn').addEventListener('click', function () {
        isPaused = true;
        isLocked = true;

        const answerSection = document.getElementById('answer-section');
        answerSection.style.display = 'block';

        let userAnswer = prompt("Please enter your answer:");

        fetch('/api/check-answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                answerline: globalData.tossups[0].formatted_answer,
                answer: userAnswer,
            }),
        })
        .then(response => response.json())
        .then(data => {
            answerSection.innerHTML = (data.correct ? "Correct!" : "Incorrect.")+" The correct answer was "+ globalData.tossups[0].formatted_answer;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
    buzzBtn.disabled = true;
});