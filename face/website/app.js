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
    GS_pixels = []
    dataArray = imageData.data
    for (var i = 0; i < dataArray.length; i+=4) {
        GS_pixels.push(Math.round(0.3*dataArray[i] + 0.6*dataArray[i+1] + 0.1*dataArray[i+2]))
    }
    grayscale = []
    for (var i = 0; i < GS_pixels.length; i+=500) {
        grayscale.push(GS_pixels.slice(i,i+500))
    }
    updateData("img_data", imageData.data)
  

    var blob1 = new Blob([JSON.stringify(grayscale)], { type: "text/plain;charset=utf-8" });
    var link = document.createElement("a"); // Or maybe get it from the current document
    var blobUrl = URL.createObjectURL(blob1);
    link.href = blobUrl;
    link.download = "imgGS.txt";
    link.innerHTML = "downloadGSarray";
    document.body.appendChild(link); // Or append it whereever you want
    // downloadURI(picture, "pic.png")
}