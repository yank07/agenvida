agenvidaApp.controller('ResetPassCtrl', 

	function($scope, $http){
			$scope.pass = {};
		
			$scope.data = {}

			$scope.path = window.location.pathname.split('/')
			$scope.data.uid = $scope.path[4];
			$scope.data.token =  $scope.path[5];
			console.log($scope.data);
		
			$scope.mensajeShow = false;


		
		$scope.reset = function(){	

						if ($scope.pass.dos == $scope.pass.uno) {

							console.log($scope.data);
							$http.post('/auth/password/reset/confirm/',$scope.data).then(
								function(result){
									$scope.mensaje = "Contraseña cambiada. Dirijase a la aplicación e inicie sesión con la nueva contraseña"
									$scope.mensajeShow = true;

								}
							);
						}
						else {
							$scope.mensaje = "Las contraseñas no coinciden"
							$scope.mensajeShow = true;
						}

			
		}


	});
