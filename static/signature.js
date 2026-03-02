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

function secondaryScreen(btnID, canvasID, step1ID, step2ID, form, signature){

    const btnAssinar = document.getElementById(btnID);
    const step1 = document.getElementById(step1ID);
    const step2 = document.getElementById(step2ID);
    const canvas = document.getElementById(canvasID);

    if(btnAssinar){
        btnAssinar.addEventListener("click", function(){

            const name = document.querySelector("input[name='name']").value;

            if(!name){
                alert("Preencha o nome antes de assinar.");
                return;
            }

            step1.style.display = "none";

            step2.style.display = "block";

            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;

            startSignature(canvasID, form, signature)
        })
    };


}