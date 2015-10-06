

agenvidaApp.controller('PhoneListCtrl', ['$scope', '$http',
  

  function ($scope, $http ) {

      $scope.getPropositos = function() { 

    

      $http.get('/propositos2/').then(function(result){
                                                        $scope.propositos = result.data;
                                                        },
                                        function(){ } 
                                     );

                              }


    console.log("hola");

  //  $scope.dominio = "http://localhost:8000/";
    $scope.dominio = "http://agenvida.herokuapp.com/";

    $scope.username = "rodrigo";
    $scope.password = "hola09";

  // $scope.TokenLocal = "DbSojNBpAXDEQ3CARcrKOpWI3PS8mkI3osJL0jdd";
    $scope.TokenHeroku = "QlLwYhQoeYx98FzV40a82amX9Ik3HjGtfPNlXHqN";//ClienTID

    console.log("client_id="+$scope.TokenHeroku +"&grant_type=password&username="+$scope.username+"&password="+$scope.password+"&client_secret=");
    $http({
    method: 'POST',
              url:$scope.dominio+"o/token/",
              headers: {
                        'Content-Type': "application/x-www-form-urlencoded",
                        },
              data:"client_id="+$scope.TokenHeroku +"&grant_type=password&username="+$scope.username+"&password="+$scope.password+"&client_secret="
  })
   .then(function(result){
      $scope.token = result.data;   

      console.log(result.data);
      console.log("then");
     // TokenService.setToken($scope.token.access_token);
     
      $scope.token = result.data.access_token;
    
      console.log($scope.token);
      //$state.go('home');
      $http.defaults.headers.common['Authorization']= 'Bearer ' + $scope.token ;

      $scope.getPropositos();

   });





  

  

  $scope.dia = 25;
  $scope.mes = "09";
  $scope.ano = "2015";
  $scope.showInput = [true, true, true, true] ;
  $scope.NuevoProposito = ['','','',''];
  $scope.vinculaciones = [{"id":1,"nombre":"Dios"}, {"id":2,"nombre":"Conmigo"},{"id":3,"nombre":"Con los Demás"}, {"id":4,"nombre":"Con la Naturaleza"},] 

  



$scope.searchFecha = function (dia, myArray){
    for (var i=0; i < myArray.length; i++) {
        if (myArray[i].dia === $scope.ano + "-" + $scope.mes + "-" + $scope.dia) {
            console.log(myArray[i].dia)
            return myArray[i];
        }
    }
}


	

  $scope.change = function() { /* Cuando cambio el dropdown  DE MES */
        console.log($scope.mes);  
      };


  $scope.addPropositoInput = function(vinculacion){ /* Cuando hago click en "+" de nuevo proposito */

    $scope.showInput[vinculacion] = false ;
  }




  $scope.call = function( proposito, valorMarcacion){
    console.log(proposito);
    console.log($scope.ano + "-" + $scope.mes + "-" + $scope.dia);

    console.log( searchFecha( $scope.dia , proposito.marcaciones) );

    marcacion = searchFecha( $scope.dia , proposito.marcaciones)

    if (marcacion){
      console.log("hay marcacion");
      marcacion.cumplimiento = valorMarcacion;
      $http.put('/marcaciones2/' + marcacion.id + "/", marcacion).then(function(){console.log("volvi")});


    }

    else{
       console.log(" NO hay marcacion");
         data = { 
         "dia": $scope.ano + "-" + $scope.mes + "-" + $scope.dia,
        "cumplimiento": valorMarcacion,
        "proposito": proposito.id

      }

      console.log(data);
      $http.post('/marcaciones2/', data).then(function(result){

        console.log(result);

        proposito.marcaciones.push(result.data);



    });
    }



  }

   $scope.submitNuevoProposito = function( vinculacion_id ){

    data ={
      proposito: $scope.NuevoProposito[vinculacion_id],
      mes_ano:  $scope.ano + "-" + $scope.mes + "-" + $scope.dia, /* CAmbiar por la fecha de hoy */
      vinculacion: vinculacion_id,

    }

    console.log(data);
    $http.post('/propositos2/', data ).then(function(){

      getPropositos();

      $scope.NuevoProposito[vinculacion_id] = "";
      

    });
        

  }




  }]);