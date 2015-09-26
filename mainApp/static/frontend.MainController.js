

agenvidaApp.controller('PhoneListCtrl', ['$scope', '$http',
  

  function ($scope, $http) {
  

    getPropositos = function() { 

      $http.get('/propositos2/').then(function(result){
                                                        $scope.propositos = result.data;
                                                        },
                                        function(){ } 
                                     );

                              }


  $scope.dia = 25;
  $scope.mes = "09";
  $scope.ano = "2015";
  $scope.showInput = true ;

  getPropositos();



function searchFecha(dia, myArray){
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


  $scope.addPropositoInput = function(){ /* Cuando hago click en "+" de nuevo proposito */

    $scope.showInput = false ;
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
      proposito: $scope.NuevoProposito,
      mes_ano:  $scope.ano + "-" + $scope.mes + "-" + $scope.dia, /* CAmbiar por la fecha de hoy */
      vinculacion: vinculacion_id,

    }
    $http.post('/propositos2/', data ).then(function(){

      getPropositos();

      $scope.NuevoProposito = "";
      

    });
        

  }




  }]);