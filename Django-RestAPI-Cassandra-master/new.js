const urlDecode = 'http://127.0.0.1:8000/image-decodeLeast/'
const urlEncode = 'http://127.0.0.1:8000/image-encode/'
const urlDecodeTwo = 'http://127.0.0.1:8000/image-decodeTwoLeast/'
const urlEncodeDct = 'http://127.0.0.1:8000/image-dct-encode/'
const urlDecodeDct = 'http://127.0.0.1:8000/image-dct-decode/'

const myHeaders = new Headers();
myHeaders.append('Access-Control-Allow-Headers', "*")
myHeaders.append('Access-Control-Allow-Origin', "*")
myHeaders.append('content-type', 'application/json')


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e){
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
          behavior: "smooth"
      });
  });
});

//var data = new FormData();
var base;


const inpFile = document.getElementById("upload")
const previewContainer = document.getElementById("imagePreview")
const previewImage = previewContainer.querySelector(".image-preview-image")
const previewDefaultText = previewContainer.querySelector(".image-preview-default-text")
var psnrText = document.getElementById('psnrText')
var mseText = document.getElementById("mseText")
var decodedText = document.getElementById("stegText")

const inpFile2 = document.getElementById("upload2")
const previewContainer2 = document.getElementById("imagePreview2")
const previewImage2 = previewContainer2.querySelector(".image-preview-image2")
const previewDefaultText2 = previewContainer2.querySelector(".image-preview-default-text2")

const previewContainer3 = document.getElementById("imagePreview3")
const previewImage3 = previewContainer3.querySelector(".image-preview-image3")
const previewDefaultText3 = previewContainer3.querySelector(".image-preview-default-text3")

inpFile2.addEventListener("change", function(){
    const file = this.files[0]
  
    if (file) {
      reader = new FileReader();
  
      previewDefaultText2.style.display = "none";
      previewImage2.style.display = "block";
  
      reader.addEventListener("load", function(){
        base = this.result;
        //data.append('img', JSON.stringify(base))
        console.log(base)
        previewImage2.setAttribute("src", this.result);
      });
  
      reader.readAsDataURL(file);
  
    }else{
  
      previewDefaultText2.style.display = "null";
      previewImage2.style.display = "null";
      previewImage2.setAttribute("src", "");
    }
  
  });

 

inpFile.addEventListener("change", function(){
  const file = this.files[0]

  if (file) {
    reader = new FileReader();

    previewDefaultText.style.display = "none";
    previewImage.style.display = "block";

    reader.addEventListener("load", function(){
      base = this.result;
      //data.append('img', JSON.stringify(base))
      console.log(base)
      previewImage.setAttribute("src", this.result);
    });

    reader.readAsDataURL(file);

  }else{

    previewDefaultText.style.display = "null";
    previewImage.style.display = "null";
    previewImage.setAttribute("src", "");
  }

});



function encode(baseImage, url){
  fetch(url,{
    method: 'POST',
    headers: myHeaders,
    body: baseImage,
  }
  ).then(function (response) {
    // The API call was successful!
    response.json().then(function(response){
      psnrText.innerHTML = response['psnr']
      mseText.innerHTML = response['mse']
      //document.getElementById("psnrText").innerHTML = response['psnr'];
      console.log(response['psnr'])
    });
    

    previewDefaultText3.style.display = "none";
    previewImage3.style.display = "block";
    previewImage3.setAttribute("src", 'afterfoo.png')

  }).catch(function (err) {
    // There was an error
    console.warn('Something went wrong.', err);
  });

}

function decode(baseImage, url){
    fetch(url,{
      method: 'POST',
      headers: myHeaders,
      body: baseImage,
    }
    ).then(function (response) {
      response.json().then(function (response){
          // The API call was successful!
      console.log('success!!!', response.data);
      //hossam = JSON.stringify(response);
      //console.log(response['data']);
      //console.log("this is "+hossam);
      decodedText.innerHTML = response['data']
      });
    }).catch(function (err) {
      // There was an error
      console.warn('Something went wrong.', err);
    });
  }


function onEncodeClicked(){

    var radios = document.getElementsByName("Technique")
    var selected = Array.from(radios).find(radio => radio.checked)

    if(selected.value == "LSB"){
      var stegoText = document.getElementById("stegoText").value;
      var data = JSON.stringify({ "img": base, "text": stegoText}); 
      encode(data, urlEncode);
      previewImageFun();

    }else if(selected.value == "DCT"){

      var stegoText = document.getElementById("stegoText").value;
      var data = JSON.stringify({ "img": base, "text": stegoText}); 
      encode(data, urlEncodeDct);
      previewImageFun();

    }else{

      var stegoText = document.getElementById("stegoText").value;
      var data = JSON.stringify({ "img": base, "text": stegoText}); 
      encode(data, urlEncodeDct);
      previewImageFun();

    }
}

function onDecodeClicked(){

    var radios = document.getElementsByName("TechniqueDec")
    var selected = Array.from(radios).find(radio => radio.checked)

    if(selected.value == "LSB"){

      var data = JSON.stringify({ "img": base,});
      decode(data, urlDecode);

    }else if(selected.value == "DCT"){

      var data = JSON.stringify({ "img": base,});
      decode(data, urlDecodeTwo);

    }else{
      var data = JSON.stringify({ "img": base,});
      decode(data, urlDecodeDct);
    }

}

function previewImageFun(){
  document.getElementsByClassName("image-preview-image3").src="afterfoo.png";
}







