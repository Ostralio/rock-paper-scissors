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

function takePic(){
    document.getElementById("canvas").style.display = "block"
    let picture = webcam.snap();
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let imageData = ctx.getImageData(0 , 0, 500, 375);
    rgbArray = []
    dataArray = imageData.data
    for (var i = 0; i < dataArray.length; i+=4) {
        rgbArray.push([dataArray[i], dataArray[i+1], dataArray[i+2]])
    }
    updateData("img_data", imageData.data)
    var normalArray = Array.prototype.slice.call(imageData.data);
    var blob1 = new Blob([JSON.stringify(rgbArray)], { type: "text/plain;charset=utf-8" });
    var link = document.createElement("a"); // Or maybe get it from the current document
    var blobUrl = URL.createObjectURL(blob1);
    link.href = blobUrl;
    link.download = "imgData.txt";
    link.innerHTML = "downloadRGBarray";
    document.body.appendChild(link); // Or append it whereever you want
    // downloadURI(picture, "pic.png")
}