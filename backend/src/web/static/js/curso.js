/**
 * Created by renzo on 4/24/14.
 */
var myApp = angular.module('myApp', [], function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{_');
    $interpolateProvider.endSymbol('_}');
});
""

function MyAppCtrl($scope) {
    $scope.listaDeCursos = [
        {'detalhar_path': '/', 'nome': 'PyPrático'}
    ];

    $scope.adicionarCurso = function () {
        var curso = {'nome': $scope.nomeDoCurso,
            'detalhar_path': '/',
            'descricao': $scope.descricaoDoCurso
        };
        $scope.listaDeCursos.push(curso);
        $scope.nomeDoCurso='';
        $scope.descricaoDoCurso='';
    }

}