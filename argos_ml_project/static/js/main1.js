Dropzone.autoDiscover = false;

const myDropzone1 = new Dropzone("#my-dropzone1",{
    url: "upload1/",
    maxFiles: 1,
    maxFilesize: 3,
    addRemoveLinks: true,
    acceptedFiles: '.xlsx',
    accept: function (file, done) {
        if (file.name != "REPUESTO POR AREAS.xlsx") {
            done("Borre este archivo por que no es el indicado");
        }
        else { done(); }
    }
})