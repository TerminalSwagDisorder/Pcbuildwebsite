fetch('http://localhost:8001/pcbuildapp-1170c5b/case')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(JSON.stringify(myJson));
  });
