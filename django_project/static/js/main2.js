Dropzone.autoDiscover = false;

const myDropzone2 = new Dropzone("#my-dropzone2",{
    url: "upload2/",
    //uploadMultiple: true,
    //thumbnailWidth: 1000,
    //thumbnailHeight: 750,
    //thumbnailMethod: 'crop',
    maxFiles: 20,
    maxFilesize: 3,
    addRemoveLinks: true,
    //acceptedFiles: 'imagen / .jpeg, imagen / .png, imagen / .jpg',
    //acceptedFiles: 'image/*',
    acceptedFiles: '.jpg, .jpeg, .png',
    
})