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

function paper(){
    choice = "paper"
    takePic()
}

function scissors(){
    choice = "scissors"
    takePic()
}

function downloadURI(uri, name) {
    var link = document.createElement("a");
    link.download = name;
    link.href = uri;
    link.click();
}

function takePic(){
    document.getElementById("canvas").style.display = "block"
    let picture = webcam.snap();
    downloadURI(picture, "pic.png")
}