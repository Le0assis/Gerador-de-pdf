function startSignature(canvasId, formId, inputHiddenId){
    
    const canvas = document.getElementById(canvasId);
    canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;
    canvas.tabIndex = 0;
    let signaturePad = new SignaturePad(canvas);
    let signatureOn = false;

    canvas.addEventListener("click", function() {
        canvas.focus();
    });

    canvas.addEventListener("focus", function() {
        signatureOn = true;
        canvas.style.border = "2px solid blue";
    });

    canvas.addEventListener("blur", function(e){
        if(signatureOn) {
            setTimeout(() => canvas.focus(), 0)
        }
        signatureOn = false;
        canvas.style.border = "1px solid black";
    });

    canvas.addEventListener("keydown", function(event){

        if (event.code === "Space") {
            event.preventDefault();
            signaturePad.clear();
        }
        if (event.code === "Enter") {
            event.preventDefault();
            canvas.blur();
        }
    })
   
    document.getElementById(formId).addEventListener("submit", function() {

        if (!signaturePad.isEmpty()) {
        const dataURL = signaturePad.toDataURL();
        document.getElementById(inputHiddenId).value = dataURL;
        }
    });


}