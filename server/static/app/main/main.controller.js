(function() {

    'use strict';

    angular
        .module('blogapp')
        .controller('MainController', MainController);

    MainController.$inject = ['$timeout'];
    function MainController($timeout) {
        var vm = this;

        vm.classAnimation = '';

        activate();

        function activate() {
            $timeout(function() {
                vm.classAnimation = 'rubberBand';
            }, 4000);
        }

    }  // <-- MainController

})();
