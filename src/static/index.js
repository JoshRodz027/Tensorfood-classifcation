function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.readAsDataURL(input.files[0]);
      reader.onload = function(e) {
        //Initiate the JavaScript Image object.
        var image = new Image();
        //Set the Base64 string return from FileReader as source.
        image.src = e.target.result;
        //Validate the File Height and Width.
        image.onload = function() {
          $('#uploaded_img')
              .attr('src', e.target.result)
              .width(320)
              .height(320);
          $("form").submit()
        };
      };
    }
  }