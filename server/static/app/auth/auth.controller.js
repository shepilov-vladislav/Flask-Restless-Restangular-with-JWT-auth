(function() {
    'use strict';

    angular
        .module('blogapp.auth')
        .controller('AuthController', AuthController);

    AuthController.$inject = ['AuthService', '$auth', '$state', '$stateParams', '$rootScope', 'API'];
    function AuthController(AuthService, $auth, $state, $stateParams, $rootScope, API) {
        var vm = this;
        vm.status = AuthService.status;
        vm.statusMessage = AuthService.statusMessage;


        vm.login = function() {
            var credentials = {
                username: vm.email,
                password: vm.password
            }
            AuthService.login(credentials, vm.remember_me).then(function(user) {
                AuthService.saveUser(user);
                $state.transitionTo('article');
            }, function(response) {
                vm.error = true;
                vm.errorMessage = response.data.description;
            });
        }

        vm.register = function() {
          AuthService.register(vm.email, vm.username, vm.password).then(function(response) {
            $state.transitionTo('auth.login', {status: true, statusMessage: response.data.message});
            AuthService.status = true;
            AuthService.statusMessage = response.data.message;
            AuthService.registered = true;
          }, function(response) {
            vm.error = true;
            vm.errorMessage = response.data.description;
          });
        }

        vm.logout = function() {
            AuthService.logout().then(function() {
                $state.transitionTo('auth.login', {status: true, statusMessage: "Successfully logged out."});
                vm.classAnimation = '';
            });
         }

    }  // <-- AuthController

})();
