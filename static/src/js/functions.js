const getimgs1 = document.getElementById("forma");
const getimgs2 = document.getElementById("finalimg");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
// const get3=getimgs2.value.replace("blob","")

getimgs1.addEventListener("submit", function (e) {
  const csrf2 = csrf[0].value;
  arr2 = [];
  console.log(getimgs2.files);
  for (itema of getimgs2.files) {
    arr2.push(itema);
  }
  var arr3 = "{" + arr2[0] + "}";
  console.log(arr2);
  e.preventDefault();
  // $.ajax({
  //   dataType: "json",
  //   type: "POST",
  //   url: "proccess",
  //   cache: false,
  //   contentType: 'multipart/form-data',
  //   // processData: true,
  //    data: {
  //     csrfmiddlewaretoken: csrf2,
  //     finalimg:(arr2),
  //     'ggg':'sssssssssssssss'
  //   },
  //   success: function (data) {
  //     if (data.errors) {
  //       console.log(data.errors);

  //       // handelAlert2("danger", data.errors);
  //     } else {
  //       console.log(data);
  //       // document.getElementById("addRow").style.display = "block";
  //       // document.getElementById("testsform").style.display="block";

  //       //viewing data to main htmls
  //     }
  //   },
  // });



  const blob =
            new Blob(
                ['arr2'],
                { type: "text/plain" }
            );
            fetch('proccess', {
  
            // HTTP request type
            method: "POST",
  
            // Sending our blob with our request
            body: blob
        })
        .then(response => alert('Blob Uploaded'))
        .catch(err => alert(err));
  
});
