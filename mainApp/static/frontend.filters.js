angular.module('phonecatFilters', []).filter('marcacion', function() {
  return function(input) {
  	console.log("hola");
    return input ? '\u2713' : '\u2718';
  };
});