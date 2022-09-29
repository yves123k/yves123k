
    var Element = document.getElementById('id_banner_user');
    var img = document.getElementById("banner_preview");
    Element.addEventListener('change', function() {
      var url = URL.createObjectURL(Element.files[0]);
      img.src = url;
      console.log(url);
    //   var d=document.querySelector(".p");
    //   d.textContent+=url;
});
