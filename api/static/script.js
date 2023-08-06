function handleDrop(e) {
    e.preventDefault();
    let file = e.dataTransfer.files[0];
    if (file) {
        console.log("Image Drop successful\n");
        displayImage(file);
        uploadImage(file);
    }
}

function displayImage(file) {
    const reader = new FileReader();
    reader.onload = function(event) {
        const imgPreview = document.getElementById('image-preview');
        imgPreview.src = event.target.result;
        imgPreview.style.display = 'block';
        const dropText = document.getElementById('drop-text');
        dropText.style.display = 'none';
    };
    reader.readAsDataURL(file);
}

function preventDefault(e) {
    e.preventDefault();
}

function uploadImage(file) {
    let formData = new FormData();
    formData.append('image', file);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/classify', true);
    xhr.onload = function() {
        console.log("In the function");
        if (xhr.status === 200) {
            console.log("Finding Result...");
            let result = JSON.parse(xhr.responseText);
            console.log(result);
            displayClassificationResult(result);
        }
    };
    xhr.send(formData);
}

function displayClassificationResult(result) {
    console.log("Classification Successfull");
    let resultElement = document.getElementById('classification-result');
    resultElement.innerHTML = `
        <h2>Classification Result:</h2>
        <p>Predicted class: ${result.class}</p>
        <p>Confidence: ${result.confidence}</p>
    `;
}