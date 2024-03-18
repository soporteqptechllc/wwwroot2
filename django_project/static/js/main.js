Dropzone.autoDiscover = false;

const myDropzone = new Dropzone("#my-dropzone",{
    url: "upload/",
    maxFiles: 1,
    maxFilesize: 3,
    addRemoveLinks: true,
    acceptedFiles: '.txt',
    accept: function (file, done) {
        if (file.name != "inventario.txt") {
            done("Borre este archivo por que no es el indicado");
        }
        else { done(); }
    }
})