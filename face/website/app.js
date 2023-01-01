var choice = "rock"
const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');

const webcam = new Webcam(webcamElement, 'user', canvasElement);

webcam.start()
   .then(result =>{
      console.log("webcam started");
   })
   .catch(err => {
       console.log(err);
   });

var rock = document.getElementById("rock")
document.getElementById("rock").addEventListener("click", () => {
    takePic(0);
})

var paper = document.getElementById("paper")
document.getElementById("paper").addEventListener("click", () => {
    takePic(1);
})

var scissors = document.getElementById("scissors")
document.getElementById("scissors").addEventListener("click", () => {
    takePic(2);
})

function downloadURI(uri, name) {
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    link.click();
}

function updateData(id, data) {
    document.getElementById(id).innerHTML = data
}

function grayscale_array(arr) {
    GS_pixels = [];
    for (var i = 0; i < arr.length; i+=4) {
        GS_pixels.push(Math.round(0.3*arr[i] + 0.6*arr[i+1] + 0.1*arr[i+2]))}
    grayscale = [];
    for (var i = 0; i < GS_pixels.length; i+=500) {
        grayscale.push(GS_pixels.slice(i,i+500));
    }
    return grayscale
}

function displayResult(pred){
    displayText = "fr you gotta be a " + pred + " kinda guy/gal"
    console.log(displayText)
    document.getElementById("predictionDisplay").innerHTML = displayText; 
}

function send_data(url, arr) {
    let xhr = new XMLHttpRequest;
    xhr.open("POST", url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        displayResult(xhr.responseText);
    }};
    
    xhr.send(arr);
    return xhr.responseText;
}

function takePic(choice){
    document.getElementById("canvas").style.display = "block"
    let picture = webcam.snap();
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let imageData = ctx.getImageData(0 , 0, 500, 375);
    output = {'img': grayscale_array(imageData.data), 'choice': choice};
    
    var outputBlob = new Blob([JSON.stringify(output)], { type: "text/plain;charset=utf-8" });
    pred = send_data('http://127.0.0.1:5000/face_data', outputBlob);
    // document.getElementsByClassName("hide").classList.remove("hide");
}

// let myPromise = new Promise(function(pred) {
//     pred()
// });

// myPromise.then(
//     displayText = "fr you gotta be a " + pred + " kinda guy/gal",
//     console.log(displayText),
//     document.getElementById("predictionDisplay").innerHTML = displayText,
// );