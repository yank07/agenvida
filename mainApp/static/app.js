var agenvidaApp=angular.module('agenvidaApp', []);



agenvidaApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
});



