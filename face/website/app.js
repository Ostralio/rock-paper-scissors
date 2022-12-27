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
    takePic();
})

var paper = document.getElementById("paper")
document.getElementById("paper").addEventListener("click", () => {
    takePic();
})

var scissors = document.getElementById("scissors")
document.getElementById("scissors").addEventListener("click", () => {
    takePic();
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

function send_data(url, arr) {
    let xhr = new XMLHttpRequest;
    xhr.open("POST", url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
        console.log(xhr.responseText); // responseText will be return from API call
    }};

    xhr.send(arr)
}

function takePic(){
    document.getElementById("canvas").style.display = "block"
    let picture = webcam.snap();
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let imageData = ctx.getImageData(0 , 0, 500, 375);
    grayscale = grayscale_array(imageData.data);
    
    var grayscaleBlob = new Blob([JSON.stringify(grayscale)], { type: "text/plain;charset=utf-8" });

    send_data('http://127.0.0.1:5000/face_data', grayscaleBlob);
    // var link = document.createElement("a"); // Or maybe get it from the current document
    // var blobUrl = URL.createObjectURL(grayscaleBlob);
    // link.href = blobUrl;
    // link.download = "imgGS.txt";
    // link.innerHTML = "downloadGSarray";

    // saveAs(grayscaleBlob, "imgdata.txt");
    // document.body.appendChild(link);
}