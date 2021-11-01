// selecting all required elements
const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input");


let file; // global variable

button.onclick = ()=>{
  input.click();
}

input.addEventListener("change", function(){
  file = this.files[0];
  showFile();
  dropArea.classList.add("active");
});



//If user Drag file over drop Area
dropArea.addEventListener("dragover", (event)=>{
  event.preventDefault(); //preventing from default behaviour
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

//If user leave dragged file from Drop area
dropArea.addEventListener("dragleave", ()=>{
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});

//If user drop file on drop area
dropArea.addEventListener("drop", (event)=>{
  event.preventDefault();
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = event.dataTransfer.files[0];
  showFile();
});

function showFile() {
  let fileType = file.type;
  

  let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; // adding some valid image extensions in an array
  if(validExtensions.includes(fileType)) {
    let fileReader = new FileReader();
    fileReader.onload = ()=>{
      let fileURL = fileReader.result;
      console.log(fileURL);
      let imgTag = `<img src="${fileURL}" alt="">`;
      dropArea.innerHTML = imgTag;
    }
    fileReader.readAsDataURL(file);
  }else {
    alert("This is not and Image File!")
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}