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

function takePic(){
    document.getElementById("canvas").style.display = "block"
    let picture = webcam.snap();
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const arr = new Uint8ClampedArray(187500 * 4);
    let imageData = ctx.getImageData(0 , 0, 375, 500);
    console.log(imageData.data);
    // downloadURI(picture, "pic.png")
}