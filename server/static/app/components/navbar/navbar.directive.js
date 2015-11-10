(function() {
    'use strict';

    angular
        .module('blogapp')
        .directive('blogappNavbar', blogappNavbar);

    /** @ngInject */
    function blogappNavbar() {
        var directive = {
            restrict: 'E',
            templateUrl: 'static/app/components/navbar/navbar.html',
            controller: NavbarController,
            controllerAs: 'vm',
            bindToController: true
        };

        return directive;

        NavbarController.$inject = ['$auth', 'AuthService', '$rootScope'];
        function NavbarController($auth, AuthService, $rootScope) {
            var vm = this;
            vm.isAuthenticated = AuthService.isAuthenticated;
        }

    }  // <-- blogappNavbar

})();
